class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))
        l=min(min_index,max_index)
        r=max(min_index,max_index)
        front=r+1
        back=len(nums)-l
        frontBack=(l+1)+(len(nums)-r)
        return min(front,back,frontBack)
