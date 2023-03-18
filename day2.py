#Lists -> Ordered , Default Index
'''
list1 = [12,34,55,67,787,62]
print(list1,type(list1))
list2 = [12,34.56,"Hello",(56+8j)]
print(list2,type(list2))
'''
#Insertion
'''
list1.append(233)
print(list1)
#insert(<index>,<number>)
list1.insert(0,51)
print(list1)
'''
#deletion
'''
list2.remove((56+8j))
list1.pop(3)
del list1[2]
print(list1)
print(list2)
'''
#Question 1
'''
def answer(str):
    alph=0
    dig = 0
    for i in str:
        if i.isalpha():
            alph += 1
        elif i.isdigit():
            dig += 1
    return [alph,dig]

print(answer("INFOSYS 123 %&*"))
'''
#Question 2
'''
def sumpair(list,target):
    cnt = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j] == target:
                cnt+=1
    return cnt
print(sumpair([2,3,45,6,7],4))
'''
#Question 3
'''
def fun3(str):
    if (len(str) < 2):
        return -1
    elif (len(str) == 2):
        return str*2
    else:
        return str[0:2]+str[-2:]
s = input("Enter the String ")
print(fun3(s))
'''
#Question 4
'''
def func(str):
    if len(str) < 3:
        return str
    elif str[-3:] == "ing":
        return str+"ly"
    else:
        return str+"ing"
print(func("amazing"))
'''
#Question 5
'''
def check_double(num):
    double = num*2
    if(len(str(num)) == len(str(double))) and (set(str(num)) == set(str(double))):
        return True
    else:
        return False
print(check_double(245))
'''
#Question 6
'''
def find_more_than_average(marks):
    avg = sum(marks)/len(marks)
    cnt = 0
    for i in marks:
        if i > avg:
            cnt += 1
    return cnt/len(marks)*100

print(find_more_than_average((12,18,25,24,2,5,18,20,20,21)))

def generate_frequency(marks):
    l = []
    for i in range(26):
        l.append(marks.count(i))
    return l

print(generate_frequency((12,18,25,24,2,5,18,20,20,21)))

def sort_marks(marks):
    marks = list(marks)
    marks.sort()
    return marks
print(sort_marks((12,18,25,24,2,5,18,20,20,21)))
'''
#Question 7
'''
def translate(d,word):
    trans = []
    for i in word.split():
        if i in dict:
            trans.append(dict[i])
    return trans

d = {'merry':'god','christimas':'jul','and':'och','happy':'gott','new':'nytt','year':'ar'}
words = "happy new year all"
print(translate(d,words))
'''
#Question 8
"""
a = int(input())
b = int(input())
l = []
for i in range(a,b+1):
    l.append(i)
lists = []
for i in range(1,len(l)+1):
    for j in range(i):
        lists.append(l[j: i])
print(lists)
c = 0
for i in lists:
    if sum(i) % 2 != 0:
        c+=1
print(c)


a = int(input())
b = int(input())
arr= [i for i in range(a,b+1)]
l1 = [arr[i:j+1] for i in range(len(arr)) for j in range(i,len(arr))
print(l1)
c = 0
for i in l1:
    if sum(i) % 2 == 0:
        c+=1
print(c)
"""