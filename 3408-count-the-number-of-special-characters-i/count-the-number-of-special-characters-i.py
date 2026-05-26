class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = set(word)
        output = 0
        for char in c:
            if (char.islower()) and (char.upper() in c):
                output += 1
        return output

    
                


         


        