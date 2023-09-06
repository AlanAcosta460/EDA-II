import math

def hIzq(i):
    return 2*i+1

def hDer(i):
    return 2*i+2

def intercambiar(A, x, y):
    A[x], A[y] = A[y], A[x]
    
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

lista = [15, 19, 4, 2, 17, 14, 12, 7, 5, 16, 20, 8, 18, 1, 13, 9, 3, 6, 10, 11]
print("---Heap Sort---")
print(f"Lista original: {lista}")
OrdenacionHeapSort(lista, len(lista))
print(f"\nLista ordenada: {lista}")
