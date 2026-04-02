# LeetCode 2114. Maximum Number of Words Found in Sentences
# Difficulty: Easy
# Topic: Array & String

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(s.split()) for s in sentences)
