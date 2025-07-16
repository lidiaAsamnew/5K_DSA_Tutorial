class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        rows, cols = len(mat), len(mat[0])
        row, col = 0, 0
        gong_up = True

        while len(ans) < rows*cols:
            if going_up:
                while row >= 0 and col<cols:
                    ans.append(mat[row][col])
                    row -= 1
                    col += 1
                if col== cols:
                    row += 2
                    col -= 1
                else:
                    row += 1
                going_up = False
            else:
                while col>=0 and row<rows:
                    ans.append(mat[row][col])
                    col -= 1
                    row += 1
                if row == rows:
                    col += 2
                    row -= 1
                else:
                    col += 1
                going_up = True
        return ans
