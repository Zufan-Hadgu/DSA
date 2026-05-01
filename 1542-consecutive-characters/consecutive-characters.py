class Solution:
    def maxPower(self, s: str) -> int:
        output = float("-inf")
        j = 0
        for i in range(len(s)):
            length = 0
            while j < len(s):
                if  s[j] == s[i]:
                    length += 1
                    j += 1
                    print(j)
                else:
                    break
            j = i
            output = max(length,output)
        return output
        



                
                

        