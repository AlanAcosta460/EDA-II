def InsertionSort(A, n):
    for j in range(1, n):
        llave = A[j]
        print(f"\nPasada {j} elemento a insertar {llave}")
        print(A)
        i = j-1
        while i >= 0 and A[i] > llave:
            A[i+1] = A[i]
            i = i-1
            print(A)
        A[i+1] = llave
        print(A)

lista = [12, 9, 3, 7, 14, 11]
InsertionSort(lista, len(lista))