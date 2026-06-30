class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letters = defaultdict(int)
        output = 0
        i = 0
        j = 0

        while j < len(s):
            letters[s[j]] += 1
            j += 1
            while len(letters) == 3:
                output += len(s) - j + 1
                letters[s[i]] -= 1
                if letters[s[i]] == 0:
                    del letters[s[i]]
                i += 1

        return output
            
            
                






        