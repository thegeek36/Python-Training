#Selection Sort
def selection_sort(array,size):
    for step in range(size):
        #Step is 
        min_indx = step
        for i in range(step+1,size):
            #Select the minimum element in each loop
            if array[i] < array[min_indx]:
                min_indx = i
        #Swap with step and min_indx
        (array[step],array[min_indx] )= (array[min_indx],array[step])
    
data  = [20,233,12,100,15,22,90]
size = len(data)
selection_sort(data,size)
print(data)

'''
Time Complexity	
Best : O(n2)
Worst : O(n2)
Average : O(n2)
Space Complexity:O(1)
'''