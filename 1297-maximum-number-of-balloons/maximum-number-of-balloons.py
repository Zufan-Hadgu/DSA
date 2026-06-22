class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       c = Counter(text)
       return min(
            c["b"], 
            c["a"], 
            c["n"], 
            c["l"] // 2, 
            c["o"] // 2
        )


        

     

            

                

        
        