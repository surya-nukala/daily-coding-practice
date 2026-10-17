from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            curr=num
            d_s=0
            while curr:
                d_s+=curr%10
                curr//=10
            nums[i]=(d_s,num,i)
        nums.sort()
        nums=[num[2] for num in nums]
        n=len(nums)
        visited=[False]*n
        cy=0
        for i,num in enumerate(nums):
            if visited[i]:
                continue
            cy+=1
            j=i
            while not visited[j]:
                visited[j]=True
                j=nums[j]
        print(n,cy)
        return n-cy