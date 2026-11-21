class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myhash={}
        myhash={0:1}
        cnt=0
        prefixsum=0
        for right in range(len(nums)):
            prefixsum+=nums[right]
            target=prefixsum-k
            if target in myhash:
                cnt+=myhash[target]
            myhash[prefixsum]=myhash.get(prefixsum,0)+1
        return cnt


        