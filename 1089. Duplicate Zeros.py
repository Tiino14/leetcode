class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        
        while i < n:
            if arr[i] == 0:
                # Chèn 0 vào vị trí i+1 và dịch các phần tử sau sang phải
                arr.insert(i + 1, 0)
                # Xóa phần tử cuối (vì độ dài cố định)
                arr.pop()
                # Bỏ qua vị trí vừa chèn
                i += 2
            else:
                i += 1