class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s:
            return ""

        output = s[0]
        same = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                same += 1
            else:
                same = 1

            if same <= 2:
                output += s[i]

        return output

        