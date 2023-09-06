def Particionar(A, p, r):
    x = A[p]
    i = p
    j = r
    print(f"\nPivote: [{x}]")
    while True:
        while A[j] > x:
            j -= 1
        while A[i] < x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            print(A[p:i + 1], end=" -- ")
            print(A[i + 1:r + 1])
            return j

def QuickSort(A, p, r):
    if p < r:
        q = Particionar(A, p, r)
        QuickSort(A, p, q)
        QuickSort(A, q + 1, r)

lista = [2, 8, 10, 7, 1, 3, 9, 5, 6, 4]
print("---Quick Sort Hoare---")
print(f"Lista original: {lista}")
QuickSort(lista, 0, 9)
print(f"\nLista ordenada: {lista}")