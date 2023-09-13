def bubble_sort(lista):
  print("\nOrdenamiento:\n")
  for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
      if lista[i] > lista[j]:
        lista[i], lista[j] = lista[j], lista[i]
        print(lista)

lista = ['XI7FS6', 'PL4ZQ2', 'JI8FR9', 'XL8FQ6', 'PY2ZR5', 'KV7WS9', 'JL2ZV3', 'KI4WR2']

print("Array desordenado: ", lista)

bubble_sort(lista)

print("\nArray ordenado: ", lista)