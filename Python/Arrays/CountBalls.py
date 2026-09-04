class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        a = [0] * 46

        for i in range(lowLimit, highLimit + 1):
            num = i
            sm = 0

            while num > 0:
                sm += num % 10
                num //= 10

            a[sm] += 1

        return max(a)