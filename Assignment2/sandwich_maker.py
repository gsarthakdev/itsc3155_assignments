
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount_needed in ingredients.items():
            if self.machine_resources[ingredient] < amount_needed:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Makes a sandwich and deducts ingredients."""
        # No need to check resources again - already validated in main()
        for ingredient, amount_needed in order_ingredients.items():
            self.machine_resources[ingredient] -= amount_needed
        return True