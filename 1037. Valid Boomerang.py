# LeetCode 1037. Valid Boomerang
# Difficulty: Easy
# Topic: Math & Geometry

class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        (x1,y1),(x2,y2),(x3,y3) = points
        # Cross product of vectors (p2-p1) and (p3-p1) must be non-zero
        return (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1)
