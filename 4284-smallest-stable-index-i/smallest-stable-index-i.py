class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if not nums:
            return -1
        for i in range(0,len(nums)):
            maxi=max(nums[:i+1])
            mini=min(nums[i:])
            score=maxi-mini
            if score<=k:
                return i
        return -1

        