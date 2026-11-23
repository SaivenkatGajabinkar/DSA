class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        my_hash={}
        ans=[]
        n=len(nums)
        needed=(n//3)+1
        for num in nums:
            my_hash[num]=my_hash.get(num,0)+1
        for k,v in my_hash.items():
            if v>=needed:
                ans.append(k)
        return ans
            
        