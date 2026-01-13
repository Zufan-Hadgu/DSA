class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0      
        curr = 1      
        output = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                output += min(prev, curr)
                prev = curr
                curr = 1

        # compare the last two groups
        output += min(prev, curr)

        return output
