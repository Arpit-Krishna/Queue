class MyQueue:

    def __init__(self):
        self.queue=[]
        self.front,self.rear=-1,-1

    def push(self, x: int) -> None:
        if self.front==-1:
            self.front=0
        self.rear+=1
        if self.rear>=len(self.queue):
            self.queue.append(0)
        self.queue[self.rear]=x

    def pop(self) -> int:
        if self.empty():
            return -1
        ans=self.queue[self.front]
        self.front+=1
        if self.front==len(self.queue):
            self.front,self.rear=-1,-1
        return ans

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.queue[self.front]

    def empty(self) -> bool:
        if self.front==-1 and self.rear==-1:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()