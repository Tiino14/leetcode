# LeetCode 881. Boats to Save People
# Difficulty: Medium
# Topic: Two Pointers & Greedy

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
