# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        level_dict = []
        while queue:
            each_level = 0
            for i in range (len(queue)):
                node = queue.popleft()
                each_level += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level_dict.append([level,each_level])
            level += 1
        sorted_matrix = sorted(level_dict,key=lambda row:row[1])
        n = len(sorted_matrix)
        max_val = sorted_matrix[n-1][1]
        for level,summed in level_dict:
            if summed == max_val:
                return level


      




        

        