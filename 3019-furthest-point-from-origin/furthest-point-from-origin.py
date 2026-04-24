class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = 0
        l = 0
        d = 0
        for letter in moves:
            if letter == "R":
                r += 1
            elif letter == "L":
                l += 1
            else:
                d += 1
        maxi = max(r,l)
        mini = min(r,l)
        output = d + maxi - mini
        return output
