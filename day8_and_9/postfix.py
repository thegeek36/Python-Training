class PostFix:
    def __init__(self,max):
        self.top = -1
        self.max = max
        self.array = []
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[self.top]
    
    def push(self,item):
        self.array.append(item)
        self.top += 1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.top-=1
            return self.array.pop()
    def evalute(self,expr):
        for i in expr:
            if i.isdigit():
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=str(eval(op2 + i + op1))
                self.push(result)
        return int(self.pop())
    
exp = input("Enter the expression (0-9 or +-*/)")
ans = PostFix(len(exp))
print("Answer is",ans.evalute(exp))

    