class Solution:
    def magicalString(self, n: int) -> int:
        starting_str = "122"
        j = 2
        for i in range(2,n):
            if starting_str[i] == "2":
                if starting_str[j] == "2":
                    starting_str += "1"*2
                else:
                    starting_str += "2" * 2
                j += 2
            else:
                if starting_str[j] == "1":
                    starting_str += "2"
                else:
                    starting_str += "1"
                j += 1
        once = starting_str[:n].count("1")
        return once
     

                


        