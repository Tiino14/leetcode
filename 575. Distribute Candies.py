class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Số loại kẹo khác nhau
        unique_types = len(set(candyType))
        
        # Chỉ được ăn n/2 viên
        max_eat = len(candyType) // 2
        
        # Số loại tối đa có thể ăn
        return min(unique_types, max_eat)