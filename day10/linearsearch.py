#Linear Search in Python 
#Time Complexity O(N) 
def linear_search(arr,key):
    for i in range(0,len(arr)) :
        if arr[i] == key:
            return i
    return -1

arr = list(map(int,input("Enter array").split()))
key = int(input("Enter the key"))
ind = linear_search(arr,key)
if (ind == -1):
    print("Element not found")
else:
    print("Element found at:",ind)

