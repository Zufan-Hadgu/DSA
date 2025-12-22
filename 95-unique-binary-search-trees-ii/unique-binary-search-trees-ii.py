# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def dp(i,j):
            if i > j:
                return [None]
            if (i,j) in memo:
                return memo[(i,j)]
            output = []
            for val in range(i,j + 1):
                for lefttree in  dp(i,val - 1):
                    for righttree in dp(val + 1, j):
                        root = TreeNode(val,lefttree,righttree)
                        output.append(root)
            memo[(i,j)] = output
            return output
        return dp(1,n)
            

            


            
                

        

        