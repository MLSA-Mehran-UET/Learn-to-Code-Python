#Implementation of Stack
class Stack:
    def __init__(self):
        self.top = 0
        self.data = []
    def push(self,obj):
        self.data.append(obj)
        self.top = self.top+1
    def pop(self):
        if (self.top > 0):
            Top = self.data[self.top-1]
            self.data.remove(self.data[self.top-1])
            self.top = self.top - 1
            return Top
        else:
            print("Stack is empty")
            return 0