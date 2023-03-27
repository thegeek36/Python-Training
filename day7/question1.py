'''
Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder.
Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.
Example:
Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear) 
Output Queue: 10080, 2520(front-rear) 
'''
class Queue:
 
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front= 0

    def is_full(self):
        if (self.__rear == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__front > self.__rear):
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue Full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size
    
def check_divisible(num_queue):
    size = num_queue.get_max_size()
    ans_queue = Queue(size)
    while size > 0:
        data = num_queue.dequeue()
        cnt = 0
        for i in range(1,11):
            if data % i == 0:
                cnt += 1
            if cnt == 10:
                ans_queue.enqueue(data)
        size -= 1
    return ans_queue
#Main function
num_queue = Queue(5)
num_queue.enqueue(13983)
num_queue.enqueue(10080)
num_queue.enqueue(7113)
num_queue.enqueue(2520)
num_queue.enqueue(2500)

check_divisible(num_queue).display()


        
      
