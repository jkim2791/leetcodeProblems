# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums)-1
        # reverse nums
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        
        # reverse index of 0 to k-1
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
            
        # reverse index of k to len(nums)
        l, r = 0, k-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        

        


        