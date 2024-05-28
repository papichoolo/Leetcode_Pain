class Solution:
    def validsudoku(arr):
        row=[[0 for i in range(9)] for j in range(9)]
        col=[[0 for i in range(9)] for j in range(9)]
        box= [[0 for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if arr[i][j] != -1:
                    num=int(arr[i][j])-1
                    k=(i//3)*3+j//3
                    if row[i][num] or col[j][num] or box[k][num]:
                        return False
                    row[i][num]=col[j][num]=box[k][num]=1
        return True
