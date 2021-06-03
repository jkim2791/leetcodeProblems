'''
https://leetcode.com/problems/min-stack/
stack = [1, 2, 5, 3, 1, 0]
sorted_stack = [[x, min], [x, min], [x,min], ... , [x, min]]
stack[-1][1] will be the min value of the stack
'''


class MinStack:
    ## initialize stack
    def __init__(self):
        self.stack= []

    def push(self, x):
        if not self.stack:
            ## stack = [[x, x]]
            return self.stack.append((x,x)) 
        else:
            ## compare prev_min with x
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