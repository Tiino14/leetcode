# LeetCode 1556. Thousand Separator
# Difficulty: Easy
# Topic: String

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return f"{n:,}".replace(",", ".")
