# LeetCode 1304. Find N Unique Integers Sum up to Zero
# Difficulty: Easy
# Topic: Array & Hashing

class Solution:
    def sumZero(self, n: int) -> list[int]:
        # Use 1, 2, ..., n-1 and negate their sum as the last element
        result = list(range(1, n))
        result.append(-sum(result))
        return result
