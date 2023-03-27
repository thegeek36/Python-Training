class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1
    def is_full(self):
        if(self.__top == self.__max_size -1 ):
            return True
        return False
    
    def is_empty(self):
        if(self.__top == -1):
            return True
        return False
    
    def push(self,element):
        if(self.is_full()):
            print("Stack is full")
        else:
            self.__top += 1
            self.__elements[self.__top] = element
    def pop(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return  data
        
    def get_max_size(self):
        return self.__max_size
    
    def get_top(self):
        return self.__elements[self.__top]     
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.__top+1):
                print(self.__elements[i])
            print()

ball_stack = Stack(5)
print("Is it empty ?",ball_stack.is_empty())
ball_stack.push(4)
print("Is it full ?",ball_stack.is_full())
ball_stack.push(3)
ball_stack.push(2)
ball_stack.push(1)
ball_stack.display()
ball_stack.pop()
print("After Pop")
ball_stack.display()
print("The top of the stack is",ball_stack.get_top()) 