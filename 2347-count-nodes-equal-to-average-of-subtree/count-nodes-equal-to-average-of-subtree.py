# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root is None:
            return (0,0)
        leftsum,left_count=self.solve(root.left)
        right_sum,right_count=self.solve(root.right)
        current_sum=leftsum+right_sum+root.val
        subtree_count=left_count+right_count+1
        if current_sum//subtree_count==root.val:
            self.count+=1
        return (current_sum,subtree_count)

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count=0
        self.solve(root)
        return self.count
        