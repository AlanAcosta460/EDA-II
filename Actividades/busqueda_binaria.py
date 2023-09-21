import random

def BusquedaBinariaIterativa(A,x,indiceIzq, indiceDer):
    while indiceIzq <= indiceDer:
        medio = int((indiceIzq+indiceDer)/2)
        if x == A[medio]:
            return medio
        else:
            if A[medio] < x:
                indiceIzq = medio+1
            else:
                indiceDer = medio-1
    return -1

def BusquedaBinariaRecursiva(A,x,indiceIzq,indiceDer):
    if indiceIzq > indiceDer:
        return -1
    else:
        medio = int((indiceIzq+indiceDer)/2)
        
        if x == A[medio]:
            return medio
        else:
            if x < A[medio]:
                return BusquedaBinariaRecursiva(A,x,indiceIzq,medio-1)
            else:
                return BusquedaBinariaRecursiva(A,x,medio+1,indiceDer)
            
def InsertionSort(A,n):
    for j in range(1,n):
        llave = A[j]
        i = j-1
        while i >= 0 and A[i] > llave:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = llave

def CrearListaRandom():
    lista = [0] * 20
    for i in range(20):
        lista[i] = random.randint(1,20)
    return lista

def main():
    A = CrearListaRandom()
    llave = random.randint(1,20)
    
    print(f'Lista aleatoria desordenada: {A}')
    InsertionSort(A, len(A))
    print(f'Lista aleatoria ordenada: {A}')
    print(f'Llave: {llave}')
    
    print('\nBúsqueda Binaria Iterativa')
    i = BusquedaBinariaIterativa(A,llave,0,len(A)-1)
    if i != -1:
        print(f'Indice: {i} \tElemento: {A[i]}')
    else: 
        print("Elemento no encontrado")
    
    print('\nBúsqueda Binaria Recursiva')
    i = BusquedaBinariaRecursiva(A,llave,0,len(A)-1)
    if i != -1:
        print(f'Indice: {i} \tElemento: {A[i]}')
    else: 
        print("Elemento no encontrado")
    
main()