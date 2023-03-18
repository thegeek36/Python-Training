#List Comprehension
'''
res = []
for i in range(11):
    res.append(i)
print(res)
#list comprehension version
print([i for i in range(11)])
'''
#Question 1
'''
#For loop to print odd elements ---> odd elements
res = []
for i in range(11):
    if i % 2!=0:
        res.append(i)
print(res)
res = [i for i in range(11) if i%2 == 0]
print(res)
res =[i if i%2 == 0 else i**2 for i in range(11)]
print(res)
'''
#Question 2
'''
for i in range(8):
    for j in range(8):
        if i == 0 or j == 0 or i == 7 or j == 7:
            print(("'----'"), end=" ")
        else:
            print((j,i), end= " ")
    print()

ans = [[(j,i) if i not in (0,7) and j  not in (0,7) else ('----') for i in range(8)] for j in range(8)]
for i in ans: print(i)

mat  = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#odd -> square it
#even -> cube it
res=[]
for i in mat:
    for ele in i:
        ans = []
        if ele % 2 ==0:
            ele = ele **3
            ans.append(ele)
        else:
            ele = ele ** 2
            ans.append(ele)    
print(res)

mat  = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[ele**2 if ele%2 != 0 else ele**3 for ele in row] for row in mat])
'''
#Question 3
#for each number in list b get the number and its position in my list as are turn list if tuples
'''
my_list =[9,3,6,1,5,0,8,2,4,7]
list_b =[6,4,6,1,2,2]
ans = []
#result = [(6,2),(4,8)1,3),(2,7)]
for num in list_b:
    ele = my_list.index(num)
    if (num,ele) not in ans:
        ans.append((num,ele))
print(ans)

print({i:my_list.index(i) for i in list_b})

sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
results = []    
for sentence in sentences:
    sentence_tokens = []
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_tokens.append(word)
    results.append(sentence_tokens)

results = [word for sentence in sentences for word in sentence.split(' ') if word not in stopwords]
print(results)

alph = {chr(i):i-96 for i in range(97,123)}
word = "Hi Iam Priyanshu"
for i in word.lower():
    if i in alph:
        print(i, alph[i])
'''
#Quesstion 4
'''
ar = list(map(int,input().split(",")))
num1 = 0
num2 = ""
ind5 = ar.index(5)
ind8 = ar.index(8)
for i in range(len(ar)):
    if i not in range(ind5,ind8+1):
        num1 += int(ar[i])
l = (ar[ind5:ind8+1])
for i in l:
    num2+=str(i)
print("Num1 ",num1)
print("Num2",num2)
print(int(num1)+int(num2))
'''
#Question 5
'''
s = input().split(":")
for i in s:
    if(i.isdigit()):
        n = i
    else:
        str = i

def sqr(n):
    ans = 0
    while n!=0:
        rem = n%10
        ans += rem ** 2
        n //= 10
    return ans

if sqr(int(n)) %2==0:
    print(str[-1]+str[:-1])
else:
    print(str[-2]+str[:-2])
'''