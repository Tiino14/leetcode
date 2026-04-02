# LeetCode 2469. Convert the Temperature
# Difficulty: Easy
# Topic: Math

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
