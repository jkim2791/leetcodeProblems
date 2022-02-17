# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, left, right):
            # base case
            if not node:
                return True

            # base condition
            if not (node.val < right and node.val > left):
                return False

            # recursion
            return (validBST(node.left, left, node.val) and  # left
                    validBST(node.right, node.val, right))  # right

        return validBST(root, float("-inf"), float("inf"))

