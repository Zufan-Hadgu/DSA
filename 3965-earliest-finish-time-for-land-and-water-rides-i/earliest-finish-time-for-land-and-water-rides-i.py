class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        rides = []
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            land_end = landStartTime[i] + landDuration[i]
            for j in range(m):
             
                water_start = max(land_end,waterStartTime[j])
                water_end = water_start + waterDuration[j]
                rides.append(water_end)
        for i in range(m):
            water_end = waterStartTime[i] + waterDuration[i]
            for j in range(n):
                
                land_start = max(water_end,landStartTime[j])
                land_end = land_start + landDuration[j]
                rides.append(land_end)
        return min(rides)
        
            
