from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = Counter(magazine)
        
        for char in ransomNote:
            if count_mag[char] > 0:
                count_mag[char] -= 1
            else:
                return False
                
        return True