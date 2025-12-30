class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # output = []
        # for mat in matrix:
        #     output.extend(mat)
        # output.sort()
        # return output[k-1]
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[n-1][n-1]
        def count(mid):
            count = 0
            col = n - 1

            for row in range(n):
                while col >= 0 and matrix[row][col] > mid:
                    col -= 1
                count += (col + 1)
            return count

        while left < right:
            mid = (left + right)//2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
                