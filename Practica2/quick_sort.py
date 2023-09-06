def Intercambiar(A, x, y):
    A[x], A[y] = A[y], A[x]

def Particionar(A, p, r):
    x = A[r]
    i = p - 1
    print(f"\nPivote: [{x}]")
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            Intercambiar(A, i, j)
    Intercambiar(A, i + 1, r)
    print(A[p:i + 1], end=" -- ")
    print(A[i + 2:r + 1])
    return i + 1

def QuickSort(A, p, r):
    if p < r:
        q = Particionar(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

lista = [2, 8, 10, 7, 1, 3, 9, 5, 6, 4]
print("---Quick Sort---")
print(f"Lista original: {lista}")
QuickSort(lista, 0, 9)
print(f"\nLista ordenada: {lista}")