from Matrix import *
from Vector import *
from gauss_seidel import *

def run_system(matrix_values, ans_values, guess_values, abs_rel_err=1e-8):
    """Helper function to run and print a Gauss–Seidel test."""
    rows = len(matrix_values)
    cols = len(matrix_values[0])

    matrix = Matrix(rows, cols)
    matrix.values = matrix_values
    print("\nMatrix:")
    matrix.output()

    ans = Vector(rows)
    ans.values = ans_values

    initial_guess = Vector(rows)
    initial_guess.values = guess_values

    print("\nRunning Gauss–Seidel...")
    result = gauss_seidel(matrix, ans, initial_guess, abs_rel_err=abs_rel_err)

    if isinstance(result, str):
        print(result)
    elif isinstance(result, Vector):
        print("Solution Vector:")
        for i, val in enumerate(result.values):
            print(f"x{i+1} = {val:.6f}")


def main():
    print("=== Convergent System ===")
    run_system(
        matrix_values=[[4, 1],
                       [2, 3]],
        ans_values=[1, 2],
        guess_values=[0, 0],
        abs_rel_err=5e-8
    )

    print("\n=== Divergent System ===")
    run_system(
        matrix_values=[[1, 3],
                       [2, 1]],
        ans_values=[7, 4],
        guess_values=[0, 0],
        abs_rel_err=5e-8
    )


if __name__ == '__main__':
    main()
