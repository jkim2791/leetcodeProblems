# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Collection, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root:TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])
        while q:
            rSide = None
            qLength = len(q)

            for i in range(qLength):
                node = q.popleft()
                if node:
                    rSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rSide:
                res.append(rSide.val)
        return res
