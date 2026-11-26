import math
class Solution:
    def solve(self,arr,mid,h):
        sumi=0
        for i in range(len(arr)):
            sumi+=math.ceil(arr[i]/mid)
        return sumi
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            a=self.solve(piles,mid,h)
            if a<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
