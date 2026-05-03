class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        characters = []
        output = []
        for char in s:
            if char.isalpha():
                letters.append(char)
            else:
                characters.append(char)
        letters = letters[::-1]
        characters = characters[::-1]
        i = 0
        j = 0
        for char in s:
            if char.isalpha():
                output.append(letters[i])
                i += 1
            else:
                output.append(characters[j])
                j += 1
        return "".join (output)

        
        