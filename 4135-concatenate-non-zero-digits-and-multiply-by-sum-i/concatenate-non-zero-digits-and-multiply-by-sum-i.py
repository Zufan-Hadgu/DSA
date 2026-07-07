class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = str(n)
        added = 0
        x = ""
        if n == 0:
            return 0
        for digit in num:
            added += int(digit)
            if digit != "0":
                x += digit
        return int(x) * added
        


        