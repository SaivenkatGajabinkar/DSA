class Solution:
    def solve(self,bloomDay,mid,m,k):
        cnt=0
        no_of_days=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=mid:
                cnt+=1
            else:
                no_of_days+=(cnt//k)
                cnt=0
        no_of_days += cnt // k
        if no_of_days>=m:
            return True
        else:
            return False
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if n< m*k:
            return -1
        low=min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid= (low+high) // 2
            if self.solve(bloomDay, mid, m, k):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        