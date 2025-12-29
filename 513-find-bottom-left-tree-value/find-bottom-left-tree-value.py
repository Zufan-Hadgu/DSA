from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def bfs(root):
            if not root:
                return None
            
            queue = deque([root])
            
            while queue:
                level_size = len(queue)
                leftnode = queue[0]   
                
                for _ in range(level_size):
                    node = queue.popleft()
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                if not queue:
                    return leftnode.val    

        return bfs(root)
