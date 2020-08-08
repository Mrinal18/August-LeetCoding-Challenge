# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        """
        Intuition

        The simplest approach (3 lines in Python) is to build inorder traversal and then find the closest element in a sorted array with built-in function min.


        This approach is simple stupid, and serves to identify the subproblems.

        Algorithm

        Build an inorder traversal array.

        Find the closest to target element in that array.
        """
        
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        
        
        return min(inorder(root), key=lambda x : abs(target-x))
