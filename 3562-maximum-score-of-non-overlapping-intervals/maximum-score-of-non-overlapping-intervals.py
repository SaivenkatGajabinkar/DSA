class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        from bisect import bisect_right
        from functools import lru_cache

        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        @lru_cache(None)
        def solve(i, count):

            if i == n or count == 4:
                return (0, ())

            # Skip
            skip_score, skip_indices = solve(i + 1, count)

            # Take
            l, r, w, original_index = arr[i]

            next_i = bisect_right(starts, r)

            take_score, take_indices = solve(next_i, count + 1)

            take_score += w

            take_indices = tuple(sorted(
                (original_index,) + take_indices
            ))

            # Compare scores
            if take_score > skip_score:
                return (take_score, take_indices)

            if skip_score > take_score:
                return (skip_score, skip_indices)

            # Same score -> lexicographically smaller
            return (skip_score, min(skip_indices, take_indices))

        return list(solve(0, 0)[1])