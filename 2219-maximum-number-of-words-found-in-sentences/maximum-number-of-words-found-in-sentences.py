class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        for sente in sentences:
            a = sente.split(" ")
            output = max(output,len(a))
        return output