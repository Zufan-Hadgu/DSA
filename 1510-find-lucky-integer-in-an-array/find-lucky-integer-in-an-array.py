class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyBox = Counter(arr)   
        lucky = -1
        for key,val in luckyBox.items():
            if key == val:
                lucky = max(lucky,val)
        return lucky


        