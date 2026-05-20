class Solution:
    def mirrorDistance(self, n: int) -> int:
        rv = str(n)
        print(type(rv))
        new_no = rv[::-1]
        nm = int(new_no)
        return abs(nm-n)
       