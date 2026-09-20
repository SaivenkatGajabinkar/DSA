class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        total=0
        for i in range(len(s)):
            ans=ord('z')-ord(s[i])+1
            total+=ans*(i+1)

        return total
        