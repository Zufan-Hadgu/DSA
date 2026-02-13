class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = 0
        digit_sum = 0
        for  i in range (len(nums)):
            element_sum += nums[i]
            num = nums[i]
            while  num > 0:
                digit = num % 10
                num = num // 10
                digit_sum += digit
            
        return abs(element_sum - digit_sum)
