import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    """Main function to run the sandwich maker machine."""
    is_on = True
    
    while is_on:
        print("\nWelcome to the Sandwich Maker Machine!")
        print("What would you like?")
        print("1. Small sandwich - $1.75")
        print("2. Medium sandwich - $3.25") 
        print("3. Large sandwich - $5.50")
        print("4. Report")
        print("5. Turn off")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            sandwich_size = "small"
        elif choice == "2":
            sandwich_size = "medium"
        elif choice == "3":
            sandwich_size = "large"
        elif choice == "4":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slices")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slices")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces")
            continue
        elif choice == "5":
            print("Turning off the machine. Goodbye!")
            is_on = False
            continue
        else:
            print("Invalid choice. Please try again.")
            continue
            
        # Check if resources are sufficient
        if not sandwich_maker_instance.check_resources(recipes[sandwich_size]["ingredients"]):
            print("Sorry, there are not enough ingredients to make that sandwich.")
            continue
            
        # Process payment
        cost = recipes[sandwich_size]["cost"]
        print(f"That will be ${cost:.2f}")
        payment = cashier_instance.process_coins()
        
        if cashier_instance.transaction_result(payment, cost):
            # Make the sandwich
            if sandwich_maker_instance.make_sandwich(sandwich_size, recipes[sandwich_size]["ingredients"]):
                print(f"Here is your {sandwich_size} sandwich. Enjoy!")
            else:
                print("Sorry, there was an error making your sandwich.")

if __name__=="__main__":
    main()
