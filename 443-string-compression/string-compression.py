class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        i = 0
        j = 1
        k = 0

        if len(chars) == 1:
            return 1  
        while i < len(chars):
            count = 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
                count += 1
            chars[k] = chars[i]
            k += 1
            if count > 1:
                for digits in str(count):
                    chars[k] = digits
                    k += 1
            i += count 
            j = i + 1
        return k
     
         
        
            
            
        