# LeetCode 2160. Minimum Sum of Four Digit Number After Splitting Digits
# Difficulty: Easy
# Topic: Math & Greedy

class Solution:
    def minimumSum(self, num: int) -> int:
        # Sort digits; pair smallest with smallest to minimize two 2-digit numbers
        digits = sorted(int(d) for d in str(num))
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
