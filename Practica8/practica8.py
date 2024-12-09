pascal = [[1]]

numRows = int(input("Ingrese el numero de filas a mostar: "))
espacios = numRows
for i in range(numRows-1):
    nextRow = []
    nextRow.append(pascal[i][0])
    for j in range(i+1):
        try:
            n = pascal[i][j] + pascal[i][j+1]
        except:
            n = pascal[i][j]
        nextRow.append(n)
    pascal.append(nextRow)

print(pascal)