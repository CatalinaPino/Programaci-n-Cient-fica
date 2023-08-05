import numpy as np
import matplotlib.pyplot as plt
import time
import psutil



crd = []
coordenadas = []


#Extraer lineas y separarlas por espacio
f = open('UNI_CORR_500_01.txt', 'r')

for line in f.readlines():
    extraer = line[0:29]
    aux = extraer.split()
    crd.append(aux)
f.close()


#Identificar las coordenadas y agregarlas a las listas requeridas más adelante
for n in range (4, len(crd)):
    ListAux = crd[n]
    a = []
    tup = []
    X = ListAux[2]
    Y = ListAux[3]
    Z = ListAux[4]
   
    #agregar las coordenadas X, Y y Z a una lista auxiliar a (PARTE 1)
    a.append(float(X))
    a.append(float(Y))
    a.append(float(Z))
    #agregar la lista auxiliar a como sublista (PARTE 1)
    coordenadas.append(a)
    #print(X, Y, Z, sep=' ')




### PARTE 1 ###

#Devolver las coordenadas X, Y y Z de la linea especificada 
k = int(input('Ingrese la linea de coordenadas: '))
print('Las coordenadas de la linea ', k, 'son: ', coordenadas[k-1])
print('')



### PARTE 2 ###

#Cordenada X que mas se repite
FrecuenciasX = {coord [0]: 0 for coord in (coordenadas)}

for coord in coordenadas:
    coordenadaX = coord[0]
    FrecuenciasX[coordenadaX]+=1 #recuento de la frecuencia

max_frecuencia_X = max(FrecuenciasX.values())
coordenada_mas_repetida_X = [numero for numero, Frecuencia in FrecuenciasX.items() if Frecuencia == max_frecuencia_X]
print(f'La(s) coordenadas X que mas se repite(n): {coordenada_mas_repetida_X} con un recuento de {max_frecuencia_X} oportunidades')
print('')
#print(Frecuencias)


#Coordenadas Y que mas se repiten
FrecuenciasY = {coord[1]: 0 for coord in (coordenadas)}

for coord in coordenadas:
    coordenadaY = coord[1]
    FrecuenciasY[coordenadaY]+=1

max_frecuencia_Y = max(FrecuenciasY.values())
coordenada_mas_repetida_Y = [numero for numero, frecuencia in FrecuenciasY.items() if frecuencia == max_frecuencia_Y]
print(f'La(s) coordenadas Y que mas se repite(n): {coordenada_mas_repetida_Y} con un recuento de {max_frecuencia_Y} oportunidades')
print('')

#Coordenadas X,Y que mas se repiten
FrecuenciasXY = {tuple(coord[0:2]): 0 for coord in (coordenadas)}

for coord in coordenadas:
    coordenadaXY = tuple(coord[0:2])
    FrecuenciasXY[coordenadaXY]+=1

max_frecuencia_XY = max(FrecuenciasXY.values())
tupla_mas_repetida = [numero for numero, frecuencia in FrecuenciasXY.items() if frecuencia == max_frecuencia_XY]
print(f'La(s) coordenadas X,Y que mas se repite(n): {tupla_mas_repetida} con un recuento de {max_frecuencia_XY} oportunidades')
print('')




### PARTE 3 ###

ix = 320
iy = 480
mx = (640-ix)/9
my = (0-iy)/5
Xpixel = []
Ypixel = []

#Conversion coordenada metro a pixel
def Conversion(CoordenadaM):
    Xmetro, Ymetro = CoordenadaM
    Xpixel = int(mx * Xmetro + ix)
    Ypixel = int(my * Ymetro + iy)
    return Xpixel , Ypixel


#creacion de matriz de posiciones
Matriz = np.zeros([641 , 481])


#Diccionario frecuencia de posiciones en pixel
FrecuenciaPixel = {(ValX, ValY): 0 for ValX in range(641)for ValY in range (481)}


#Pasar metro a pixel en el diccionario
for coordenada, frecuencia in FrecuenciasXY.items():
    CoordenadaPixel = Conversion(coordenada)
    Xpixel.append(CoordenadaPixel[0])
    Ypixel.append(CoordenadaPixel[1])
    #print(f'La coordenada metrica: {coordenada} pasa a pixel {CoordenadaPixel}' )
    FrecuenciaPixel[CoordenadaPixel] = frecuencia
print('')


#Coordenadas X, Y que mas se repiten en pixel
max_FrecuPixelXY = max(FrecuenciaPixel.values())
XYPixel_mas_repetida = [CordXY for CordXY, frecuenciaXY in FrecuenciaPixel.items() if frecuenciaXY == max_FrecuPixelXY]
print(f"La(s) coordenadas X,Y en pixel que más se repite(n): {XYPixel_mas_repetida} con un recuento de {max_FrecuPixelXY} oportunidades")

print('')


print('El valor minimo de X es: ', min(Xpixel))
print('El valor maximo de X es: ', max(Xpixel))
print('La valor varianza de X es de: ', np.var(Xpixel))
print('')
print('El valor minimo de Y es: ', min(Ypixel))
print('El valor maximo de Y es: ', max(Ypixel))
print('La varianza de Y es de: ', np.var(Ypixel))




bins = 350

heatmap, xedges, yedges = np.histogram2d(Xpixel, Ypixel, bins=bins)

heatmap = heatmap.T

x_extent = [0, 640]
y_extent = [480, 0]

plt.imshow(heatmap, extent=[x_extent[0], x_extent[1], y_extent[0], y_extent[1]], cmap='RdBu')
plt.colorbar(label='Frecuencia')
plt.show()



### CUANTOS RECURSOS CONSUME EL PROGRAMA ###

def get_resource_info(code_to_measure):
    resources_save_data = get_resource_usage(code_to_measure=code_to_measure)
    print(f"Tiempo de CPU: {resources_save_data['tiempo_cpu']} segundos")
    print(f"Uso de memoria virtual: {resources_save_data['memoria_virtual']} MB")
    print(f"Uso de memoria residente: {resources_save_data['memoria_residente']} MB")
    print(f"Porcentaje de uso de CPU: {resources_save_data['%_cpu']} %")


# Función que devuelve el tiempo de CPU y el uso de memoria para un código dado
def get_resource_usage(code_to_measure):
    process = psutil.Process()
    #get cpu status before running the code
    cpu_percent = psutil.cpu_percent()
    start_time = time.time()
    code_to_measure()
    end_time = time.time()
    end_cpu_percent = psutil.cpu_percent() 
    cpu_percent = end_cpu_percent - cpu_percent
    cpu_percent = cpu_percent / psutil.cpu_count()
    
    return {
        'tiempo_cpu': end_time - start_time,
        'memoria_virtual': process.memory_info().vms / (1024 * 1024),  # Convertir a MB
        'memoria_residente': process.memory_info().rss / (1024 * 1024),  # Convertir a MB
        '%_cpu': cpu_percent # Porcentaje de uso de CPU
    }
