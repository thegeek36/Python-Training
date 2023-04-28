#Python code to implement 2 stacks in an array or list.
class twostacks:
    def __init__(self,size):
        self.size = size
        self.top1 = -1
        self.top2 = size
        self.arr= [0]*size
    
    def push1(self,data):
        if(self.top2 - self.top1 > 1):
            self.top1 += 1
            self.arr[self.top1] = data
    
    def push2(self,data):
        if(self.top2 - self.top1 > 1):
            self.top2 -= 1
            self.arr[self.top2] =data
    
    def pop1(self):
        if(self.top2 - self.top1 > 1):
            ans = self.arr[self.top1]
            self.top1 -= 1
            return ans
        else:
            return -1
    
    def pop2(self):
        if(self.top2 - self.top1 > 1):
            ans = self.arr[self.top2]
            self.top2 += 1
            return ans
        else:
            return -1

    def print1(self):
        print("Stack 1:")
        for i in range(self.top1,-1,-1):
            print(self.arr[i],end=" ")
    
    
    def print2(self):
        print("Stack 2")
        for i in range(self.top2,self.size):
            print(self.arr[i],end=" ")
        
stack = twostacks(12)

#Pushing into stack 1
stack.push1(11)
stack.push1(12)
stack.push1(13)
stack.push1(14)
#Pushing into stack 2
stack.push2(15)
stack.push2(16)
stack.push2(17)
stack.push2(18)

stack.print1()
print()
stack.print2()
print()

stack.pop1()
stack.pop2()

print("After Poping")

stack.print1()
print()
stack.print2()




