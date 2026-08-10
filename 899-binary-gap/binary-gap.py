class Solution:
    def binaryGap(self, n: int) -> int:
        Binary = bin(n)
        m = Binary[2:]
        prev = -1
        output = 0
        for i , bit in enumerate(m):
            if bit == "1":
                if prev != -1:
                    output = max(output,i-prev)
                prev = i
        return output 
                
            



