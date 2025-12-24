# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(node):
            if not node:
                return 0       
            node_sum = dfs(node.right) + dfs(node.left) + node.val
            output.append(node_sum)
            return node_sum
        dfs(root)
        d = Counter(output)
        answer = []
        max_count = max(d.values())
        for key,val in d.items():
            if val == max_count:
                answer.append(key)
        return answer
        