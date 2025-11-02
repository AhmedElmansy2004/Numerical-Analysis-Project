from Matrix import *
from Vector import *
from gauss_sidel import *

def main():
    rows = int(input("Enter # of rows: "))
    cols = int(input("Enter # of cols: "))

    matrix = Matrix(rows, cols)

    matrix.input()
    matrix.output()

    ans = Vector(3)
    ans.values = [10, 11, 3]

    intial_guess = Vector(3)
    intial_guess.values = [0, 0, 0]

    gauss_sidel(matrix, ans, intial_guess, iterations=3).output()



if __name__ == '__main__':
    main()