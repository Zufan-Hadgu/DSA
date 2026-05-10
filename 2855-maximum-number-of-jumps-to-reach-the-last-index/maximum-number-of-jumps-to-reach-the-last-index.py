class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        difference = []
        output = 0
        max_jump = [-1]* len(nums)
        max_jump[0] = 0

        for i in range(len(nums)):
            for j in range(i):
                if -target <= nums[j] - nums[i] <= target:
                    if max_jump[j] != -1:
                        max_jump[i] = max(max_jump[i],max_jump[j] + 1)
        return max_jump[len(nums)-1]

        


        