from Matrix import *
from Vector import *

# Assumme arrays start with index 1 instead of 0.
# matrix: Coef. of matrix A; 2-D array. Upon successful
# completion, it contains the coefficients of both L and U.
# b: Coef. of vector b; 1-D array
# x: Coef. of vector x (to store the solution)
# tol: Tolerance; smallest possible scaled
# pivot allowed.
# er: Pass back -1 if matrix is singular.
# (Reference var.)

def crout_LU_decompose(matrix, b, x, tol):
    s = [0] * matrix.rows           # An n-element array for storing scaling factors
    o = [0] * matrix.rows           # Use as indexes to pivot rows.
                                    # o(i) stores row number of the ith pivot row.
    er = 0
    matrix_t = matrix.transpose()
    er = crout_decompose(matrix_t, tol, o, s)
    if (er != -1):
        matrix = matrix_t.transpose()
        substitute(matrix, o, b, x)
        matrix.output()
        return x
    else: 
        return "Cannot Solve"
    


def crout_decompose(matrix_t, tol, o, s):
    # Find scaling factors
    for i  in range(matrix_t.rows):                        
        o[i] = i
        s[i] = abs(matrix_t.values[i][0])
        for j in range(1, matrix_t.rows):
            s[i] = max(abs(matrix_t.values[i][j]), s[i])

    for i in range(matrix_t.rows):
        scaled_pivot(matrix_t, o, s, i)        # Locate the kth pivot row

        # Check for singular or near-singular cases
        if (abs(matrix_t.values[o[i]][i]) / s[o[i]]) < tol:
            return -1                                           #handle for infinite solutions

        for j in range(i+1, matrix_t.rows):
            factor = matrix_t.values[o[j]][i] / matrix_t.values[o[i]][i]
            # Instead of storing the factors in another matrix,
            # We reuse the space in A to store U.
            matrix_t.values[o[j]][i] = factor

            # Eliminate the coefficients at column j
            # forming the L matrix
            for k in range(i+1, matrix_t.cols):
                matrix_t.values[o[j]][k] = matrix_t.values[o[j]][k] - factor * matrix_t.values[o[i]][k]



    # Check for singular or near-singular cases
    n = matrix_t.rows-1
    if (abs(matrix_t.values[o[n]][n]) / s[o[n]]) < tol:
        return -1                                           #handle for infinite solutions



def scaled_pivot(matrix, o, s, k):
    # Find the largest scaled coefficient in column k
    p = k                                           # p is the index to the pivot row
    big = abs(matrix.values[o[k]][k] / s[o[k]])
    for i in range(k+1, matrix.rows) :
        temp = abs(matrix.values[o[i]][k] / s[o[i]])
        if (temp > big):
            big = temp
            p = i

    # Swap row k with the pivot row by swapping the
    # indexes. The actual rows remain unchanged
    temp = o[p]
    o[p] = o[k]
    o[k] = temp

    temp = s[p]
    s[p] = s[k]
    s[k] = temp


def substitute(matrix_t, o, b, x):
    y = [0] * matrix_t.rows
    n = matrix_t.rows
    for i in range(n):
        summ = 0
        for j in range(0, i):
            summ += matrix_t.values[i][o[j]] * y[j]
        y[i] = (b[i] - summ) / matrix_t.values[i][o[i]]


    for i in range(n-1, -1, -1):
        summ = y[i]
        for j in range(i+1, n):
            summ -= matrix_t.values[i][o[j]] * x.values[o[j]]
        x.values[o[i]] = summ



# Issues to be fixed:
# 1. forcing zeros on pivot
# 2. Separation of L and U requires O[] due to misplaced "columns"
