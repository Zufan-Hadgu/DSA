class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        output = nums
        for i in range(len(nums)-1,-1,-1):
            output.append(nums[i])
        return output
