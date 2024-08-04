class MinStack:

    def __init__(self):
        self.arr=[]
        self.min=[]
        self.length=0

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.length+=1
        if self.min:
            self.min.append(min(self.min[-1],val))
        else:
            self.min.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.min.pop()

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()