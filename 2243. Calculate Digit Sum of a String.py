# LeetCode 2243. Calculate Digit Sum of a String
# Difficulty: Easy
# Topic: String & Simulation

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                chunk = s[i:i+k]
                new_s += str(sum(int(c) for c in chunk))
            s = new_s
        return s
