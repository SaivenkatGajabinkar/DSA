class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        valid_sum=[]
        if k==len(nums):
            return max(nums)
        if k==1:
            candidates=nums
        if k>1:
            candidates=[nums[0],nums[-1]]
        for x in candidates:
            if nums.count(x)==1:
                valid_sum.append(x)
        if valid_sum:
            return max(valid_sum)
        return -1
            
