class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        k=sum(nums)-x
        if k<0:
            return -1
        bb=-1
        s=i=0
        for p,num in enumerate(nums):
            s+=num
            while s>k:
                s-=nums[i]
                i+=1
            if s==k:
                bb=max(bb,p-i+1)
        return -1 if bb<0 else len(nums)-bb
