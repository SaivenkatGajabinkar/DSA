class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        min_idx=0
        max_ind=0
        for i in range(len(nums)):
            if nums[i]==mini:
                min_idx=i
            if nums[i]==maxi:
                max_idx=i
        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx
        n = len(nums)
        ans1 = max_idx + 1
        ans2 = n - min_idx
        ans3 = (min_idx + 1) + (n - max_idx)
        return min(ans1, ans2, ans3)