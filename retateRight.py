class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head:ListNode, k:int) -> ListNode:
        if not head:
            return head
        
        # get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # case for k which is greater than length
        k = k % length

        if k == 0:
            return head
        # move th the pivot and rotate
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead
        