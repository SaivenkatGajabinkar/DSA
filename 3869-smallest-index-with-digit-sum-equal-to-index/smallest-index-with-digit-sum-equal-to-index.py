class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            ch=str(nums[i])
            sumi=0
            for c in ch:
                sumi+=int(c) 
            if sumi==i:
                return i
        return -1
            
        