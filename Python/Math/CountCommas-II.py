class Solution:
    def countCommas(self, n: int) -> int:
        p=1000
        re=0
        while p<=n:
            re+=n-p+1
            p*=1000
        return re