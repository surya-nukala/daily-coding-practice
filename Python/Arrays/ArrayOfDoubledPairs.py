class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        d = {}

        for num in arr:
            d[num] = d.get(num, 0) + 1

        arr.sort(key=abs)

        for num in arr:
            if d[num] == 0:
                continue

            if d.get(2 * num, 0) == 0:
                return False

            d[num] -= 1
            d[2 * num] -= 1

        return True