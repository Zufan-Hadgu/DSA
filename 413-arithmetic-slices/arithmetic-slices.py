class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        output = 0
        curr = 0
        if len(nums) < 3:
            return 0

        for i in range(2,len(nums)):
            if nums[i] - nums[i - 1] == nums[i-1] - nums[i-2]:
                curr += 1
                output += curr
            else:
                curr = 0
        return output



        