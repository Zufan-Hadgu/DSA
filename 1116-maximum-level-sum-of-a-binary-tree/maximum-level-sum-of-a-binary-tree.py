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
        max_sum = float("-inf")
        output = [max_sum,0]
        output_level = 0
        while queue:
            each_level = 0
            for i in range (len(queue)):
                node = queue.popleft()
                each_level += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)         
            if max_sum < each_level:
                max_sum = each_level
                output_level = level
            
            output = [max_sum,output_level]
            level += 1
        return output[1]
        

      




        

        