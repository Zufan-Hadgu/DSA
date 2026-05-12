class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)[2:]
        output = 0
        power = len(a) - 1
        for i in range(len(a)):
            if a[i] == "0":
                output += 2**power
            power -= 1
        return output



   
        