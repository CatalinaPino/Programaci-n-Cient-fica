#f = open('powers.txt', 'w')
#for i in range (1, 1001): # como esta especificado de 1 a 1001, pero teoricamente comienza desde 0 solo llegara 1000
#    print(i, i**2, i**3, i**4, sep= ',', file= f)
#f.close()

f = open('powers.txt', 'r') #abre el archibo par leer
squares, cubes, fourths = [], [], [] #crea listas para cada uno
for line in f.readlines(): # readlines da la cantidad de lineas que contiene el texto como len y lee cada una de ellas a la vez
    fields = line.split(',') #separa los caracteres de las lineas con coma
    squares.append(int(fields[1])) # toma el caracter [1] dentro de cada fila. 1 es el cuadrado
    cubes.append(int(fields[2])) 
    fourths.append(int(fields[3]))
f.close()
n = 500
print(' ')
print(n, 'cubed is', cubes[n-1])