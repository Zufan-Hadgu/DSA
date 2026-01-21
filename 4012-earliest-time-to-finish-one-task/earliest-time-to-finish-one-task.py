class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        output = float('inf')
        for start, finish in tasks:
            earliest = start + finish
            output = min(earliest, output)
        return output

        