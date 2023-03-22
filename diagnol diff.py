def diagonalDifference(arr):
    l=r=0
    n=len(arr)
    for i in range(n):
        l+=arr[i][i]
        r+=arr[i][n-1-i]
        
    return abs(l-r)
        