class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_element = max(nums)
        c = Counter(nums)
        duplicate = 0
        for key,val in c.items():
            if val >= 2:
                duplicate += 1
        
            
        if len(nums) == max_element + 1 and duplicate == 1 and  c[max_element] == 2:
                return True
        return False
       