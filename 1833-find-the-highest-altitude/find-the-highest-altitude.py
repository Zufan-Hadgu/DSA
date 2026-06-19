class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = [0] * (len(gain) + 1)
   
        for i in range(len(gain)):
            a = gain[i] + output[i]
            output[i+1] = a
        return max(output)

        