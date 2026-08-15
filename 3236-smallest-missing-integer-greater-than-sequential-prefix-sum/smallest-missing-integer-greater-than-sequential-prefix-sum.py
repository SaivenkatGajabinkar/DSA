class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Find smallest missing integer greater than total
        ans = total

        while ans in nums:
            ans += 1

        return ans