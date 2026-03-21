class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)
        
        for i in range(m):
            if flowerbed[i] == 0:
                left_ok = i == 0 or flowerbed[i-1] == 0
                right_ok = i == m-1 or flowerbed[i+1] == 0
                
                if left_ok and right_ok:
                    count += 1
                    if count >= n:
                        return True
                    flowerbed[i] = 1  
        
        return count >= n