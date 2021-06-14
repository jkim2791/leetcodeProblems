'''
# https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        # return the "len(nums)/2"th  elememt from sorted array
        return nums[len(nums)/2]
        