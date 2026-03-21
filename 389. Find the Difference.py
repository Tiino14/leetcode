class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        for char in t:
            idx = ord(char) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return char
                
        return ""