class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = []
        for sentence in sentences:
            c.append(len(sentence.split()))
        return max(c)\
# Time complexity: O(n*m) where n is the number of sentences and m is the average length of the sentences
# Space complexity: O(n) where n is the number of sentences