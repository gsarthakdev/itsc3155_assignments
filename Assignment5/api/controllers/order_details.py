from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status, Response
from ..models import models


def create(db: Session, order_detail):
    # Validate FKs exist
    if db.query(models.Order).filter(models.Order.id == order_detail.order_id).first() is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if db.query(models.Sandwich).filter(models.Sandwich.id == order_detail.sandwich_id).first() is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")

    db_od = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount,
    )
    db.add(db_od)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid order detail data")
    db.refresh(db_od)
    return db_od


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


def update(db: Session, order_detail_id, order_detail):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    if q.first() is None:
        return None
    update_data = order_detail.model_dump(exclude_unset=True)
    # Validate FKs on change
    if "order_id" in update_data:
        if db.query(models.Order).filter(models.Order.id == update_data["order_id"]).first() is None:
            raise HTTPException(status_code=404, detail="Order not found")
    if "sandwich_id" in update_data:
        if db.query(models.Sandwich).filter(models.Sandwich.id == update_data["sandwich_id"]).first() is None:
            raise HTTPException(status_code=404, detail="Sandwich not found")
    q.update(update_data, synchronize_session=False)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid order detail data")
    return q.first()


def delete(db: Session, order_detail_id):
    q = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
