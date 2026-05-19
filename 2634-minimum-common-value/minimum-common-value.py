class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        # common = []
        # if m < n:
        #     for i in range(m):
        #         if nums2[i] in nums1:
        #             common.append(nums2[i])
        # else:
        #     for i in range(n):
        #         if nums1[i] in nums2:
        #             common.append(nums1[i])
        # return min(common) if common else -1
        i = 0
        j = 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
            