class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        while j < len(nums) and i < j:
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
            elif nums[i] % 2 == 0 and nums[j] % 2 != 0:
                i += 1
                j += 1
            elif nums[i] % 2 == 0 and nums[j] % 2 == 0:
                i = j + 1
                j = j + 2
            else:
                j += 1
        return nums
            
           
        
            

        