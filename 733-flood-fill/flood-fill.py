class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        direction = ((1,0),(-1,0),(0,1),(0,-1))
        def valid(i,j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])
        first = image[sr][sc]

        queue = deque(image)
        if first == color:
            return image 

        def dfs(i,j):
            if not valid(i,j) or image[i][j] != first:
                return 
            image[i][j] = color

            for dx,dy in direction:
                new_x = i + dx
                new_y = j + dy
                dfs(new_x,new_y)
           
        dfs(sr,sc)

        return image
                

                



        
        