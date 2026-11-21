class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        right=0
        window_sum=0
        minsum=float('inf')
        n=len(nums)
        for right in range(0,n):
            window_sum+=nums[right]
            while window_sum>=target:
                minsum=min(minsum,right-left+1)
                window_sum-=nums[left]
                left+=1
        if minsum==float('inf'):
            return 0
        else:
            return minsum
        