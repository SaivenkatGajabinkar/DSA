class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen = len(words[0])
        totalwords = len(words)
        total = wordlen * totalwords
        ans = []
        for i in range(len(s) - total + 1):
            part = s[i:i + total]
            current = []
            for j in range(0, total, wordlen):
                current.append(part[j:j + wordlen])
            if sorted(current) == sorted(words):
                ans.append(i)
        return ans