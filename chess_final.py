import random

#Crear tablero
letras = ["A", "B","C", "D", "E", "F", "G", "H"]
numeros = ["8","7", "6","5","4","3","2","1"]

piezas = []

ubicacion = {}

juego = {"player 1": ["R", "K"],
"player 2": "Q"}

tablero = []

tablero_aesthetic = [["-", "A", "B", "C", "D", "E", "F", "G", "H", "-"],
           ["8", "■", " ", "■", " ", "■", " ", "■", " ", "8"],
           ["7", " ", "■", " ", "■", " ", "■", " ", "■", "7"],
           ["6", "■", " ", "■", " ", "■", " ", "■", " ", "6"],
           ["5", " ", "■", " ", "■", " ", "■", " ", "■", "5"],
           ["4", "■", " ", "■", " ", "■", " ", "■", " ", "4"],
           ["3", " ", "■", " ", "■", " ", "■", " ", "■", "3"],
           ["2", "■", " ", "■", " ", "■", " ", "■", " ", "2"],
           ["1", " ", "■", " ", "■", " ", "■", " ", "■", "1"],
           ["-", "A", "B", "C", "D", "E", "F", "G", "H", "-"]]

# crear tablero
for numero in numeros:
    casillas = [letra+numero for letra in letras]
    tablero.append(casillas)
    
#imprimir tablero de jugadas
def imprimir_tablero():
    for row in tablero:
        for tile in row:
            print(tile, end=" ")
        print("")
    print("\n")

def agregar_piezas(tablero, piezas, pieza):
    row  = random.randint(0,7)
    col = random.randint(0,7)
    
    pos = tablero[row][col]

    #Checar que o este ocupando un lugar ya usado
    if pos in piezas:
        agregar_piezas(tablero, piezas, pieza)

    #agregar piezas para checar lo mismo
    piezas.append(pieza)
    
    # agregar valor al dict
    
    ubicacion[pieza] = pos
    tablero[row][col] = pieza
    tablero_aesthetic[row+1][col+1] = pieza

reina = agregar_piezas(tablero, piezas, juego["player 2"])
torre =  agregar_piezas(tablero, piezas, juego["player 1"][0])
rey =  agregar_piezas(tablero, piezas, juego["player 1"][1])

# imprimir tablero bonito
for row in tablero_aesthetic:
  for tile in row:
    print(tile, end=" ")
  print(" ")

# las posiciones por si no se encuntran en el tablero
print(ubicacion)

def move(ubi, tab, name,letras):
    # todas las posibles diagonales del tablero
    diagonal=[["A8","B7","C6","D5","E4","F3","G2","H1"],
["A7","B6","C5","D4","E3","F2","G1"],
["A6","B5","C4","D3","E2","F1"],
["A5","B4","C3","D2","E1"],
["A4","B3","C2","D1"],
["A3","B2","C1"],
["A2","B1"],
["B8","C7","D6","E5","F4","G3","H2"],
["C8","D7","E6","F5","G4","H3"],
["D8","E7","F6","G5","H4"],
["E8","F7","G6","H5"],
["F8","G7","H6"],
["G8","H7"],
#Lista izquierda
["H2","G1"],
["H3","G2","F1"],
["H4","G3","F2","E1"],
["H5","G4","F3","E2","D1"],
["H6","G5","F4","E3","D2","C1"],
["H7","G6","F5","E4","D3","C2","B1"],
["H8","G7","F6","E5","D4","C3","B2","A1"],
["G8","F7","E6","D5","C4","B3","A2"],
["F8","E7","D6","C5","B4","A3"],
["E8","D7","C6","B5","A4"],
["D8","C7","B6","A5"],
["C8","B7","A6"],
["B8","A7"]]

    movimientos =[]
    let = ubi[name][0]
    indice =letras.index(let)
    if name == "R":

        for row in tab:
            if name in row:
                for cell in row: 
                    if not cell == name :
                        movimientos.append(cell)
      
        for row in tab:
            if name not in row:
                movimientos.append(row[indice])
            
        return movimientos
    
    if name == "K":
        tablero2= []
        for x in tab:
            for i in x:
                tablero2.append(i)
       
        y = 0
        for row in tab:
            try:
                r = row.index("K")
                yf= y
            except:
                y +=1
        dig=[]
        try:
            movimientos.append(tab[yf-1][r-1])
        except:
            pass
        try:
            movimientos.append(tab[yf+1][r-1])
        except:
            pass

        try:
            movimientos.append(tab[yf-1][r+1])
        except:
            pass
        try:
            movimientos.append(tab[yf+1][r+1])
        except:
            pass

        try:
            movimientos.append(tab[yf][r-1])
        except:
            pass

        try:
            movimientos.append(tab[yf][r+1])
        except:
            pass

        try:
            movimientos.append(tab[yf-1][r])
        except:
            pass
        try:
            movimientos.append(tab[yf+1][r])
        except:
            pass     
            
        return movimientos

    if name == "Q":
        for row in tab:
            if name in row:
                for cell in row: 
                    if not cell == name:
                        movimientos.append(cell)
        for row in tab:
            if name not in row:
                movimientos.append(row[indice])

        for x in diagonal:
            if ubicacion["Q"] in x:
                for i in x:
                    
                    if i !=  ubicacion["Q"]:
                        movimientos.append(i)   
   
        return movimientos           

torre_movimientos = move(ubicacion, tablero, "R", letras)
rey_movimientos = move(ubicacion, tablero, "K", letras)
reina_movimientos = move(ubicacion, tablero, "Q", letras)
print(f"Los movimientos de la torre son {torre_movimientos}")
print(f"Los movimientos de la reina son {reina_movimientos}")

legales =[]
for x in rey_movimientos:
    if x not in reina_movimientos:
        legales.append(x)
print(f"Los movimimientos del rey son {legales}")

if "Q" in torre_movimientos or ubicacion["Q"] in reina_movimientos:
    print(f"Mueve tu torre {ubicacion['R']} a {ubicacion['Q']} para eliminar a la Reina")
else:
    print(f"Torre ({ubicacion['R']}) sin jugada")

if ubicacion["K"] in reina_movimientos or "K" in reina_movimientos:
    print('\033[1m'+"EL REY ESTÁ EN JAQUE"+'\033[0m')