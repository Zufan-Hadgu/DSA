class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        output = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(nums)//2):
            output.append(even[i])
            output.append(odd[i])
        return output
