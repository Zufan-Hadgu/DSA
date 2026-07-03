from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c = Counter(nums)
        freq = -1
        output = -1  
        
        for key, val in c.items():
            if key % 2 == 0:
                if val > freq:
                    freq = val
                    output = key
                elif val == freq:
                    output = min(output, key)
                    
        return output