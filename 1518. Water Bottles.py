# LeetCode 1518. Water Bottles
# Difficulty: Easy
# Topic: Math & Simulation

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            new = empty // numExchange
            total += new
            empty = empty % numExchange + new
        return total
