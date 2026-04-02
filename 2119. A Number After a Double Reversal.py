# LeetCode 2119. A Number After a Double Reversal
# Difficulty: Easy
# Topic: Math

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Reversing removes trailing zeros; num == 0 or num has no trailing zero
        return num == 0 or num % 10 != 0
