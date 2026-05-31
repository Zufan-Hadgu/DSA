class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = k
        j = 2 * k
        r = 0

        output = ""

        while j <= len(s):
            output += s[r:i][::-1]
            output += s[i:j]

            r = j
            i = j + k
            j += 2 * k

        remaining = s[r:]

        if len(remaining) < k:
            output += remaining[::-1]
        else:
            output += remaining[:k][::-1]
            output += remaining[k:]

        return output