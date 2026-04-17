class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        Holder = {}
        ans = float("inf")

        for i in range(len(nums)):
            if nums[i] in Holder:
                ans = min(ans, i - Holder[nums[i]])
            rev = int(str(nums[i])[::-1])
            Holder[rev] = i

        return -1 if ans == float("inf") else ans