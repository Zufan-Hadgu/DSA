class Solution:
    def countKeyChanges(self, s: str) -> int:
        b = s.lower()
        i = 0
        j= 1
        ans = 0
        while j < len(s):
            if b[i] != b[j]:
                ans += 1
            i += 1
            j += 1
        return ans
        


        