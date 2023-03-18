#Data Types
'''
name = "Priyanshu"
# print("Name :",name,type(name))
# roll = 10
# print("Roll :",roll,type(roll))
# mark = 88.8
# print("Mark :",mark,type(mark))'''

#multiple 0f 3, multiple of 5 and both else 45invalid
'''
n = int(input("Enter Number"))
if n%3==0 and n%5==0:
    print("Divisible by both 3 and 5")
elif n%5==0:
    print("Divisible by 5")
elif n%3==0:
    print("Divisible by 3")
else:
    print("Invalid")  '''


#Range function for loop
'''
for i in range (1,101):
        print(i,end=" ")
print(end="\n")
print("Even Number")
for i in range(2,101,2):
        print(i,end =" ")
print(end="\n")
print("Odd Number")
for i in range(1,101,2):
        print(i,end =" ")'''
'''
print("Reverse")
for i in range(100,0,-1):
        print(i,end =" ")
print()
print("Even Reverse")
for i  in range(100,0,-2):
        print(i,end = " ")
print()
print("Odd Reverse")
for i in range(99,0,-2):
        print(i,end=" ") 
'''
    
#use a for loop and iterate between 1 - 100 and come out  of the loop as we reach 50
#Break and Continue
'''
for i in range(1,101):
        if i==50:
            break
        print(i,end=" ")
print()
print()
for i in range(1,101):
        if i==50:
            continue
        print(i,end=" ")
'''

#Functions
'''
def function1():
      print("It is Function 1")
function1()
def function2(num1,num2):
      print("Num1 ",num1,"Num2 ",num2)
function2(10,20)
def function3(num1,num2):
      num3 =num1+num2
      return num3
print(function3(100,200.9))

def fun4(num1,num2):
      num3 = float(num1)+num2
      return num3
print(fun4('12',56.9))
'''
#Categories of functions based on Arguments
'''
#1.Positional Arguments
def fun1(num1,num2,num3,num4):
      print("num1 ",num1,"num2 ",num2,"num3 ",num3,"num4 ",num4)
#fun1(100,234,543,890.9)
fun1(num1=100,num4=234,num2="63",num3=890.9)

def fun2(name,roll,branch,college ="GIET"):
      print(name," ",roll," ",branch," ",college)

fun2("Priyanshu",23,"CSE")
fun2("Priyanshu",24,"CSE")

#var is used to take n number of arguments.
def fun4(*var):
      for i in var:
            print(i,end = ' ')
            
fun4(10,20)
fun4(10,20,30,40,50)

def sum1(*var):
    s = 0 
    for i in var:
        s += i
    print(s)

sum1(1245,556,67)
'''

#Question 1
'''
a,b,c = map(int,input().split())
prod  = 1
if(a==7):
     prod = b*c
elif b == 7:
     prod = c
elif c == 7:
     prod = -1
else:
     prod = a*b*c
print(prod)
'''
#Question 2
'''
curr = input()
inr = int(input())
if(curr == "Euro"):
     print(inr * 0.01417," Euro")
elif(curr == "British Pound"):
     print(inr*0.0100," British Pound")
elif(curr == "Australian Dollar"):
     print(inr*0.02140," Australian Dollar")
elif(curr=="Canadian Dollar"):
     print(inr*0.02027," Canadian Dollar")
else:
    print("-1")
'''
#Question 3
'''
ad = int(input())
chld = int(input())
r_adlt = 37550.0
r_chld = r_adlt/3
fare = ad*r_adlt+chld*r_chld
tax = 0.07*fare
disc = (tax+fare)*0.10
total = (fare+tax-disc)
print(total)

ad = int(input())
chld = int(input())
print(37550.0*ad+(37550.0/3)*chld+0.07*(37550.0*ad+(37550.0/3)*chld)-0.10*(37550.0*ad+(37550.0/3)*chld+0.07*(37550.0*ad+(37550.0/3)*chld)))

'''
#Question 4
'''
x  = int(input("Amount of 5 rs coin"))
y  = int(input("Amount of 1 rs coin"))
z  = int(input("Amount to be paid"))
rs5  = 0
rs1 = 0 
total = 5*x + 1*y
if z > total:
    print("Invalid")
while(z!=0):
    if z >= 5:
        rs5 = z//5
        z = z%5
    else:
        rs1 = z//1
        z = z%10
        break
print("5 rs",rs5,"1rs",rs1)
'''

