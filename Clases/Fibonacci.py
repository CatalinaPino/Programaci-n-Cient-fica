
f = open('SecuenciaFibonacci.txt', 'w')
Lista =[1, 1]
print(Lista)
print(Lista, end='\n', file=f)
for i in range (2,101): #como la lista ya comenzo desde 0 tiene que continuar hasta el 100
    Lista.append(Lista[i-1] + Lista[i-2])
    print(Lista, end='\n')
    print(Lista, end='\n', file=f)
f.close()

#siempre que se especifica file = f se imprime en el archivo txt, si no se escribe
#se imprimira dentro del programa. Para imprimir en ambos lados hay que utilizar 2
#print() distintos.

