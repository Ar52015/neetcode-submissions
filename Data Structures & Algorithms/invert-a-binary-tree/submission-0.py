# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(node):
    if (node.right != None or node.left != None):
        node.left, node.right = node.right, node.left

    if (node.left != None): invert(node.left)
    if (node.right != None): invert(node.right)
    
    return node

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if (root == None):
            return root

        invert(root)
        return root
        