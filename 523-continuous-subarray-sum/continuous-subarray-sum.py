class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder_dict = {0:-1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            r = total % k
            if r not in reminder_dict:
                reminder_dict[r] = i
            elif i - reminder_dict[r] > 1:
                return True
        return False

        
            
        