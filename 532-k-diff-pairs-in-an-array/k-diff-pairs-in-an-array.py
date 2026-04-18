class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[j] - nums[i]) == k:
                    pairs.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
        
        return len(pairs)