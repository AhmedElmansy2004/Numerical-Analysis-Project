'''
Gauss-Jordan
A: coefficients matrix
b: constant vector
n: number of equations
x: solution vector
tol: tolerance
er: error flag
'''
def gauss_jordan(A, b, n, x, tol, er):
    s = [0] * n # initialize list with n places
    for i in range(n): # perform elimination n times
        s[i] = abs(A[i][0])
        for j in range(1, n): # search for largest pivot
            s[i] = max(s[i], abs(A[i][j]))
                

    Eliminate(A, b, n, s, tol, er)
    if (er != -1):
        substitute(A, n, b, x)
    return


def Eliminate(A, b, n, s, tol, er):
    for k in range(n):
        pivot(A, b, s, n, k)
        if (abs(A[k][k]/s[k]) < tol):
            er = -1
            return
        # normalize pivot row
        pivot_value = A[k][k]
        for j in range(n):
            A[k][j] /= pivot_value
        b[k] /= pivot_value

        for i in range(n): # elimination
            if (i == k): continue
            factor = A[i][k]# / A[k][k] #no need to divide
            for j in range(n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

        if (abs(A[n-1][n-1]/s[n-1]) < tol):
            er = -1
    return

def pivot(A, b, s, n, k):
    p = k
    big = abs(A[k][k]/ s[k])
    for i in range(k+1, n):
        dummy = abs(A[i][k] / s[i])
        if (dummy > big):
            big = dummy
            p = i
    
    if (p != k): # swap if necessary
        for j in range(n):
            A[k][j], A[p][j] = A[p][j], A[k][j] # swap
        
        b[k], b[p] = b[p], b[k]

        s[k], s[p] = s[p], s[k]

    return

def substitute(A, n, b, x):
    for i in range(n):
        x[i] = b[i]

    return

if __name__ == '__main__':
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
    gauss_jordan(A, b, n, x, tol, er)
    print(A)
    print(x)