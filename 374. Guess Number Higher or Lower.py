# LeetCode 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            mid = left + (right - left) // 2
            
            result = guess(mid)        # ← Sửa ở đây: không dùng self.guess
            
            if result == 0:
                return mid
            elif result == 1:   # mid < picked → tìm bên phải
                left = mid + 1
            else:               # mid > picked → tìm bên trái
                right = mid - 1
                
        return -1  # Không bao giờ chạy đến đây