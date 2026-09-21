class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            degree = 26 - (ord(s[i]) - ord('a'))
            total += (i + 1) * degree

        return total