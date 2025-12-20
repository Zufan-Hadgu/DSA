# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(node):
            if not node:
                return 
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        d = Counter(arr)
        freq_max = max(d.values(),default = 0)

        
        output = []
        for key,val in d.items():
            if val == freq_max:
                output.append(key)
        return output

            
        