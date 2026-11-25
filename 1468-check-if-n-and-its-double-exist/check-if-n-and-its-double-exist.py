class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        #for i in range(len(arr)):
            #hashmap={}
            #for num in range(i+1,len(arr)):
                #hashmap[num]=hashmap.get(num,0)+1
            #ans=2*arr[i]
            #if ans in hashmap:
                #return True
            #hashmap={}
        #return False
        seen=set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False