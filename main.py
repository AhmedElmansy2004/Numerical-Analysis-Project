from Matrix import *
from Vector import *
from gauss_seidel import *
from LU_crout import *

def run_system(matrix_values, ans_values, tol):
    """Helper function to run and print a Gauss–Seidel test."""
    rows = len(matrix_values)
    cols = len(matrix_values[0])

    matrix = Matrix(rows, cols)
    matrix.values = matrix_values
    print("\nMatrix:")

    ans = Vector(rows)
    ans.values = ans_values

    x = Vector(rows)

    print("\nRunning Crout's LU Decomposition...")
    result = crout_LU_decompose(matrix, ans_values, x, tol)

    if isinstance(result, str):
        print(result)
    elif isinstance(result, Vector):
        print("Solution Vector:")
        for i, val in enumerate(result.values):
            print(f"x{i+1} = {val:.6f}")

        matrix.output()


def main():

    run_system(
        matrix_values=[[1, 1, 1],
                       [2, -1, -1],
                       [1, -1, 1]],
        ans_values=[3, 3, 9],
        tol=1e-12
    )

if __name__ == '__main__':
    main()
