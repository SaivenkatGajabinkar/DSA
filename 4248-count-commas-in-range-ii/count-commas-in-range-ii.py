class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        start=1000
        totalcommas=0
        while start<=n:
            totalcommas+=n-start+1
            start*=1000
        return totalcommas
        