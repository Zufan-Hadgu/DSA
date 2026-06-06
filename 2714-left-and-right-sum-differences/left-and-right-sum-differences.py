class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
      

        for i in range(1,len(nums)):
            left_sum[i] = nums[i-1] + left_sum[i-1]
        for i in range(len(nums) - 2,-1,-1):
            right_sum[i] = nums[i+1] + right_sum[i+1]

        i = 0
        output = [0] * len(nums)

        while i < len(nums):
            output[i] = abs(left_sum[i] - right_sum[i])
            i += 1
        return output
        


        print(right_sum)


        
        print(left_sum)

        