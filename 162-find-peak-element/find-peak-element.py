class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num2 = sorted(nums)
        return (nums.index(num2[-1]))

        