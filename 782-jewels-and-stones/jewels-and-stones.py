class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for letter in stones:
            if letter in jewels:
                output += 1
        return output

        