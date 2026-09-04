class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for i in t:
            res ^= ord(i)

        for i in s:
            res ^= ord(i)

        return chr(res)