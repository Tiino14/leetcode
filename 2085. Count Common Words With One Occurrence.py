# LeetCode 2085. Count Common Words With One Occurrence
# Difficulty: Easy
# Topic: Array & Hashing

from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        return sum(1 for w in count1 if count1[w] == 1 and count2[w] == 1)
