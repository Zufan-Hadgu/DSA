class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(board)
        m = len(board[0])
        def valid(i,j):
            return 0 <= i < n and 0 <=j < m and board[i][j] != '.'
        def dfs(i,j,count):
            if word[count] != board[i][j]:
                return False
            if count == len(word)-1:
                return True
            temp = board[i][j]
            board[i][j] = '.'
            for x,y in direction:
                    new_x = x + i
                    new_y = y + j
                    if valid(new_x,new_y):
                        if dfs(new_x,new_y,count + 1):
                            board[i][j] = temp
                            return True
            board[i][j] = temp
            return False
        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                  if dfs(i,j,count):
                    return True
        return False
            
            
        