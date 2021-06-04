class MinStack(object):
    def __init__(self):
        self.stack= []

    def push(self, x):
        if not self.stack:
            return self.stack.append((x,x)) 
        else:
        return self.stack.append((x,min(x,self.stack[-1][1])))

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else: 
            return None