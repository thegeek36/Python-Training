class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front= 0
    
    def get_max_size(self):
        return self.__max_size

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

def check_odd_even(numq,evenq,oddq,size):
    while size>0:
        ele = numq.dequeue()
        if ele%2 == 0:
            evenq.enqueue(ele)
        else:
            oddq.enqueue(ele)
        size -= 1

q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
print("Original Queue")
q.display()
size = q.get_max_size()
evenq = Queue(size)
oddq = Queue(size)
check_odd_even(q,evenq,oddq,size)
print("Even Queue")
evenq.display()
print("odd Queue")
oddq.display()