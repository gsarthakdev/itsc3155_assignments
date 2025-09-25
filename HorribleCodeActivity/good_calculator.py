import math
from dataclasses import dataclass


@dataclass
class CalculationResult:
    """Data class to represent a calculation result."""
    operation: str
    operands: tuple
    result: float
    timestamp: str


class InputValidator:
    """Handles input validation for the calculator."""
    
    @staticmethod
    def validate_number(value):
        """Validate and convert string input to float."""
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid number: {value}")
    
    @staticmethod
    def validate_positive_number(value):
        """Validate that input is a positive number."""
        num = InputValidator.validate_number(value)
        if num < 0:
            raise ValueError("Number must be positive")
        return num
    
    @staticmethod
    def validate_non_zero(value):
        """Validate that input is not zero."""
        num = InputValidator.validate_number(value)
        if num == 0:
            raise ValueError("Number cannot be zero")
        return num


class CalculationHistory:
    """Manages calculation history."""
    
    def __init__(self):
        self._history = []
    
    def add_calculation(self, operation, operands, result, timestamp):
        """Add a calculation to history."""
        calc_result = CalculationResult(operation, operands, result, timestamp)
        self._history.append(calc_result)
    
    def get_history(self):
        """Get all calculation history."""
        return self._history.copy()
    
    def clear_history(self):
        """Clear all calculation history."""
        self._history.clear()
    
    def get_history_count(self):
        """Get the number of calculations performed."""
        return len(self._history)


class BasicOperations:
    """Handles basic mathematical operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract second number from first."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide first number by second."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    @staticmethod
    def power(base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent


class AdvancedOperations:
    """Handles advanced mathematical operations."""
    
    @staticmethod
    def square_root(number):
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(number)
    
    @staticmethod
    def factorial(n):
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n > 20:  # Prevent extremely large calculations
            raise ValueError("Factorial too large (max 20)")
        
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    @staticmethod
    def circle_area(radius):
        """Calculate area of a circle."""
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius


class Calculator:
    """Main calculator class that orchestrates all operations."""
    
    def __init__(self):
        self.history = CalculationHistory()
        self.basic_ops = BasicOperations()
        self.advanced_ops = AdvancedOperations()
        self.validator = InputValidator()
    
    def _get_user_input(self, prompt, validator_func=None):
        """Get validated input from user.
        It's private (the underscore prefix) because it's only used internally by the calculator.
        """
        while True:
            try:
                value = input(prompt)
                if validator_func:
                    return validator_func(value)
                return self.validator.validate_number(value)
            except ValueError as e:
                print(f"Error: {e}")
                print("Please try again.")
    
    def _record_calculation(self, operation, operands, result):
        """Record calculation in history.
        It's private (the underscore prefix) because it's only used internally by the calculator.
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.add_calculation(operation, operands, result, timestamp)
    
    def perform_addition(self):
        """Perform addition operation."""
        a = self._get_user_input("Enter first number: ")
        b = self._get_user_input("Enter second number: ")
        result = self.basic_ops.add(a, b)
        self._record_calculation("Addition", (a, b), result)
        print(f"Result: {a} + {b} = {result}")
    
    def perform_subtraction(self):
        """Perform subtraction operation."""
        a = self._get_user_input("Enter first number: ")
        b = self._get_user_input("Enter second number: ")
        result = self.basic_ops.subtract(a, b)
        self._record_calculation("Subtraction", (a, b), result)
        print(f"Result: {a} - {b} = {result}")
    
    def perform_multiplication(self):
        """Perform multiplication operation."""
        a = self._get_user_input("Enter first number: ")
        b = self._get_user_input("Enter second number: ")
        result = self.basic_ops.multiply(a, b)
        self._record_calculation("Multiplication", (a, b), result)
        print(f"Result: {a} × {b} = {result}")
    
    def perform_division(self):
        """Perform division operation."""
        a = self._get_user_input("Enter first number: ")
        b = self._get_user_input("Enter second number: ", 
                                self.validator.validate_non_zero)
        result = self.basic_ops.divide(a, b)
        self._record_calculation("Division", (a, b), result)
        print(f"Result: {a} ÷ {b} = {result}")
    
    def perform_power(self):
        """Perform power operation."""
        base = self._get_user_input("Enter base: ")
        exponent = self._get_user_input("Enter exponent: ")
        result = self.basic_ops.power(base, exponent)
        self._record_calculation("Power", (base, exponent), result)
        print(f"Result: {base}^{exponent} = {result}")
    
    def perform_square_root(self):
        """Perform square root operation."""
        number = self._get_user_input("Enter number: ", 
                                    self.validator.validate_positive_number)
        result = self.advanced_ops.square_root(number)
        self._record_calculation("Square Root", (number,), result)
        print(f"Result: √{number} = {result}")
    
    def perform_circle_area(self):
        """Calculate area of a circle."""
        radius = self._get_user_input("Enter radius: ", 
                                    self.validator.validate_positive_number)
        result = self.advanced_ops.circle_area(radius)
        self._record_calculation("Circle Area", (radius,), result)
        print(f"Result: Area of circle with radius {radius} = {result:.2f}")
    
    def show_history(self):
        """Display calculation history."""
        history = self.history.get_history()
        if not history:
            print("No calculations performed yet.")
            return
        
        print("\nCalculation History:")
        print("-" * 50)
        for i, calc in enumerate(history, 1):
            operands_str = ", ".join(map(str, calc.operands))
            print(f"{i}. {calc.operation}({operands_str}) = {calc.result}")
            print(f"   Time: {calc.timestamp}")
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear_history()
        print("History cleared successfully.")
    
    def show_constants(self):
        """Display mathematical constants."""
        print(f"π (Pi) = {math.pi:.10f}")
        print(f"e (Euler's number) = {math.e:.10f}")


class CalculatorUI:
    """Handles user interface for the calculator."""
    
    def __init__(self):
        self.calculator = Calculator()
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("Calculator Menu")
        print("=" * 50)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Circle Area")
        print("8. Show History")
        print("9. Clear History")
        print("10. Show Constants")
        print("11. Exit")
        print("-" * 50)
    
    def get_user_choice(self):
        """Get user's menu choice."""
        return input("Enter your choice (1-11): ").strip()
    
    def handle_menu_choice(self, choice):
        """Handle user's menu choice. Returns False if we want to exit."""
        try:
            if choice == "1":
                self.calculator.perform_addition()
            elif choice == "2":
                self.calculator.perform_subtraction()
            elif choice == "3":
                self.calculator.perform_multiplication()
            elif choice == "4":
                self.calculator.perform_division()
            elif choice == "5":
                self.calculator.perform_power()
            elif choice == "6":
                self.calculator.perform_square_root()
            elif choice == "7":
                self.calculator.perform_circle_area()
            elif choice == "8":
                self.calculator.show_history()
            elif choice == "9":
                self.calculator.clear_history()
            elif choice == "10":
                self.calculator.show_constants()
            elif choice == "11":
                return False
            else:
                print("Invalid choice. Please enter a number between 1-11.")
        except ValueError as e:
            print(f"Calculation error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        return True
    
    def run(self):
        """Main application loop."""
        print("Welcome to the Calculator!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if not self.handle_menu_choice(choice):
                break
        
        print("Thank you for using our calculator!")


def main():
    """Main entry point of the application."""
    ui = CalculatorUI()
    ui.run()


if __name__ == "__main__":
    main()
