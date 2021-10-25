class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTree(self, t1:TreeNode, t2:TreeNode) -> TreeNode:
        # return none when both trees have empty nodes
        if not t1 and not t2:
            return None
        # implement values for each tree
        v1 = t1.val if t1 else 0
        v2 = t2.val if t2 else 0
        # add values from t1, t2 when the value is not 0
        root = TreeNode(v1+v2)
        # recursive call for t1 and t2
        root.left = self.mergeTree(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTree(t1.right if t1 else None, t2.right if t2 else None)

        return root        
        