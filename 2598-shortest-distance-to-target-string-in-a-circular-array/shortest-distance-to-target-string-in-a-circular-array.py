class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        ans = float('inf')
        n = len(words)
        for i in range(n):
            if words[i] == target:
                diff = abs(startIndex - i)
                ans = min(ans,min(diff,n - diff))
        return ans



      
