"""
This is a calculator program that demonstrates horrible coding practices
It violates DRY, Single Responsibility, and Clean Code principles. 
It pretty much also violates the Document your Code principle.
"""

import math
import random

# Global variables everywhere
result = 0
history = []
user_name = ""
current_operation = ""
debug_mode = False
calculation_count = 0
pi_value = 3.14159
e_value = 2.71828

# One massive function that does everything
def calculator():
    global result, history, user_name, current_operation, debug_mode, calculation_count
    
    print("Welcome to the Ultimate Calculator!")
    print("This calculator can do everything!")
    
    # Get user input
    user_name = input("What's your name? ")
    print(f"Hello {user_name}!")
    
    # Main loop
    while True:
        print("\n" + "="*50)
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract") 
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. Show history")
        print("8. Clear history")
        print("9. Debug mode")
        print("10. Random number")
        print("11. Show pi")
        print("12. Show e")
        print("13. Calculate area of circle")
        print("14. Calculate factorial")
        print("15. Exit")
        
        choice = input("Enter your choice (1-15): ")
        
        if choice == "1":
            # Add operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 + num2
            current_operation = f"{num1} + {num2} = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "2":
            # Subtract operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 - num2
            current_operation = f"{num1} - {num2} = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "3":
            # Multiply operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            current_operation = f"{num1} * {num2} = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "4":
            # Divide operation
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero!")
                result = 0
            else:
                result = num1 / num2
            current_operation = f"{num1} / {num2} = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "5":
            # Power operation
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            result = num1 ** num2
            current_operation = f"{num1} ^ {num2} = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "6":
            # Square root operation
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot calculate square root of negative number!")
                result = 0
            else:
                result = math.sqrt(num)
            current_operation = f"sqrt({num}) = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Result: {result}")
            
        elif choice == "7":
            # Show history
            print("Calculation History:")
            for i, calc in enumerate(history):
                print(f"{i+1}. {calc}")
                
        elif choice == "8":
            # Clear history
            history.clear()
            calculation_count = 0
            print("History cleared!")
            
        elif choice == "9":
            # Debug mode toggle
            debug_mode = not debug_mode
            print(f"Debug mode: {'ON' if debug_mode else 'OFF'}")
            
        elif choice == "10":
            # Random number
            min_val = float(input("Enter minimum value: "))
            max_val = float(input("Enter maximum value: "))
            result = random.uniform(min_val, max_val)
            current_operation = f"Random({min_val}, {max_val}) = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Random number: {result}")
            
        elif choice == "11":
            # Show pi
            print(f"Pi = {pi_value}")
            result = pi_value
            
        elif choice == "12":
            # Show e
            print(f"E = {e_value}")
            result = e_value
            
        elif choice == "13":
            # Calculate area of circle
            radius = float(input("Enter radius: "))
            if radius < 0:
                print("Error: Radius cannot be negative!")
                result = 0
            else:
                result = pi_value * radius * radius
            current_operation = f"Area of circle (r={radius}) = {result}"
            history.append(current_operation)
            calculation_count += 1
            print(f"Area: {result}")
            
        elif choice == "15":
            # Exit
            print(f"Goodbye {user_name}! You performed {calculation_count} calculations.")
            break
            
        else:
            print("Invalid choice! Please try again.")
            
        # Debug information
        if debug_mode:
            print(f"Current result: {result}")
            print(f"History length: {len(history)}")
            print(f"Calculation count: {calculation_count}")

# Main execution
if __name__ == "__main__":
    calculator()
