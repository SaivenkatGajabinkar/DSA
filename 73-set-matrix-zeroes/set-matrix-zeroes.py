class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        r_visited=[1 for _ in range(n)]
        c_visited=[1 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r_visited[i]=0
                    c_visited[j]=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    if c_visited[j]==0 or r_visited[i]==0 or matrix[i][j]==0:
                        matrix[i][j]=0
        return matrix


        