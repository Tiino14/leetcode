# LeetCode 9. Palindrome Number
# Difficulty: Easy
# Topic: Math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
