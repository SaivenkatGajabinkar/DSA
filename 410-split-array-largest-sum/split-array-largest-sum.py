class Solution:
    def solve(self,nums,capacity):
        load=0
        splits=1
        for i in range(len(nums)):
            if load+nums[i]>capacity:
                splits+=1
                load=nums[i]
            else:
                load+=nums[i]
        return splits
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        mini=high
        while low <=high:
            capacity=(low+high)//2
            ans=self.solve(nums,capacity)
            if ans<=k:
                mini=min(mini,capacity)
                high=capacity-1
            else:
                low=capacity+1
        return mini