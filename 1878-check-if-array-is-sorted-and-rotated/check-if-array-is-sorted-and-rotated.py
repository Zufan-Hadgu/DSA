class Solution:
    def check(self, nums: List[int]) -> bool:
        min_num = min(nums)
       
        for start in range(len(nums)):
            output = []
            i = start

            while len(output) < len(nums):
                output.append(nums[i])
                i += 1
                if i == len(nums):
                    i = 0
            if output == sorted(nums):
                return True
        return False



        # for i in range(nums):

