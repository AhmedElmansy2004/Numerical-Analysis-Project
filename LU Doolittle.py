'''
LU decomposition using Doolittle algorithm
A: coefficients matrix
n: number of equations
L: lower triangular matrix
U: upper triangular matrix
s: scaling vector
o: order vector
tol: tolerance
er: error flag
'''

def LUDecomp(A, b, n, x, tol, er):
    o = [0] * n
    s = [0] * n
    decompose(A, n, tol, o, s, er)
    if er != -1:
        substitute(A, o, n, b, x)
    return

def decompose(A, n, tol, o, s, er):
    for i in range(n):
        o[i] = i
        s[i] = abs(A[i][0])
        for j in range(1, n):
            s[i] = max(s[i], abs(A[i][j]))
        if s[i] == 0.0: er = -1 # not in lecture slides

    for k in range(n-1):
        pivot(A, o, s, n, k)
        if (abs(A[o[k]][k]/s[o[k]]) < tol):
            er = -1
            return
        
        for i in range(k+1, n):
            factor = A[o[i]][k] / A[o[k]][k]
            # instead of storing the factors in another matrix L
            # we reuse the space in A to store L
            A[o[i]][k] = factor

            # eliminate the coefficients at column j in subsequent rows
            for j in range(k+1, n):
                A[o[i]][j] -= factor * A[o[k]][j]

    if (abs(A[o[n-1]][n-1]/s[o[n-1]]) < tol):
        er = -1

    return

def pivot(A, o, s, n, k):
    p = k
    big = abs(A[o[k]][k]/ s[o[k]])
    for i in range(k+1, n):
        dummy = abs(A[o[i]][k] / s[o[i]])
        if (dummy > big):
            big = dummy
            p = i
    
    # swap if necessary -> row k with pivot row
    # by swapping indices, actual rows remain unchanged
    if (p != k):
        o[k], o[p] = o[p], o[k]

    return

def substitute(A, o, n, b, x):
    y = [0] * n
    y[o[0]] = b[o[0]]

    # forward substitution
    for i in range(1, n):
        sum_val = b[o[i]]
        for j in range(i):
            sum_val -= A[o[i]][j] * y[o[j]]
        y[o[i]] = sum_val

    # back substitution
    x[n-1] = y[o[n-1]] / A[o[n-1]][n-1]
    for i in range(n-2, -1, -1):
        sum_val = 0
        for j in range(i+1, n):
            sum_val += A[o[i]][j] * x[j]
        x[i] = (y[o[i]] - sum_val) / A[o[i]][i]
    return


if __name__ == "__main__":
    A = [
        [1, 1, -1],
        [6, 2, 2],
        [-3, 4, 1]
         ]
    b = [-3, 2, 1]
    n = 3
    x = [0, 0, 0]
    tol = 0.0001
    er = 0
    
    LUDecomp(A, b, n, x, tol, er)
    print(A)
    print(x)

    A = [
        [1, -1],
        [1, 2]
    ]
    b = [0, 6]
    x = [0, 0]
    n = 2
    tol = 0.0001
    er = 0

    LUDecomp(A, b, n, x, tol, er)
    print(A)
    print(x)