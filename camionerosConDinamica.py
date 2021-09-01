from decorators import tiempoDeEjecucion
import math

def armarSolucion(camino, solucion):
    lista=[]
    cantidad=0
    i=solucion[len(solucion)-1]
    while(camino[i]>0):
        lista.append(i)
        cantidad+=1
        i=solucion[i]
    lista.reverse()

    print("Cantidad minima de paradas: ", cantidad)
    print("Debe detenerse en las paradas: ")
    for i in range(len(lista)):
        print(lista[i])

def hallarMenor(camino, visitado, posicion):
    menor=9999
    for i in range(1, len(visitado)):
        if(visitado[i]==0):
            if(camino[i]<menor):
                menor=camino[i]
                posicion=i
    return posicion

def dijkstra(matriz):
    longitud = len(matriz[0]) 
    posicion=0
    visitado=[0 for x in range(longitud)]
    camino= [0 for x in range(longitud)]
    solucion= [0 for x in range(longitud)]
    for i in range(1, longitud):
       camino[i]= matriz[0][i]
    visitado[0]=1
    for i in range(1, longitud-1):
        posicion= hallarMenor(camino, visitado, posicion)
        visitado[posicion]=1
        for j in range(1, longitud):
            if(visitado[j]==0):
                if(camino[posicion]+matriz[posicion][j]< camino[j]):
                    camino[j]=camino[posicion]+matriz[posicion][j]
                    solucion[j]=posicion

    armarSolucion(camino, solucion)


def armarMatriz(n, distancias):
    longi = len(distancias) + 1
    matriz = [[9999] * (longi) for i in range(longi)]
    for i in range(longi):
        acum = 0
        aux=longi
        for j in range(i, longi - 1):
            acum += distancias[j]
            if acum <= n:
                matriz[i][j + 1] = aux
            aux-=1

    return matriz


@tiempoDeEjecucion("dinamica")
def dinamica():
    n = 80
    distancias = [23, 55, 47, 36,11]
    matriz = armarMatriz(n, distancias)
    print(matriz)
    input()
    dijkstra(matriz)

dinamica()