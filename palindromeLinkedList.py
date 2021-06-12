# https://leetcode.com/problems/palindrome-linked-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def isPalindrome(self, head):
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev



        
