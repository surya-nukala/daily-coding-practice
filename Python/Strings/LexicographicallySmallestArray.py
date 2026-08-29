from typing import List
from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_s = sorted(nums)
        curr = 0
        ntg = {}

        ntg[nums_s[0]] = curr

        gtl = {}
        gtl[curr] = deque([nums_s[0]])

        for i in range(1, len(nums)):
            if abs(nums_s[i] - nums_s[i - 1]) > limit:
                curr += 1

            ntg[nums_s[i]] = curr

            if curr not in gtl:
                gtl[curr] = deque()

            gtl[curr].append(nums_s[i])

        for i in range(len(nums)):
            num = nums[i]
            group = ntg[num]
            nums[i] = gtl[group].popleft()

        return nums