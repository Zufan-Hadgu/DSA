class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstWordSum = ""
        secondWordSum = ""
        targetWordSum = ""

        for letter in firstWord:
            a = abs(ord(letter)-ord("a"))
            firstWordSum += str(a)
        for letter in secondWord:
            b = abs(ord(letter) - ord("a"))
            secondWordSum += str(b)
        for letter in targetWord:
            c = abs(ord(letter)-ord("a"))
            targetWordSum += str(c)
        
        targetWordSumF = int(firstWordSum) + int(secondWordSum)
        return targetWordSumF == int(targetWordSum)
        
        
        

        