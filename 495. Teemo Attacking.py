class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
            
        total = 0
        n = len(timeSeries)
        
        for i in range(n - 1):
            # Khoảng cách giữa hai lần tấn công liên tiếp
            diff = timeSeries[i + 1] - timeSeries[i]
            
            # Nếu khoảng cách < duration → có chồng lấn
            # Chỉ cộng thêm phần không bị chồng (hoặc toàn bộ nếu không chồng)
            total += min(diff, duration)
        
        # Lần tấn công cuối cùng luôn cộng đủ duration
        total += duration
        
        return total