from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0

        for i in nums:
            i = str(i)
            n = max(i)
            ans = int(n * len(i))
            total += ans

        return total