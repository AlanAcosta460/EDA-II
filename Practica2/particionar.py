def intercambia(A, x, y):
    A[x], A[y] = A[y], A[x] 

def Particionar(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            intercambia(A, i, j)
        print(A)
    intercambia(A, i + 1, r) 
    print(A)
    return i + 1
    
lista = [2, 8, 7, 1, 3, 5, 6, 4]
print(f"Lista original: {lista}")
print("\nLista particionada: ")
Particionar(lista, 0, len(lista) - 1)