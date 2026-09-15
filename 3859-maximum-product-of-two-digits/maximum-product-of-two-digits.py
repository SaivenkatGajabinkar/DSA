class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        ans=0
        if len(digits)<=1:
            return digits
        else:
            digits.sort()
            ans=digits[-1]*digits[-2]
        return ans

        