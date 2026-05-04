# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        output = []
        def tiltcalc(node):
            if node is None:
                return 0
           
            left = tiltcalc(node.left)
            right =  tiltcalc(node.right)
            tilt = abs(left-right)
            output.append(tilt)
            return right + left + node.val
        tiltcalc(root)

        return sum(output)





        

        