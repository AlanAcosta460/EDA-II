import matplotlib.pyplot as plt
import random
import math
from time import time

def MergeSort(C, p, r):
    if(p < r):
        q = int((p+r)/2)
        MergeSort(C, p, q)
        MergeSort(C, q+1, r)
        Merge(C, p, q, r)

def Merge(C, p, q, r):
	izq = C[p:(q+1)]
	der = C[q+1:(r+1)]
	i = 0
	j = 0
	for k in range(p, r+1):
		if(j >= len(der) or (i < len(izq) and izq[i] > der[j])):
			C[k] = izq[i]
			i = i+1
		else:
			C[k] = der[j]
			j = j+1

def Intercambiar(A, x, y):
    A[x], A[y] = A[y], A[x]

def Particionar(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            Intercambiar(A, i, j)
    Intercambiar(A, i + 1, r)
    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = Particionar(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def hIzq(i):
    return 2*i+1

def hDer(i):
    return 2*i+2

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
        Intercambiar(A, i, posMax)
        MaxHeapify(A, posMax, tamanoHeap)
        
def construirHeapMaxIni(A, tamanoHeap):
    for i in range(math.ceil((tamanoHeap-1)/2), -1, -1):
        MaxHeapify(A, i, tamanoHeap)
        
def OrdenacionHeapSort(A, tamanoHeap):
    construirHeapMaxIni(A, tamanoHeap)
    for i in range(len(A)-1, 0, -1):
        Intercambiar(A, 0, i)
        tamanoHeap = tamanoHeap-1
        MaxHeapify(A, 0, tamanoHeap)

def graficas():
    # Quick Sort
    TQ = []
    nD = [k*100 for k in range(1, 31)]
    for k in nD:
        datosQ = random.sample(range(1, 100000000), k)
        t0 = time()
        QuickSort(datosQ, 0, len(datosQ)-1)
        t1 = time()
        TQ.append(round(t1-t0, 6))
    
    # Heap Sort
    TH = []
    for k in nD:
        datosH = random.sample(range(1, 100000000), k)
        t0 = time()
        OrdenacionHeapSort(datosH, len(datosH))
        t1 = time()
        TH.append(round(t1-t0, 6))
    
    # Merge Sort
    TM = []
    for k in nD:
        datosM = random.sample(range(1, 100000000), k)
        t0 = time()
        MergeSort(datosM, 0, len(datosM)-1)
        t1 = time()
        TM.append(round(t1-t0, 6)) 

    # Mostrar todas las graficas en una sola ventana
    fig, ax = plt.subplots()

    ax.plot(nD, TM, label="Merge Sort", marker = "*")
    ax.plot(nD, TQ, label="Quick Sort", marker = "*")
    ax.plot(nD, TH, label="Heap Sort", marker = "*")

    ax.set_xlabel("n Datos")
    ax.set_ylabel("Tiempo")
    ax.set_title("n vs t(n)")
    
    ax.grid(True)
    ax.legend(loc=2)
    plt.show()

graficas()
