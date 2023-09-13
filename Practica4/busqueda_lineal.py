def BusquedaLineal(A,n,x):
    encontrado = -1
    for k in range(0, n-1):
        if x == A[k]:
            encontrado = k
    return encontrado

def BusquedaLinealMejorada1(A,n,x):
    encontrado = -1
    for k in range(0, n-1):
        if A[k] == x:
            encontrado = k
            break
    return encontrado

def BusquedaLinealCentinela(A,n,x):
    tmp = A[n-1]
    A[n-1] = x
    k = 0
    
    while A[k] != x:
        k += 1
        
    A[n-1] = tmp
    
    if k < n-1 or A[n-1] == x:
        return k
    else:
        return -1
    
def BusquedaLinealMejorada2(A,n,x):
    i = 0
    
    while A[i] != x and i < n:
        i += 1
    
    if A[i] == x:
        return i
    else: 
        return -1

def BusquedaLinealRecursiva(A,x,ini,fin):
    if ini > fin:
        encontrado = -1
    else:
        if A[ini] == x:
            return ini
        else:
            return BusquedaLinealRecursiva(A,x,ini+1,fin)

def main():
    llave = 6
    A = [23,6,4,3,6,31,12,89,6,78,54,19]
    
    print('Búsqueda Lineal')
    i = BusquedaLineal(A,len(A),llave)
    print(f'Indice: {i} \tElemento: {A[i]}')
    
    print('\nBúsqueda Lineal Mejorada 1')
    i = BusquedaLinealMejorada1(A,len(A),llave)
    print(f'Indice: {i} \tElemento: {A[i]}')
    
    print('\nBúsqueda Lineal Con Centinela')
    i = BusquedaLinealCentinela(A,len(A),llave)
    print(f'Indice: {i} \tElemento: {A[i]}')
    
    print('\nBúsqueda Lineal Mejorada 2')
    i = BusquedaLinealMejorada2(A,len(A),llave)
    print(f'Indice: {i} \tElemento: {A[i]}')
    
    print('\nBúsqueda Lineal Recursiva')
    i = BusquedaLinealRecursiva(A,llave,0,len(A)-1)
    print(f'Indice: {i} \tElemento: {A[i]}')

main()