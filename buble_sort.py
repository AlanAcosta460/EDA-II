def bubbleSortSinMejora(A, n):
    for i in range(1, n):
        for j in range (0, n-1):
            print(A)
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

A = [8,20,2,39,11,34,22,5,2,0]
print("Lista Original\n", A)
bubbleSortSinMejora(A, 10)

B = [10,9,8,7,6,5,4,3,2,1]
print("Lista Original\n", B)
bubbleSortSinMejora(B, 10)
