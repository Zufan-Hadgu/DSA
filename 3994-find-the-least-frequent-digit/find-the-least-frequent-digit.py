class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        m = str(n)
        freq  = Counter(m)
        less = float("inf")
        valu = float("inf")
        for key,val in freq.items():
            if val < less:
                less = min(val,less)
                valu = int(key)
            elif val == less:
                less = min(val,less)
                valu = min(valu,int(key))

        return valu

            



        