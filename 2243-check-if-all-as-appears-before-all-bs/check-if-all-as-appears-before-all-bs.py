class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i]=='a':
                continue
            for t in range(i+1,len(s)):
                if s[t]=='a':
                    return False
        return True

        