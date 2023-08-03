#import numpy as np
Linea = '|' + '*'*65 + '|'

print(Linea)
materia = str(input('Ingrese el nombre de la Materia (FIN para salir): '))
LMateria = []
LPorcentaje = []

while materia != 'FIN':
    LMateria.append(materia)
    materia = str(input('Ingrese el nombre de la Materia (FIN para salir): '))
print(Linea)

for i in range (0, len(LMateria)):
    porcentaje = print('Ingrese procentaje de la materia ', LMateria[i],': ')
    LPorcentaje.append(porcentaje)
print(Linea)