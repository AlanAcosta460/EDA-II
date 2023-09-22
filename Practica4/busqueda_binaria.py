import random

def busquedaBinariaIterativa(A, x, p, r):
    while(p <= r):
        medio = int((p + r)/2)
        if(x == A[medio]):
            return medio
        else:
            if(A[medio] < x):
                p = medio + 1
            else:
                r = medio - 1
    return -1

def busquedaBinariaRecursiva(A, x, p, r):
    if(p > r):
        return -1
    medio = int((p + r)/2)
    if(x == A[medio]):
        return medio
    else:
        if(x < A[medio]):
            return busquedaBinariaRecursiva(A, x, p, medio-1)
        else:
            return busquedaBinariaRecursiva(A, x, medio+1, r)

def insertionSort(A, n):
    for j in range(1, n):
        llave = A[j]
        i = j-1
        while(i >= 0 and A[i] > llave):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = llave

def crearListaRandom():
    A = [0] * 20
    for i in range(20):
        A[i] = random.randint(1, 20)
    return A

def main():
    llave = random.randint(1, 20)
    lista = crearListaRandom()
    print("La lista es: ", lista)
    insertionSort(lista, len(lista))
    print("La lista ordenada es: ", lista)
    print("La llave es: ", llave)
    print("\nBUSQUEDA BINARIA ITERATIVA")
    a = busquedaBinariaIterativa(lista, llave, 0, len(lista)-1)
    if(a != -1):
        print("El indice es: ", a, "\nY el elemento es: ", lista[a])
    else:
        print("Elemento no encontrado")
    print("\n\nBUSQUEDA BINARIA RECURSIVA")
    b = busquedaBinariaRecursiva(lista, llave, 0, len(lista)-1)
    if(b != -1):
        print("El indice es: ", b, "\nY el elemento es: ", lista[b])
    else:
        print("Elemento no encontrado")

main()
