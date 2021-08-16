# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        res = [1] *(len(nums))
        # cumulative product inorder, start with 1
        pre_num = 1
        for i in range(len(nums)):
            res[i] = pre_num
            pre_num *= nums[i]
        # cumulative product postorder, start with 1
        post_num = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post_num
            post_num *= nums[i]
        return res

