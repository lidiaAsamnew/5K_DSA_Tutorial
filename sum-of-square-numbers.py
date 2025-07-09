class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = sqrt(c)//1
        while a<=b:
            num = a**2 + b**2
            if num < c:
                a += 1
            elif num > c:
                b -= 1
            else:
                return True
        
        return False
