class Solution:
    def minimumFlips(self, n: int) -> int:
        a = bin(n)
        b = str(a)[2:]
        c = b[::-1]
        count = 0
        for i in range(len(c)):
            if c[i] != b[i]:
               count += 1
        return count


  
        