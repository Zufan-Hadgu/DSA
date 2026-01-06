# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        level = 1
        level_dict = []
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level_dict.append([level_sum,level])
        sorted_level = sorted(level_dict,key=lambda row:row[0],reverse=True)

        if len(sorted_level) < k:
            return - 1
            
        return sorted_level[k-1][0]
                

        