from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, recipe):
    # Validate FKs exist
    if db.query(models.Sandwich).filter(models.Sandwich.id == recipe.sandwich_id).first() is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    if db.query(models.Resource).filter(models.Resource.id == recipe.resource_id).first() is None:
        raise HTTPException(status_code=404, detail="Resource not found")

    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount,
    )
    db.add(db_recipe)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        # Likely unique constraint on (sandwich_id, resource_id) or FK issue
        raise HTTPException(status_code=409, detail="Recipe for this sandwich and resource already exists")
    db.refresh(db_recipe)
    return db_recipe


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update(db: Session, recipe_id, recipe):
    db_recipe_q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    existing = db_recipe_q.first()
    if existing is None:
        return None

    update_data = recipe.model_dump(exclude_unset=True)
    # If FKs are changing, validate
    if "sandwich_id" in update_data:
        if db.query(models.Sandwich).filter(models.Sandwich.id == update_data["sandwich_id"]).first() is None:
            raise HTTPException(status_code=404, detail="Sandwich not found")
    if "resource_id" in update_data:
        if db.query(models.Resource).filter(models.Resource.id == update_data["resource_id"]).first() is None:
            raise HTTPException(status_code=404, detail="Resource not found")

    db_recipe_q.update(update_data, synchronize_session=False)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Recipe for this sandwich and resource already exists")
    return db_recipe_q.first()


def delete(db: Session, recipe_id):
    # Query the database for the specific recipe to delete
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    # Delete the database record without synchronizing the session
    db_recipe.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

