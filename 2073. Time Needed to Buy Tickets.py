# LeetCode 2073. Time Needed to Buy Tickets
# Difficulty: Easy
# Topic: Array & Simulation

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        for i, t in enumerate(tickets):
            # Before k: full min(t, tickets[k]); after k: min(t, tickets[k]-1)
            if i <= k:
                time += min(t, tickets[k])
            else:
                time += min(t, tickets[k] - 1)
        return time
