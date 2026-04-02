# LeetCode 3360. Stone Removal Game
# Difficulty: Easy
# Topic: Greedy & Simulation

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Alice removes 10 first, then Bob removes 9, Alice removes 8, etc.
        if n < 10:
            return False
        n -= 10
        remove = 9
        alice_turn = False  # Bob's turn after Alice's first move
        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn
        # alice_turn True means Alice can't move -> Bob wins (return False)
        # alice_turn False means Bob can't move -> Alice wins (return True)
        return not alice_turn
