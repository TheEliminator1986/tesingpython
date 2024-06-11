class Restaurant():
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        msg = f'{self.name} is the name of the restaurant!'
        print(f'\n{msg}')
        
    def open_restaurant(self):
        msg = f'{self.name} is currently open'
        print(f'\n{msg}')
        
    def set_number_served(self, number_served):
        self.number_served = number_served
        
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        
restaurant = Restaurant('Rosatti', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 100
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(2000)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(250)
print(f"Number served: {restaurant.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
        
    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
            
the_cream_shop = IceCreamStand("The Cream Shop")
the_cream_shop.flavors = ['vanilla', 'chocolate', 'mint']

the_cream_shop.describe_restaurant()
the_cream_shop.show_flavors()            
        
        