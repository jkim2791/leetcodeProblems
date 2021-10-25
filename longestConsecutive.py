# https://leetcode.com/problems/longest-consecutive-sequence/description/
# runtime limit = O(n)
from typing import List


class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        nums_set  = set(nums)
        longest = 0
        for i in nums:
            # check left value exists
            if (i-1) not in nums_set:
                length = 0
                # if right value(i+1) exists, increment the length
                while (i+length) in nums_set:
                    length += 1
                # update longest consecutive nums
                longest = max(length, longest)
        return longest

