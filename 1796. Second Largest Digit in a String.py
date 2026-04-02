# LeetCode 1796. Second Largest Digit in a String
# Difficulty: Easy
# Topic: String & Hashing

class Solution:
    def secondHighest(self, s: str) -> int:
        digits = sorted(set(int(c) for c in s if c.isdigit()), reverse=True)
        return digits[1] if len(digits) >= 2 else -1
