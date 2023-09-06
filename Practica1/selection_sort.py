def SelectionSort(A, n):
    print(f"Lista original {A}")
    for i in range(0, n):
        print(f"Pasada {i}\n{A}")
        min = i
        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j
        print(f"Elemento minimo seleccionado {A[min]}")
        A[i], A[min] = A[min], A[i] 
        print(f"\t{A}")

lista = [12, 9, 3, 7, 14, 11]
SelectionSort(lista, len(lista))