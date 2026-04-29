class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indexes = []
        output = set()
        for i in range(len(nums)):
            if nums[i] == key:
                indexes.append(i)
        for i in range(len(indexes)):
            for j in range(len(nums)):
                if abs(indexes[i] - j) <= k:
                    output.add(j)
        return list(output)




        