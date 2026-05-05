from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiou")
        
        # 1. Calculate frequency of all characters
        counts = Counter(s)
        
        # 2. Record the first occurrence index of each character
        first_occurrence = {}
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
        
        # 3. Extract vowels and their original positions
        vowels_in_s = []
        vowel_indices = []
        for i, char in enumerate(s):
            if char in vowels_set:
                vowels_in_s.append(char)
                vowel_indices.append(i)
        
        # 4. Sort the extracted vowels based on the rules:
        # Rule 1: Frequency (non-increasing -> -counts[x])
        # Rule 2: First occurrence (increasing -> first_occurrence[x])
        vowels_in_s.sort(key=lambda x: (-counts[x], first_occurrence[x]))
        
        # 5. Reconstruct the string
        s_list = list(s)
        for i, idx in enumerate(vowel_indices):
            s_list[idx] = vowels_in_s[i]
            
        return "".join(s_list)