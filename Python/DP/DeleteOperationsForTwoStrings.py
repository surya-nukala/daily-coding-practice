class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    cur[j] = 1 + prev[j - 1]
                else:
                    cur[j] = max(prev[j], cur[j - 1])

            prev = cur[:]

        lcs = prev[m]

        return (n - lcs) + (m - lcs)