from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = Counter()
        for c in nums3:
            for d in nums4:
                count[c + d] += 1
        
        ans = 0
        for a in nums1:
            for b in nums2:
                ans += count.get(-(a + b), 0)
        
        return ans