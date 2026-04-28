class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # output = set()
        # for i in range(len(nums1)):
        #     if nums1[i] in nums2 or nums1[i] in nums3:
        #         output.add(nums1[i])
        # for j in range(len(nums2)):
        #     if nums2[j] in nums3 or nums2[j] in nums1:
        #         output.add(nums2[j])
        # for k in range(len(nums3)):
        #     if nums3[k] in nums2 or nums3[k] in nums1:
        #         output.add(nums3[k])
        # return list(output)

        new_num1,new_num2,new_num3 = set(nums1),set(nums2),set(nums3)
        output = []

        for num in new_num1 | new_num2 | new_num3:
            count = (num in new_num1) + (num in new_num2)  + (num in new_num3)
            if count >= 2:
                output.append(num)
        return output
    
            

