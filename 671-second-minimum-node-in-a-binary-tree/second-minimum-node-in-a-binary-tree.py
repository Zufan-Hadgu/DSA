# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        output = []
        def mini(node):
            if not node:
                return None
            output.append(node.val)
            if node.left:
                mini(node.left)
            if node.right:
                mini(node.right)
            return output
        x = mini(root)
        y = list(set(x))
        y.sort()
        return y[1] if len(y) >= 2 else -1
                
            
      


        