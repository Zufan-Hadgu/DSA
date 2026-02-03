class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        indexes = []
        new_arr  = []

        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                new_arr.append(0)
            elif nums[i + 1] == nums[i]:
                return False
            else:
                new_arr.append(1)
        count = 0     
        if new_arr[0] != 0:
            return False
        for i in range(len(new_arr) - 1):
            if new_arr[i] == 0 and new_arr[i+1] != 0:
                count += 1
            elif new_arr[i] == 1 and new_arr[i+1] != 1:
                count += 1
        count += 1
        if count == 3:
            return True
        else:
            return False


        
       
        