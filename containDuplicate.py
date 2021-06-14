## https://leetcode.com/problems/contains-duplicate/

def containDuplicate(nums):
    setNum = set(nums)
    if len(setNum) != len(nums):
        return False
    else:
        return True
