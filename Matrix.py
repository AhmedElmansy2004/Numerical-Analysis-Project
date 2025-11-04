class Matrix:

    def __init__ (self, numOfRows=0, numOfCols=0):
        self.rows = numOfRows
        self.cols = numOfCols
        self.values = [[0 for _ in range(numOfCols)] for _ in range(numOfRows)]
    
    def input(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] = (float(input(f"Enter element[{i+1}][{j+1}]: \n")))

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
        self.values = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.values[j][i] = self.values[i][j]

        return transposed
    


    def rank(self):     #do the the rank code here

        return 0

