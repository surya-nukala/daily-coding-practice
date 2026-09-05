class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        r = "".join(map(str,nums))
        return r.count(str(digit))