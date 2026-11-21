import math
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[1]*n
        leftsum=[1]*(n)
        for i in range(1,len(nums)):
            leftsum[i]=leftsum[i-1]*nums[i-1]
        rightsum=[1]*(n)
        for i in range(len(nums)-2,-1,-1):
            rightsum[i]=rightsum[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i]=leftsum[i]*rightsum[i]
        return ans

             
        