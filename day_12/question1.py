'''
Coorg Fruit Farm is a retail chain which sells fruits grown in their orchards in Coorg, India.40 min
They want to keep track of customers who buy fruits from them and also the billing process.
Write a python program to implement the class diagram given below.
RULES TO FOLLOW
=================
Class Description:
Fruit Info class:
fruit_name_list: Static list which contains the list of fruits available
fruit_price_list: Static list which contains the price/kg of fruits
The above two lists have one-to-one correspondence, initialize it with the data given in the table
get_fruit_price(fruit_name): Accept a fruit name and return its price/kg. If fruit is not available, return -1
Fruit Name	Apple	Guava	Orange	Grape	Sweet Lime
Price per Kg	200	80	70	110	60Purchase class:
Initialize static variable counter to 101
calculate_price(): Calculate and return total fruit price based on rules given below
For valid fruit name (hint: invoke get_fruit_price(fruit_name)),
Calculate price based on price/kg and quantity of the fruit purchased by the customer
If price/kg of the fruit is maximum among the fruits in fruit lists and quantity purchased is more than 1kg, apply 2% discount on calculated price
If price/kg of the fruit is minimum among the fruits in fruit lists and quantity purchased is 5kg or more, apply 5% discount on calculated price
If the customer is a "wholesale" customer, provide an additional 10% discount. Apply this discount on already discounted price, 
if any one of the above two points are applicable. Else apply it on calculated price
Auto-generate purchase id starting from 101 prefixed by “P”. Example  P101,P102 P103 etc.
Return final fruit price
Else, return -1.
Note:
Perform case sensitive string comparison 
There will be only one fruit with maximum price and one with minimum price
For testing:
Create objects of Customer and Purchase class
Invoke calculate_price() on Purchase object
Display the details
'''