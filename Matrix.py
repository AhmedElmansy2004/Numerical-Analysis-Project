class Matrix:

    def __init__ (self, numOfRows=0, numOfCols=0):
        self.rows = numOfRows
        self.cols = numOfCols
        self.values = []
    
    def input(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(float(input(f"Enter element[{i+1}][{j+1}]: \n")))
            self.values.append(row)

    def output(self):
        for i in range(self.rows):
            for j in range(self.cols):
                elementij = self.values[i][j]
                display = int(elementij) if elementij.is_integer() else elementij
                print(f"{display:>8}", end="")
            print("\n")

    def clear(self):
        self.rows = 0
        self.cols = 0
        self.values = []

    def transpose(self):
        transposed = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.values[j][i])
            transposed.values.append(row)

        return transposed


    def rank(self):     #do the the rank code here

        return 0

