#Binary Search in Python 
#1 2 3 4 5 6 7 8 9 
#Time Complexity is O(log n)
def binarySearch(arr,start,end,key):
    while start <= end:
        mid = end +(start-end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid -1
        else:
            start = mid+1
    return -1

arr = list(map(int,input("Enter sorted array").split()))
key = int(input("Enter the key to search"))
n = len(arr)
ind = binarySearch(arr,0,n-1,key)
if ind == -1:
    print("Element not found")
else:
    print("Element found at index:",ind)


