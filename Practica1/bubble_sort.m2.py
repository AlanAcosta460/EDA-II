def bubbleSortM(B):
	print("Lista original:")
	print(B)
	bandera = True
	pasada = 0
	i = 1
	while pasada < len(B) and bandera:
		print("\n")
		print(f"Pasada {i}")
		print(B)
		bandera = False
		for j in range(len(B)-1, 0, -1):
			if (B[j] < B[j-1]):
				bandera = True
				temp = B[j]
				B[j] = B[j-1]
				B[j-1] = temp
			print(B)
		pasada = pasada+1
		i = i +1

lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

bubbleSortM(lista)
