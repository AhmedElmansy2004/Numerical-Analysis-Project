from Matrix import *

def main():
    rows = int(input("Enter # of rows: "))
    cols = int(input("Enter # of cols: "))

    matrix = Matrix(rows, cols)

    matrix.input()
    matrix.output()

    trans = matrix.transpose()

    trans.output()



if __name__ == '__main__':
    main()