class Solution:
    def largestAltitude(self, nums: list[int]) -> int:
        alt=[0]*(len(nums)+1)
        for i in range(1,len(alt)):
            alt[i]=alt[i-1]+nums[i-1]
        return max(alt)

        