class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=k
        while a in nums:
            a+=k
        return a

        