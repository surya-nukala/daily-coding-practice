class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c = []

        for sentence in sentences:
            c.append(len(sentence.split()))

        return max(c)