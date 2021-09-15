def hasNeighbor(A:list, B:list, row:int, col:int, i:int, j:int) -> None:
    if (B[i][j] == -1):
        return
    
    B[i][j] = -1
    
    if (i+1 < row):
        if (A[i+1][j] == A[i][j]):
            hasNeighbor(A, B, row, col, i+1, j)

    if (i-1 >= 0):
        if(A[i-1][j] == A[i][j]):
            hasNeighbor(A, B, row, col, i-1, j)
    
    if (j+1 < col):
        if (A[i][j + 1] == A[i][j]):
            hasNeighbor(A, B, row, col, i, j+1)

    if (j - 1 >= 0):
        if (A[i][j - 1] == A[i][j]):
            hasNeighbor(A, B, row, col, i, j-1)



def solution(A:list) -> int:
    row = len(A)
    column = len(A[0])
    res = 0

    if (row == 0 or column == 0):
        return 

    B = [arr[:] for arr in A]

    for i in range(row):
        for j in range(column):
            if(B[i][j] >= 0):
                hasNeighbor(A, B, row, column, i, j)
                res += 1
    return res 




if __name__ == "__main__":
    row = int(input())
    column = int(input())
    mx=[list(map(int, input().strip().split()[:column])) for _ in range(row)]


    print(solution(mx))
