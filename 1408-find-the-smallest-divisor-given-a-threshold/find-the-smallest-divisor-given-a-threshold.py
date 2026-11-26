import math
class Solution:
    def solve(self,nums,mid):
        sumi=0
        for i in range(len(nums)):
            sumi+=math.ceil(nums[i]/mid)
        return sumi
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=high
        while low<=high:
            mid=low+(high-low)//2
            solution=self.solve(nums,mid)
            if solution <= threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        