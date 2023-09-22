import random

def countingSort(A, k):
    print(f"Los valores a ordenar son\n{A}\n")
    
    C = [0 for i in range(k + 1)]
    B = [0 for i in range(len(A))]
    
    print(f"La lista C inicializada es\n{C}")
    
    for j in range(len(A)):
        C[A[j]] += 1
    
    print("La lista C que indica cuantos elemenos hay de cada clase:")
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
        
    print("\nLa lista C que indica Al final:")
    for j in range(0, k + 1):
        print(f"{j} - {C[j]}")
        
    return B

lista = [0]  * 20
for i in range(20):
    lista[i] = random.randint(0, 15)
    
listaOrdenada = countingSort(lista, 15)
print(listaOrdenada)