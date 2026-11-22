class Solution:
    def ncr(self,r):
        temp=[1]
        ans=1
        for i in range(1,r):
            ans=ans*(r-i)
            ans=ans//i
            temp.append(ans)
        return temp

    def generate(self, r: int) -> list[list[int]]:
        ans=[]
        for i in range(1,r+1):
            ans.append(self.ncr(i))
        return ans


        