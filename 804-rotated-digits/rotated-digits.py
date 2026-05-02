class Solution:
    def rotatedDigits(self, n: int) -> int:

        rotated = {
            "0":"0",
            "1":"1",
            "2":"5",
            "5":"2",
            "6":"9",
            "8":"8",
            "9":"6"
        }
        output = 0
        for i in range(n+1):
            new_num = str(i)
            rot = ""
            for digit in new_num:
                if digit not in rotated:
                    break
                else:
                    rot += rotated[digit]
            if len(rot) == len(new_num) and rot!= new_num:
                output += 1
        return output
            



            