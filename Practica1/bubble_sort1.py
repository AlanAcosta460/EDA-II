def bubbleSort(A):
    print("Lista original")
    print(A)
    for i in range(1, len(A)):
        print("\n")
        print(f"Pasada {i}")
        print(A)
        for j in range(len(A) - 1):
            print(A)
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

lista1 = [8, 20, 2, 39, 11, 34, 22, 5, 2, 0]
lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubbleSort(lista1)
bubbleSort(lista2)