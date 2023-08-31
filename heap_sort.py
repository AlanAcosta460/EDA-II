import math

def hIzq(i):
    return 2*i+1

def hDer(i):
    return 2*i+2

def intercambiar(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
    
def MaxHeapify(A, i, tamanoHeap):
    L = hIzq(i)
    R = hDer(i)
    if (L <= (tamanoHeap-1) and A[L] > A[i]):
        posMax = L
    else:
        posMax = i
    if (R <= (tamanoHeap-1) and A[R] > A[posMax]):
        posMax = R
    if (posMax != i):
        intercambiar(A, i, posMax)
        MaxHeapify(A, posMax, tamanoHeap)
        
def construirHeapMaxIni(A, tamanoHeap):
    for i in range(math.ceil((tamanoHeap-1)/2), -1, -1):
        MaxHeapify(A, i, tamanoHeap)
        
def OrdenacionHeapSort(A, tamanoHeap):
    construirHeapMaxIni(A, tamanoHeap)
    print("\nEmpieza ordenamiento\n")
    for i in range(len(A)-1, 0, -1):
        print("Intercambio: ", A[0], "con", A[i])
        intercambiar(A, 0, i)
        print("\nElemento", A[i], "ordenado")
        tamanoHeap = tamanoHeap-1
        MaxHeapify(A, 0, tamanoHeap)
        print("\nReconstruccion del Heap Max: ", A[0:tamanoHeap])

lista = [11, 16, 2, 8, 20, 13, 7, 18, 10, 15, 12, 1, 17, 3, 9, 5, 6, 19, 4, 14]

print("*** Heap Sort ***")

OrdenacionHeapSort(lista, len(lista))

print(f"\nLista ordenada: \n{lista}")