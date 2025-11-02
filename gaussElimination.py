def inputMatrix():
    numOfRows = int(input("Enter number of rows: "))
    numOfCols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(numOfRows):
        row = []
        for j in range(numOfCols):
            row.append(float(input(f"Enter elements of row{i+1}: \n")))
        matrix.append(row)

    return matrix

print(inputMatrix())