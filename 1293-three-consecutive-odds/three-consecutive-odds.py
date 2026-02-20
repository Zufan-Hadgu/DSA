class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        i = 0  
        j = 0  
        while j < len(arr):
            if arr[j] % 2 == 1:  
                if j - i + 1 == 3: 
                    return True
                j += 1
            else: 
                j += 1
                i = j 
        return False