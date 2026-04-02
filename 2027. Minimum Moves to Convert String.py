# LeetCode 2027. Minimum Moves to Convert String
# Difficulty: Easy
# Topic: Greedy

class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        i = 0
        while i < len(s):
            if s[i] == 'X':
                moves += 1
                i += 3  # one operation covers 3 positions
            else:
                i += 1
        return moves
