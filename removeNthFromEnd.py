# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:ListNode, n:int) ->ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # set the right pointer corresponding with n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # move two pointers together
        while right:
            left = left.next
            right = right.next

        # remove(skip) Nth element 
        left.next = left.next.next
        return dummy.next