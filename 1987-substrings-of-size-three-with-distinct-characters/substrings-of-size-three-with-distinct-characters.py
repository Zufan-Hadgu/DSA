class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        a = Counter(s[:3])
        output = 0
        
        if len(a) == 3:
            output += 1
        
        i = 0
        for j in range(3, len(s)):
            a[s[i]] -= 1
            if a[s[i]] == 0:
                del a[s[i]]
            i += 1
        
            a[s[j]] += 1
    
            if len(a) == 3:
                output += 1
        
        return output