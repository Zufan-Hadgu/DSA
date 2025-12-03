class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_sets = [set(word) for word in words]

        def checker(set1, set2):
            return set1.isdisjoint(set2)  
        
        output = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):   
                if checker(word_sets[i], word_sets[j]):
                    result = len(words[i]) * len(words[j])
                    output = max(output, result)

        return output
