# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        node = {}
        for p,c,l in descriptions:
            if p not in node:            
                node[p] = TreeNode(p)
            if c not in node:
                node[c] = TreeNode(c)
            if l:
                node[p].left = node[c]
            else:
                node[p].right = node[c]
            children.add(c)

        for val in node:
            if val not in children:
                return node[val]
        

        