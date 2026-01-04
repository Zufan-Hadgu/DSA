class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        output = 0     
        for num in nums:
            divisors = set()
            for i in range(1,int(math.sqrt(num))+ 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num//i)
            if len(divisors) == 4:
                output += sum(divisors)
           
        return output
    
