
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        li = sorted(nums, key=lambda x: (sum(int(c) for c in str(x)), x))

        pos = {num: i for i, num in enumerate(nums)}
        count = 0

        for i in range(len(nums)):
            if nums[i] != li[i]:
                j = pos[li[i]]

                pos[nums[i]] = j
                pos[li[i]] = i

                nums[i], nums[j] = nums[j], nums[i]
                count += 1

        return count
