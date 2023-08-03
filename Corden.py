import numpy as np

crd = []
coordenadas = []

f = open('UNI_CORR_500_01.txt', 'r')

for line in f.readlines():
    extraer = line[0:29]
    aux = extraer.split()
    crd.append(aux)
f.close()

for n in range (4, len(crd)):
    ListAux = crd[n]
    a = []
    auxX = ListAux[2]
    auxY = ListAux[3]
    auxZ = ListAux[4]
    a.append(float(auxX))
    a.append(float(auxY))
    a.append(float(auxZ))
    coordenadas.append(a)
    #print(auxX, auxY, auxZ, sep = ' ')

k = int(input('Ingrese la linea de coordenadas: '))
print('Las corenadas de la linea ', k, 'son: ', coordenadas[k-1])