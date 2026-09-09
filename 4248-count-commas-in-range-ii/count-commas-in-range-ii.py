class Solution:
    def countCommas(self, n: int) -> int:
        starting = 1000
        answer = 0

        while starting <= n:
            answer += n - starting + 1
            starting *= 1000
        return answer