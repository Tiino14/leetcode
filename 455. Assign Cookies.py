class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # trẻ dễ tính trước
        s.sort()  # bánh nhỏ trước
        
        child = 0   # chỉ số trẻ hiện tại
        cookie = 0  # chỉ số bánh hiện tại
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # bánh đủ lớn → gán cho trẻ này, chuyển sang trẻ tiếp theo
                child += 1
            # dù gán hay không, bánh đã dùng → chuyển sang bánh tiếp theo
            cookie += 1
        
        return child