class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result=''
        s = s.replace("-", "").upper()
        for i in range(0,len(s)):
            result+=s[i] 
            if (len(s) - i - 1) % k == 0 and i != len(s) - 1:
                    result += '-'       
        return result
        