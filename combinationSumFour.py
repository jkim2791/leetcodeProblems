# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for allcomb in range(1, target + 1):
            dp[allcomb] = 0
            for n in nums:
                dp[allcomb] += dp.get(allcomb - n, 0)
        return dp[target]
