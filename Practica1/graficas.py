import matplotlib.pyplot as plt
import random
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

def bubbleSortM(B):
	bandera = True
	pasada = 0
	i = 1
	while pasada < len(B) and bandera:
		bandera = False
		for j in range(len(B)-1-pasada):
			if (B[j] > B[j+1]):
				bandera = True
				temp = B[j]
				B[j] = B[j+1]
				B[j+1] = temp
		pasada = pasada+1
		i = i +1

def InsertionSort(A, n):
    for j in range(1, n):
        llave = A[j]
        i = j-1
        while i >= 0 and A[i] > llave:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = llave

def SelectionSort(A, n):
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i] 

def graficas():
    # Merge Sort
    TM = []
    nD = [k*100 for k in range(1, 31)]
    for k in nD:
        datosM = random.sample(range(1, 100000000), k)
        t0 = time()
        MergeSort(datosM, 0, len(datosM)-1)
        t1 = time()
        TM.append(round(t1-t0, 6))
    
    # Buble Sort Mejorado
    TB = []
    for k in nD:
        datosB = random.sample(range(1, 100000000), k)
        t0 = time()
        bubbleSortM(datosB)
        t1 = time()
        TB.append(round(t1-t0, 6))

    # Insertion Sort
    TI = []
    for k in nD:
        datosI = random.sample(range(1, 100000000), k)
        t0 = time()
        InsertionSort(datosI, len(datosI))
        t1 = time()
        TI.append(round(t1-t0, 6))
    
    # Selection Sort
    TS = []
    for k in nD:
        datosS = random.sample(range(1, 100000000), k)
        t0 = time()
        SelectionSort(datosS, len(datosS))
        t1 = time()
        TS.append(round(t1-t0, 6))

    # Mostrar todas las graficas en una sola ventana
    fig, ax = plt.subplots()

    ax.plot(nD, TM, label="Merge Sort", marker = "*")
    ax.plot(nD, TB, label="Bubble Sort Mejorado", marker = "*")
    ax.plot(nD, TI, label="Insertion Sort", marker = "*")
    ax.plot(nD, TS, label="Selection Sort", marker = "*")

    ax.set_xlabel("n Datos")
    ax.set_ylabel("Tiempo")
    ax.set_title("n vs t(n)")
    
    ax.grid(True)
    ax.legend(loc=2)
    plt.show()

graficas()
