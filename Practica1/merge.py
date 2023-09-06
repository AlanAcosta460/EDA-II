def MergeSort(C, p, r):
    if(p < r):
        q = int((p+r)/2)
        MergeSort(C, p, q)
        MergeSort(C, q+1, r)
        Merge(C, p, q, r)

def Merge(C, p, q, r):
	izq = C[p:(q+1)]
	der = C[q+1:(r+1)]
	print("Izquierda: ",izq)
	print("Derecha: ", der)
	i = 0
	j = 0
	for k in range(p, r+1):
		if(j >= len(der) or (i < len(izq) and izq[i] > der[j])):
			C[k] = izq[i]
			i = i+1
		else:
			C[k] = der[j]
			j = j+1
	print("Combinacion: ", C)
	print("\n")

lista = [8,20,2,39,11,34,22,5,2,0]

print("Lista original:")
print(lista)
print("\n")

MergeSort(lista, 0, 9)