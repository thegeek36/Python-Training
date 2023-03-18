#Question:
''' PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.

Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
                    If quantity is valid, return true. Else return false

Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required.
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
                       If pizza type is valid, return true. Else return false.
calculate_pizza_cost(): Calculate pizza cost. Validate pizza type and quantity.
                        If valid, Identify pizza cost based on details mentioned in the table.
                        Set attribute, pizza_cost with the calculated pizza cost.
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. 
Example – S101, s102, m103, S104, M105 etc. If invalid, set pizza_cost to -1.
PizzaType Cost/Pizza(in Rs) Additional topping cost/Pizza (in Rs), if applicable
Small 150 35
Medium 200 50

Doordelivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms.
                            If valid, return true. Else, return false.
calculate_pizza_cost(): Calculate pizza cost
Validate distance in kms. If valid, Calculate pizza cost. (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms Delivery Charge in km(in Rs)
For first 5 kms 5
For remaining 5 kms 7
Else, set pizza_cost to -1

Note: Perform case insensitive string comparison  
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details
'''

class Customer:
    def validate_quantity(self, quantity):
        if quantity >= 1 and quantity <= 5:
            return True
        else:
            return False
    
class PizzaService:
    count = 100
    
    def __init__(self,pizza_type,quantity,additional_topping,):
        self.pizza_type = pizza_type
        self.quantity = quantity
        self.additional_topping = additional_topping
        self.cost = 0

    def validate_pizza_type(self):
        if self.pizza_type.lower() == 'small' or self.pizza_type.lower() == 'medium':
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer().validate_quantity(self.quantity):
            if self.pizza_type.lower() == 'small':
                pizza_cost = self.quantity * 150
                if self.additional_topping:
                    pizza_cost += self.quantity * 35
            elif self.pizza_type.lower() == 'medium':
                pizza_cost = self.quantity * 200
                if self.additional_topping:
                    pizza_cost += self.quantity * 50
            self.pizza_cost = pizza_cost
            PizzaService.count += 1
            self.service_id = self.pizza_type[0].upper() + str(PizzaService.count)
        else:
            self.pizza_cost = -1

class Doordelivery(PizzaService):
        
        def __init__(self, pizza_type, quantity, additional_topping, distance_in_kms):
            super().__init__(pizza_type, quantity, additional_topping)
            self.distance_in_kms = distance_in_kms

        def validate_distance_in_kms(self):
            if self.distance_in_kms >= 1 and self.distance_in_kms <= 10:
                return True
            else:
                return False
            
        def calculate_pizza_cost(self):
            if self.validate_distance_in_kms():
                    super().calculate_pizza_cost()
                    if self.pizza_cost != -1:
                        if self.distance_in_kms <= 5:
                            self.pizza_cost += self.distance_in_kms * 5
                        else:
                            self.pizza_cost += 5 * 5
                            self.pizza_cost += (self.distance_in_kms - 5) * 7
                    else:
                        self.pizza_cost = -1
    

pizza1 = PizzaService('small', 3, True)
pizza1.calculate_pizza_cost()
print("ServiceId",pizza1.service_id)
print("PizzaCost in Rupees",pizza1.pizza_cost)
print("Type",pizza1.pizza_type)
print("Quantity",pizza1.quantity)



    