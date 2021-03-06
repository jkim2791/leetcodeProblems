## https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            # use an iteration 
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    