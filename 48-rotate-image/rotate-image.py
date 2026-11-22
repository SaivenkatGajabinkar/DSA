class Solution:
    def reverse(self,matrix):
        left=0
        right=len(matrix)-1
        while left<right:
            matrix[left],matrix[right]=matrix[right],matrix[left]
            left+=1
            right-=1
        
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        for i in range(0,n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(0,n):
            self.reverse(matrix[i])
        return matrix