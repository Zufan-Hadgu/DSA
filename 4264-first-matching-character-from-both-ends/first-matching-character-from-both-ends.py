class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n:
            if s[i] == s[n - i - 1]:
                return i
            i += 1
        return - 1
        