# LeetCode 2210. Count Hills and Valleys in an Array
# Difficulty: Easy
# Topic: Array

class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        # Remove consecutive duplicates first
        deduped = [nums[0]]
        for n in nums[1:]:
            if n != deduped[-1]:
                deduped.append(n)

        count = 0
        for i in range(1, len(deduped) - 1):
            if deduped[i] > deduped[i-1] and deduped[i] > deduped[i+1]:
                count += 1  # hill
            elif deduped[i] < deduped[i-1] and deduped[i] < deduped[i+1]:
                count += 1  # valley
        return count
