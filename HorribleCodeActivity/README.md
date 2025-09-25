# Horrible Code Activity

## Quick summary
The principles I chose to demonstrate are:
1. DRY (Don't Repeat Yourself)
2. Single Responsibility Principle
3. Clean Code

`bad_calculator.py` violates these principles. 

`good_calculator.py` follows these principles.

## How I violated and then fixed/used these principles:

### 1. DRY (Don't Repeat Yourself)

#### What I did wrong in `bad_calculator.py`:
- I kept repeating the same input validation code for every operation
- Every single operation had the exact same code for recording calculations in history
- I wrote similar error handling code over and over again
- The input prompts and result display logic were basically copy-pasted everywhere

```python
# Example of repeated code in bad version:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
current_operation = f"{num1} + {num2} = {result}"
history.append(current_operation)
calculation_count += 1
print(f"Result: {result}")
```

#### How I fixed it in `good_calculator.py`:
- I created an `InputValidator` class that handles all the input validation in one place
- Made a `CalculationHistory` class that manages all the history stuff
- Extracted common operations into reusable functions so I don't repeat myself
- Used a consistent structure for all operations so they all work the same way

```python
# Example of DRY implementation:
def _get_user_input(self, prompt: str, validator_func=None) -> float:
    """Get validated input from user."""
    while True:
        try:
            value = input(prompt)
            if validator_func:
                return validator_func(value)
            return self.validator.validate_number(value)
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")
```

### 2. Single Responsibility Principle

#### What I did wrong in `bad_calculator.py`:
- I put everything in one giant `calculator()` function that does way too much:
  - Shows the user interface
  - Validates input
  - Does all the math operations
  - Manages the history
  - Handles errors
  - Displays the menu
- I mixed up business logic, UI stuff, and data management all in the same place
- It's impossible to test individual parts because everything is tangled together

#### How I fixed it in `good_calculator.py`:
- I split everything into separate classes that each do one thing:
  - `InputValidator`: Just handles input validation
  - `CalculationHistory`: Just manages calculation history
  - `BasicOperations`: Just does basic math operations
  - `AdvancedOperations`: Just does advanced math operations
  - `Calculator`: Just orchestrates the operations
  - `CalculatorUI`: Just handles the user interface
- Now each class can be tested on its own
- Each class has a clear, single purpose

### 3. Clean Code Principles

#### What I did wrong in `bad_calculator.py`:
- Used terrible variable names like `num1`, `num2`, `choice`
- Had magic numbers everywhere without explaining what they mean
- The main function was over 200 lines long (way too long!)
- Barely any comments and no docstrings
- Used way too many global variables
- Inconsistent formatting and spacing
- No proper error handling, just basic try-catch without really managing errors

#### How I fixed it in `good_calculator.py`:
- Used descriptive names like `perform_addition()` and `validate_positive_number()`
- Defined mathematical constants properly so you know what they are
- Made each function short and focused on one thing
- Added comprehensive docstrings for all classes and methods
- Used proper encapsulation with private methods
- Made the formatting consistent and PEP 8 compliant
- Added robust error handling with meaningful error messages
