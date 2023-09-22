import random
import numpy as np

def busquedaLineal(A, n, m, x):
    encontrado = 0
    for i in range(n):
        for j in range(m):
            if(x == A[i][j]):
                encontrado += 1
    return encontrado

def crearMatrizRandom(n, m, r):
    A = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            A[i][j] = random.randint(0, r)
    return A

def crearHistograma(A, n, m, r):
    h = np.zeros((2, r + 1))
    for i in range(r + 1):
        h[0][i] = i
    
    for i in range(r + 1):
        h[1][i] = busquedaLineal(A, n, m, i)

    return h

def ordenarHistograma(A, r):
    for i in range(r + 1):
        for j in range(r + 1):
            if(A[1][i] < A[1][j]):
                A[1][i], A[1][j] = A[1][j], A[1][i]
                A[0][i], A[0][j] = A[0][j], A[0][i]
    return A

def main():
    filas = 5
    columnas = 5
    rango = 15

    matriz = crearMatrizRandom(filas, columnas, rango)
    print(f"Escala de grises \n{matriz}")

    histograma = crearHistograma(matriz, filas, columnas, rango)
    print(f"\nHistograma \n{histograma}")

    histograma = ordenarHistograma(histograma, rango)
    print(f"\nHistograma ordenado \n{histograma}")

    print(f"\nMinimo del histograma: {int(histograma[0][0])}")

main()
