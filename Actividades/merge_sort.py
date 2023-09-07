def Merge(A, p, q, r):
    izq = A[p:(q + 1)]
    der = A[q + 1:(r + 1)]
    print("Izquierda: ", izq)
    print("Derecha: ", der)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if (j >= len(der)) or (i < len(izq) and izq[i] < der[j]):
            A[k] = izq[i]
            i = i + 1
        else:
            A[k] = der[j]
            j = j + 1
    print("Combinacion: ", A, "\n")
    

def MergeS(A, p, r):
    if(p < r):
        q = int((p + r) / 2) 
        MergeS(A, p, q)
        MergeS(A, q + 1, r)
        Merge(A, p, q, r)
        
        
A = [8,20,2,39,11,34,22,5,2,0]
print("Lista Original\n", A)
MergeS(A, 0, 9)

B = [10,9,8,7,6,5,4,3,2,1]
print("\nLista Original\n", B)
MergeS(B, 0, 9)
