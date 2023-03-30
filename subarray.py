lis = [1,2,3]
arr = []
for i in range(len(lis)):
    for j in range(i,len(lis)):
        arr.append(lis[i:j+1])
print(arr)