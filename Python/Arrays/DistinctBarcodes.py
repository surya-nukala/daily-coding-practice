class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        freq = {}

        # Count frequency
        for i in barcodes:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        # Create [frequency, barcode]
        a = []
        for key, val in freq.items():
            a.append([val, key])

        # Highest frequency first
        a.sort(reverse=True)

        ans = [0] * len(barcodes)

        index = 0

        # Fill alternate positions
        for val, key in a:
            for i in range(val):
                if index >= len(barcodes):
                    index = 1

                ans[index] = key
                index += 2

        return ans