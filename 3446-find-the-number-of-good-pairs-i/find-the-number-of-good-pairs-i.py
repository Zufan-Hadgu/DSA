class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                a = nums1[i]/(nums2[j]*k)
                if a.is_integer():
                    pairs += 1
        return pairs

