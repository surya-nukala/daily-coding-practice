class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        su=[0]*n
        mn=float('inf')
        for i in range(n-1,-1,-1):
            mn=min(mn,nums[i])
            su[i]=mn
        mx=0
        for i in range(n):
            mx=max(nums[i],mx)
            score=mx-su[i]
            if score<=k:
                return i
        return -1