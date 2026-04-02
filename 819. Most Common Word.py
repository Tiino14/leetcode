# LeetCode 819. Most Common Word
# Difficulty: Easy
# Topic: Array & Hashing

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(w for w in words if w not in banned_set)
        return count.most_common(1)[0][0]
