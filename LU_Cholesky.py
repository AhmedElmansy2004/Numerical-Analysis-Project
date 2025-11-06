import math
import time

def valid_Cholesky(matrix):

    # Square
    if (len(matrix) != len(matrix[0])):
        return False

    n = len(matrix)

    # Symmetric
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if abs(matrix[row][col] - matrix[col][row]) > 1e-9:
                return False

    return True

def decompose_Cholesky(coeff):
    n = len(coeff)
    L = [[0.0 for _ in range(n)] for _ in range(n)]
    U = [[0.0 for _ in range(n)] for _ in range(n)]

    # Decompose

    try:
        for row in range(n):
            for col in range(row + 1):
                sum_val = 0.0
                k = 0
                while (k < col):
                    sum_val += L[row][k] * L[col][k]
                    k += 1

                if (row == col):
                    L[row][col] = math.sqrt(coeff[row][row] - sum_val)
                else:
                    L[row][col] = (coeff[row][col] - sum_val) / L[col][col]

        return True, L, U

    except Exception:
        return False, L, U

def solve(L, U, consts):
    n = len(L)
    solution = [0.0 for _ in range(n)]
    y = [0.0 for _ in range(n)]

    # Ly = consts (forward)
    for row in range(n):
        sum_val = 0.0
        k = 0
        while (k < row):
            sum_val += L[row][k] * y[k]
            k += 1
        y[row] = (consts[row] - sum_val) / L[row][row]

    # Ux = y (backward)
    row = n - 1
    while (row >= 0):
        sum_val = 0.0
        k = row + 1
        while (k < n):
            sum_val += U[row][k] * solution[k]
            k += 1
        solution[row] = (y[row] - sum_val) / U[row][row]
        row -= 1

    return solution

# return -> {valid, solution, time, L_Matrix, U_Matrix}
def LU_Cholesky(coeff, consts):
    L = []
    U = []
    solution = []
    result = {}

    # Start Time
    start_time = time.time()

    # Check Validitiy
    valid = valid_Cholesky(coeff)
    if not valid:
        return {"valid": False, "solution": None, "time": 0, "L": [], "U": []}

    # Decompose
    valid, L, U = decompose_Cholesky(coeff)
    if not valid:
        return {"valid": False, "solution": None, "time": 0, "L": [], "U": []}

    # Solve
    solution = solve(L, U, consts)

    # End Time
    end_time = time.time()
    # Elapsed Time
    elapsed_time = end_time - start_time

    # Return the Result
    result = {
        "valid": True,
        "solution": solution,
        "time": elapsed_time,
        "L": L,
        "U": U
    }

    return result
