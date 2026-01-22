class Solution:
    def replaceDigits(self, s: str) -> str:
        output = ""
        for i in range(len(s)):
            if i % 2 != 0:
                letter = ord(s[i-1])
                letter += int(s[i])
                output += chr(letter)
            else:
                output += s[i]
        return output


        