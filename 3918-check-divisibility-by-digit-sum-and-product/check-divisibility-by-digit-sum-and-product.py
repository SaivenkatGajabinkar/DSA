class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi=0
        prod=1
        strr=str(n)
        for ch in strr:
            sumi+=int(ch)
            prod*=int(ch)
        total=sumi+prod
        if n%total==0:
            return True
        return False
            

        