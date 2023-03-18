#Class and Objects in Python Day 5
'''
class Customer:
    #Constructor
    def __init__(self,cust_id):
        self.cust_id = 100
c1 = Customer(100)
print(c1.cust_id)

class Book:
    def __init__(self):
        self.title = None
my_fav =Book()
my_fav.title = "Let us C"
your_fav = Book()
your_fav.title = "Learn Python the hard way"
print("My favourite is :",my_fav.title)
print("Your favourite :",your_fav.title)
'''
#Questions 2
'''
class Shoe:
    def __init__(self,price,material):
        self.price  = price
        self.material = material
    def __str__(self):
        return "Shoe with material "+str(self.material)+" and price "+str(self.price)
s1 = Shoe(1000,"Canvas")
s2 = Shoe(990,"Formal")
print(s1)
print(s2)
print("The Id of S1 is ",id(s1))
print(s1.material," ",s1.price)
print(s2.material," ",s2.price)
'''
#Question 3
'''
class Mobile:
    def __init__(self, brand, price): 
        self.brand = brand 
        self.total_price = None
        self.price = price
    def purchase(self): 
        if self.brand == "Apple": discount = 10
        else: discount = 5

        self.total_price = self.price- self.price*(discount / 100) 
        print("Total price of", self.brand, "mobile is",self.total_price)

mob1 = Mobile("Apple",20000)
mob2 = Mobile("Samsung ",10000)
mob1.purchase()
mob2.purchase()

class Customer:
    def __init__(self, cust_id, name, age, __wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = __wallet_balance
    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount
    def get_wallet_balance(self):
            print("Balance: ",self.__wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.get_wallet_balance()
c1.get_wallet_balance()

class Dam:
    def __init__(self, name, length): 
        self.__length = length
        self.name=name
    def get_length(self):
        return self.__length

dam = Dam("ABC",35)
print("Dam name:", dam.name) 
print("Dam Length", dam.get_length())
'''
#Question 4
'''
class Table:
    def _init_(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None

    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top

    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(True, False)
print("Rate = ",rate)


class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None

dining_table=Table()
back_table=Table()
front_table=back_table
back_table = dining_table
print(id(dining_table),id(back_table),id(front_table))
'''