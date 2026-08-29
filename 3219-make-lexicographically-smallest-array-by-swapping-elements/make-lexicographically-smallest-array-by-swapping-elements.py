class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        arr = sorted((nums[i], i) for i in range(len(nums)))

        ans = nums[:]

        start = 0

        for i in range(len(arr) + 1):

            if i == len(arr) or arr[i][0] - arr[i-1][0] > limit:

                group = arr[start:i]

                values = sorted(x[0] for x in group)
                indices = sorted(x[1] for x in group)

                for j in range(len(group)):
                    ans[indices[j]] = values[j]

                start = i

        return ans