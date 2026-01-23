class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors = min(a,b)
        output = 0
        for i in range(1,factors + 1):
            if a  % i == 0 and b % i == 0:
                output += 1
        return output
        