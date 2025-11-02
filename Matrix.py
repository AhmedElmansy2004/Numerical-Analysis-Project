class Matrix:

    def __init__ (self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def __init__ (self, numOfRows, numOfCols):
        self.rows = numOfRows
        self.cols = numOfCols
        self.matrix = []
    
    def input(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(float(input(f"Enter element[{i+1}][{j+1}]: \n")))
            self.matrix.append(row)

    def output(self):
        for i in range(self.rows):
            for j in range(self.cols):
                elementij = self.matrix[i][j]
                display = int(elementij) if elementij.is_integer() else elementij
                print(f"{display:>8}", end="")
            print("\n")

    def clear(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def transpose(self):
        transposed = Matrix(self.rows, self.cols)
        for i in range(transposed.rows):
            row = []
            for j in range(transposed.cols):
                row.append(self.matrix[j][i])
            transposed.matrix.append(row)

        return transposed


    def rank(self):     #do the the rank code here

        return 0


