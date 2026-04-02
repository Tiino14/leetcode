# LeetCode 1436. Destination City
# Difficulty: Easy
# Topic: Array & Hashing

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        # Destination city has no outgoing path
        sources = {p[0] for p in paths}
        for _, dst in paths:
            if dst not in sources:
                return dst
