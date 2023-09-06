def bubbleSortM(B):
	print("\n")
	print("Lista original:")
	print(B)
	print("\n")
	bandera = True
	pasada = 0
	i = 1
	while pasada < len(B) and bandera:
		print("\n")
		print(f"Pasada {i}")
		print(B)
		bandera = False
		for j in range(len(B)-1-pasada):
			print(B)
			if (B[j] > B[j+1]):
				bandera = True
				temp = B[j]
				B[j] = B[j+1]
				B[j+1] = temp
		pasada = pasada+1
		i = i +1

lista1 = [8, 20, 2, 39, 11, 34, 22, 5, 2, 0]
lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubbleSortM(lista1)
bubbleSortM(lista2)