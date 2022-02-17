# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, j in enumerate(nums):
            sub = target - j
            if sub in hashMap:
                return [hashMap[sub], i]
            hashMap[j] = i
        return