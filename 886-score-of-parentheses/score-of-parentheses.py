class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        a=0
        b=0
        for i in range(len(s)):
            if s[i]=='(':
                a+=1
            else:
                a -= 1
                if s[i-1] == '(':
                    b += 1 << a
        return b
        