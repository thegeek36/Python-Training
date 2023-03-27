'''
Given two queues, one integer queue and another character queue, write a python program to merge them to form a single queue.
Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues.
For example,
Input -- queue1: 3,6,8 queue2: b,y,u,t,r,o
Output 3,b,6,y,8,u,t,r,o
'''
import queue_1 as q

def merge_queue(queue1,queue2):
    list1=[]
    list2=[]
    list3=[]
    
    while (not queue1.is_empty()):
        list1.append(queue1.dequeue())
    
    while (not queue2.is_empty()):
        list2.append(queue2.dequeue())
    
    check=0    
    if len(list1)<len(list2):
        length=len(list1)    
    else:
        length=len(list2)
        check=1
    
    if str(list1[0]).isdigit():
        integer=list1
        string=list2
    else:
        integer=list2
        string=list1
    flag=0
    j,k=0,0
    for i in range(0,2*length):
        if flag==0:
            list3.append(integer[j])
            flag=1
            j+=1
        elif flag==1:
            list3.append(string[k])
            flag=0
            k+=1
    if check==0:
        for i in list2:
            if i not in list3:
                list3.append(i)
    elif check==1:
        for i in list1:
            if i not in list3:
                list3.append(i)
    
    merged_queue=q.Queue(len(list3))
    for item in list3:
        merged_queue.enqueue(item)
    return merged_queue

queue1=q.Queue(3)
queue2=q.Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

q.merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
q.merged_queue.display()




