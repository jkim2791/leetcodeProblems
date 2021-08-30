# https://leetcode.com/problems/valid-parentheses/

class Soulution:
    def isValid(self, s:str) -> bool:
        stack = []
        # we use stack so check from last elements
        closeAndOpen =  {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in closeAndOpen:
                # check parenthese is valid (open+close)
                # if then, pop valid parenthese
                if stack and stack[-1] == closeAndOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # return True when all elements are deleted in stack
        return True if not stack else False
