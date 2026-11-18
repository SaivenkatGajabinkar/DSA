class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        arr = []

        for k in range(l, r + 1):
            sumi = sum(nums[:k])

            if sumi > 0:
                arr.append(sumi)

            for i in range(k, len(nums)):
                sumi += nums[i] - nums[i-k]

                if sumi > 0:
                    arr.append(sumi)

        if not arr:
            return -1

        return min(arr)