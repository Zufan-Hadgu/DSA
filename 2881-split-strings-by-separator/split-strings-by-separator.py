class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for part in words:
            parts = part.split(separator)
            for p in parts:
                if p:
                    output.append(p)
        return output

      