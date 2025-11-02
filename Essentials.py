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
                print(self.matrix[i][j])
            print()

    def clear(self):
        self.rows = 0
        self.cols = 0
        self.matrix = []

    def rank(self):     #do the the rank code here

        return 0


