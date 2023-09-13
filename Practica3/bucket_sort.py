def bucket_sort(A):
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        elementosbuckets = int(n * A[i])
        B[elementosbuckets].append(A[i])
   
    for i in range(n):
        B[i].sort()

    A_Ordenado = []
    for bucket in B:
       A_Ordenado.extend(bucket)

    return A_Ordenado

A = [0.78, 0.17, 0.39, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

print("Buckets antes de ordenar:")
for i in range(len(A)):
    elementosbuckets = int(len(A) * A[i])
    print(f"Bucket {elementosbuckets}: {A[i]}")

A_Ordenado = bucket_sort(A)

print("\nBuckets después de ordenar:")
for i in range(len(A_Ordenado)):
    elementosbuckets = int(len(A_Ordenado) * A_Ordenado[i])
    print(f"Bucket {elementosbuckets}: {A_Ordenado[i]}")

print("\nSecuencia ordenada:")
print(A_Ordenado)
