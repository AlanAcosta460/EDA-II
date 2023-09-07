def bubbleSortMejorado(A, n):
    bandera = True
    pasada = 0
    while pasada < n and bandera:
        bandera = False
        print(f"\nPasada {pasada + 1}")
        print(A)
        for j in range (0, n - pasada - 1):
            print(A)
            if A[j] > A[j + 1]:
                bandera = True
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp
        pasada += 1

print("Lista 1")
A = [8,20,2,39,11,34,22,5,2,0]
bubbleSortMejorado(A, 10)

print("\nLista 2")
B = [10,9,8,7,6,5,4,3,2,1]
bubbleSortMejorado(B, 10)