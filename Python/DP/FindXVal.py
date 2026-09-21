class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only num
            new_dp[num % k] += 1

            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * num) % k
                    new_dp[new_r] += dp[r]

            dp = new_dp

            # Add counts to final answer
            for r in range(k):
                ans[r] += dp[r]

        return ans