# https://leetcode.com/problems/maximum-subarray/

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0] 
        curr_sum = 0 
        # e.g. nums = [-2,1,-3,4,-1,2,1,-5,4]
        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            # choose maximum number from positive added nums
            max_sum = max(max_sum, curr_sum)
        return max_sum
