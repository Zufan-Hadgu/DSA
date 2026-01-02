class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = len(nums)
        n = m//2
        num_dict = Counter(nums)
        for key,val in num_dict.items():
            if val == n:
                return key
