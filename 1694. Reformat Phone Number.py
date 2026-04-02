# LeetCode 1694. Reformat Phone Number
# Difficulty: Easy
# Topic: String

class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = number.replace(" ", "").replace("-", "")
        blocks = []
        i = 0
        while i < len(digits):
            remaining = len(digits) - i
            if remaining > 4:
                blocks.append(digits[i:i+3])
                i += 3
            elif remaining == 4:
                blocks.append(digits[i:i+2])
                blocks.append(digits[i+2:i+4])
                i += 4
            else:
                blocks.append(digits[i:])
                i += remaining
        return "-".join(blocks)
