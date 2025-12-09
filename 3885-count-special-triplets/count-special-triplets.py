class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        left = defaultdict(int)
        right = defaultdict(int)

        for num in nums:
            right[num] += 1

        ans = 0

        for mid in nums:
            right[mid] -= 1
            target = 2 * mid
            ans = (ans + left[target] * right[target]) % MOD
            left[mid] += 1

        return ans

