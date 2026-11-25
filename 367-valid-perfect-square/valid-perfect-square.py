class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low=0
        high=num
        while low<=high:
            mid=low+(high-low)//2
            ans=mid *mid
            if ans==num and ans.is_integer():
                return True
            elif ans>num:
                high=mid-1
            else:
                low=mid+1
        return False