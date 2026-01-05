class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negative = []
        summation = 0
        list_matrix = []
        for row in range(n):
            for col in range(n):
                if matrix[row][col] <= 0:
                    summation -= matrix[row][col]

                    negative.append(matrix[row][col])
                else:
                    list_matrix.append(matrix[row][col])
                    summation += matrix[row][col]

        negative.sort()
        a = min(list_matrix) if list_matrix else float('inf')

        if len(negative) % 2 == 0:
            return summation

        smallest_neg_abs = abs(negative[-1])     
        smallest_pos = min(list_matrix) if list_matrix else float('inf')

        smallest = min(smallest_neg_abs, smallest_pos)

        return summation - 2 * smallest



       