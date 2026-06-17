class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        occurance = []
        seen = set()


        for key,val in c.items():
            if val in seen:
                return False
            seen.add(val)
        return True


       