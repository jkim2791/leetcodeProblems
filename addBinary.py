## https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a, b):
        # edge case
        if len(a)==0:
            return b
        if len(b)==0:
            return a
        # carry over 1 when 1 + 1
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        
        #case of (a=0, b=1) or (a=1, b=0)
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'



