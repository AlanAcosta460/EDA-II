def bubbleSort(A):
	print("\n")
	print("Lista original:")
	print(A)
	print("\n")
	for i in range(1, len(A)):
		print("\n")
		print(f"Pasada {i}")
		print(A)
		for j in range(len(A)-1, 0, -1):
			if A[j] < A[j-1]:
				temp = A[j]
				A[j] = A[j-1]
				A[j-1] = temp
			print(A)
lista = [8, 20, 2, 39, 11, 34, 22, 5, 2, 0]

bubbleSort(lista)