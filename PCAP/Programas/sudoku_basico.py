filas =[]
sudoku_ok = False
for i in range(9):
    linea = input("linea " + str(i)+ ": ")
    if  linea.isnumeric() and len(linea) == 9 and sorted(linea) == list("123456789"):
        sudoku_ok = True
        filas.append(linea)
if sudoku_ok:
    print("sudoku valido")





