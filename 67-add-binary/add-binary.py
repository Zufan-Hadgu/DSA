class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        output = ""
        carry = 0
        while i >= 0 or j >= 0:
            summ = 0
            
            if i >= 0 and a[i]:
                summ += int(a[i])
            if j >= 0 and  b[j]:
                summ += int(b[j])
            print(summ)
            summ += carry
            digit = summ % 2
            carry = summ // 2
            output += (str(digit) )
            i -= 1
            j -= 1
        if carry:
            output += (str(carry))
        return output[::-1]
            
    
