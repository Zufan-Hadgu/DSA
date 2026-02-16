class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        num = str(num)
        if num[-1] == "0":
            return False
        else:
            return True
        