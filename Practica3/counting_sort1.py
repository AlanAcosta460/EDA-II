import random

def countingSort(A, k):
    C = [0 for i in range(k + 1)]
    B = [0 for i in range(len(A))]
    
    print(f"La lista C inicializada es\n{C}")
    
    for j in range(len(A)):
        C[A[j]] += 1
    
    print("La lista C que indica cuantos elementos hay de cada clase:")
    for j in range(0, k + 1):
        print(f"{j} - {C[j]}")
        
    for j in range(1, k + 1):
        C[j] += C[j - 1]
        
    print("\nLa lista C que indica cuantos son menores o iguales:")
    for j in range(0, k + 1):
        print(f"{j} - {C[j]}")
        
    for j in range(len(A) -1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
        
    print("\nLa lista C que indica al final:")
    for j in range(0, k + 1):
        print(f"{j} - {C[j]}")
        
    return B

lista = [0]  * 20
for i in range(20):
    lista[i] = random.randint(0, 19)
    
print(f"Los valores a ordenar son: \n{lista}\n")
listaOrdenada = countingSort(lista, 19)
print(f"\nLa lista B que contienen los elementos ordenados: \n{listaOrdenada}")
