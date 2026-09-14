class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = n
        ans = 0
        for i in range(1,n + 1):
            total = total - i
            if total >= 0:
                ans += 1
            else:
                break
        return ans
    


        