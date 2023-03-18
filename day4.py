#Wap nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
#I/P 999 O/P - 1001
'''
def nearest_palindrome(num):
    start = num + 1
    while not ispalindrome(start):
        start += 1
    return start

def ispalindrome(num):
    s = str(num)
    return num == int(s[::-1])

print(nearest_palindrome(99))

import sys
def next_palindrome(num):
    for  i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
print(next_palindrome(101))

def near_palindorme(num):
    st = num+1
    while(1):
        if st == int(str(st)[::-1]):
            return st
        st += 1
print(near_palindorme(10005))
'''
#Question 2:
'''
d = {"P":"Pedatrics", "E":"ENT","O":"Orthopedics"}
l = list(input("Enter").split())
p_cnt = 0
o_cnt = 0
e_cnt = 0
for i in l:
    if i == 'P':
        p_cnt += 1
    elif i == 'E':
        e_cnt += 1
    elif i == 'O':
        o_cnt += 1
if p_cnt > e_cnt and p_cnt>o_cnt: print(d['P'])
if e_cnt > p_cnt and e_cnt>o_cnt: print(d['E'])
if o_cnt > e_cnt and o_cnt>p_cnt: print(d['O'])
'''
#Question 3
'''
s1 = input()
s2 = input()
s = ""
for i in s1:
    if i in s2 and i != ' ':
        s += i
print(s)
'''

