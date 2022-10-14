from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generate(self, nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if (start == end):
            return None
        if (start + 1 >= end):
            return TreeNode(nums[start])
        
        rootIdx = start + (end - start) // 2
        left = self.generate(nums, start, rootIdx)
        right = self.generate(nums, rootIdx + 1, end)
        return TreeNode(nums[rootIdx], left, right)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.generate(nums, 0, len(nums))