import math

def hIzq(i):
    return 2 * i + 1

def hDer(i):
    return 2 * i + 2

def change(lista, x, y):
    lista[x], lista[y] = lista[y], lista[x]
    
def minHeapify(lista, i, heapSize):
    l = hIzq(i)
    r = hDer(i)
    if l < heapSize and lista[l] < lista[i]:
        smallest = l
    else:
        smallest = i
    if r < heapSize and lista[r] < lista[smallest]:
        smallest = r
    if smallest != i:
        change(lista, i, smallest)
        minHeapify(lista, smallest, heapSize)
        
def buildMinHeap(lista):
    heapSize = len(lista)
    for i in range(math.floor(len(lista)/2), -1, -1):
        minHeapify(lista, i, heapSize)

def heapSort(lista):
    buildMinHeap(lista)
    print("\nHeap Min Inicial: ", lista)
    heapSize = len(lista)
    print("\nEmpieza el ordenamiento: \n")
    for i in range(len(lista)-1, 0, -1):
        print("Intercambio: ", lista[0], "con", lista[i])
        change(lista, 0, i)
        print("\nElemento ", lista[i], "ordenado")
        heapSize = heapSize - 1
        minHeapify(lista, 0, heapSize)
        print("\nReconstruccion del Heap Min: ", lista[0:heapSize])
    
lista = [15, 19, 4, 2, 17, 14, 12, 7, 5, 16, 20, 8, 18, 1, 13, 9, 3, 6, 10, 11]
print("---Heap Sort---")
print(f"Lista original: {lista}")
heapSort(lista)
print(f"\nLista ordenada: {lista}")