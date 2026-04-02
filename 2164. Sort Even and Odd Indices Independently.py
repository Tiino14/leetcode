# LeetCode 2164. Sort Even and Odd Indices Independently
# Difficulty: Easy
# Topic: Array & Sorting

class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        # Even indices sorted ascending, odd indices sorted descending
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)
        result = []
        i = j = 0
        for k in range(len(nums)):
            if k % 2 == 0:
                result.append(evens[i]); i += 1
            else:
                result.append(odds[j]); j += 1
        return result
