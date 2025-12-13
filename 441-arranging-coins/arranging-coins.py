class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = n
        output = 0
        for i in range(1,n + 1):
            total = total - i
            if total >= 0:
                output += 1
            else:
                break
        return output
    


        