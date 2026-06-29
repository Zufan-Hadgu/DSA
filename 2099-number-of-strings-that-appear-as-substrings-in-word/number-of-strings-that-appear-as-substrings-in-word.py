class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        num = 0
        for letters in patterns:
            if letters in word:
                num += 1
        return num

        