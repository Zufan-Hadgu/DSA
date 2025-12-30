class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        output = []

        for mat in matrix:
            output.extend(mat)
        output.sort()
        return output[k-1]
   

        