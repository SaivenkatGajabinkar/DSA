from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        per=list(set(permutations(digits,3)))
        even=[0,2,4,6,8]
        count=0
        for p in per:
            if p[2] in even and p[0]!=0:
                count+=1
        return count
       
        