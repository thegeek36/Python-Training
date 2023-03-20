#Question 1
''' Question
A bank has many customers and each customer has a bank account
There are also privileged customers 
who can earn bonus points for each of their transaction. 
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- account
__init__(customer_id, customer_name, age, account)
+ withdraw(amount)
+ take_card()
+ get_customer_id()
+ get_customer_name()
+ get_age()
+ get_account()
Account
- account_type
- balance
- min_balance
__init__(account_type,balance,min_balance)
+ get_account_type()
+ get_balance()
+ get_min_balance()
+ set_balance(balance)
PrivilegedCustomer
- bonus_points
__init__ (customer_id, customer_name, age, account, 
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the account balance based on the amount withdrawn. 
Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than account balance.
LimitReachedException - If the balance amount is less than minimum account balance.
take_card(): Displays the message "Take card out from the ATM".
PrivilegedCustomer:
increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method, if no exceptions occured.
If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

Write a Python program to create a new PrivilegedCustomer with below details:
Customer Id: 100
Customer Name: Gopal
Age: 43
Bonus Points: 100
Account Type: Savings
Account Balance: 1000
Account minimum: 500

The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw. 
'''
''' Answer'''

class Account:
    def __init__(self, account_type, balance, min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance

    def get_account_type(self):
        return self.__account_type
    
    def get_balance(self):
        return self.__balance
    
    def get_min_balance(self):
        return self.__min_balance
    
    def set_balance(self, balance):
        self.__balance = balance
        
class Customer:
    def __init__(self, customer_id, customer_name, age, account):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__age = age
        self.__account = account

    def withdraw(self, amount):
        bal = Account.get_balance(self.__account)
        min_bal = Account.get_min_balance(self.__account)
        new_bal = bal - amount
        if  bal < amount:
            raise OverdrawException
        elif new_bal < min_bal:
            raise LimitReachedException
        Account.set_balance(self.__account, new_bal)
        print("Withdraw Sucessfull")
        #print("Balance Left:",Account().balance)

    def take_card(self):
        print("Take card out from the ATM")
    
    def get_customer_id(self):
        return self.__customer_id
    
    def get_customer_name(self):
        return self.__customer_name
    
    def get_age(self):
        return self.__age
    
    def get_account(self):
        return self.__account
    

class OverdrawException(Exception):
    pass


class LimitReachedException(Exception):
    pass


class PrivilegedCustomer(Customer):
    def __init__ (self,customer_id, customer_name, age, account, bonus_points):
        self.__bonus_points = bonus_points
        super().__init__(customer_id,customer_name,age,account)

    def __increase_bonus(self):
        Account=self.get_account()
        if Account.get_balance() > 1000:
            self.__bonus_points += 10
        else:
            self.__bonus_points += 2

    def withdraw(self,amount):
        Customer.withdraw(self,amount)
        self.__increase_bonus()

    def get_bonus_points(self):
        return self.__bonus_points

a = Account("Savings",10000,3000)
c = Customer("100","Priyanshu",18,a)
p = PrivilegedCustomer("C101","Priyanka",22,a,100)

try:
    print("Customer Id: "+str(c.get_customer_id()))
    print("Customer Name: "+c.get_customer_name())
    print("Age: "+str(c.get_age()))
    print("Account Type: "+a.get_account_type())
    print("Account Balance: "+str(a.get_balance()))
    print("Account minimum: "+str(a.get_min_balance()))
    p.withdraw(400)
    print("Account Balance after withdraw: "+str(a.get_balance()))
    print("Bonus Points: "+str(p.get_bonus_points()))
except OverdrawException:
    print("amount to be withdrawn is greater than account balance.")
except LimitReachedException:
    print("balance amount is less than minimum account balance.")
finally:
    c.take_card()

        
            


