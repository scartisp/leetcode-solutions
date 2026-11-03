class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)-1
        n = len(matrix[0])-1
        columnBound = 0
        rowBound = 1
        i = j = 0
        goPositive = True
        ans = []

        while len(ans) < len(matrix)*len(matrix[0])-1:
            if goPositive:
                while j < n:
                    ans.append(matrix[i][j])
                    j += 1
                n -= 1
                while i < m:
                    ans.append(matrix[i][j])
                    i += 1
                m -= 1
            else:
                while j > columnBound:
                    ans.append(matrix[i][j])
                    j -= 1
                columnBound += 1
                while i > rowBound:
                    ans.append(matrix[i][j])
                    i -= 1
                rowBound += 1
            
            goPositive = not goPositive
        
        ans.append(matrix[i][j])
        return ans
