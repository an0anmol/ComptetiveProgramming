class Solution:
    def are_strings_similar(self,s1, s2):
        char_count = [0] * 256  # Assuming ASCII characters
        for char in s1:
            char_count[ord(char)] = 1
        for char in s2:
            if char_count[ord(char)] != 1:
                return False
        for char in s2:
            char_count[ord(char)] = 0
        for char in char_count:   
            if char != 0:
                return False      
        return True
    def similarPairs(self, strs: List[str]) -> int:
        n = len(strs)
        similar_pairs = 0
        for i in range(n):
            for j in range(i+1, n):
                if self.are_strings_similar(strs[i], strs[j]):
                    similar_pairs +=1
        return similar_pairs
