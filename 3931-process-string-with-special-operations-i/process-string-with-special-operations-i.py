class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for i in range (len(s)):
            if s[i].isalpha():
                stack.append(s[i])
            if stack:
                if s[i] == "#":
                    stack = stack * 2
                if s[i] == "*":
                    stack.pop()
                if s[i] == "%":
                    stack = stack[::-1]
        return "".join(stack)
        