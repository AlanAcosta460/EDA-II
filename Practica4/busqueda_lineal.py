def busquedaLineal(A, n, x):
    encontrado = -1
    for k in range(0, n-1, n):
        if(x == A[k]):
            encontrado = k
    return encontrado

def busquedaLinealMejorado1(A, n, x):
    encontrado = -1
    for k in range(0, n-1, n):
        if(x == A[k]):
            encontrado = k
            break
    return encontrado

def busquedaLinealCentinela(A, n, x):
    tmp = A[n-1]
    k = 0
    while(A[k] != x):
        k += 1
    A[n-1] = tmp
    if(k < n-1 or A[n-1] == x):
        return k
    else:
        return -1

def busquedaLinealMejorado2(A, n, x):
    i = 0
    while(A[i] != x and i < n):
        i = i+1
    if(A[i] == x):
        return i
    else:
        return -1

def busquedaLinealRecursiva(A, x, ini, fin):
    if(ini > fin):
        return -1
    else:
        if(A[ini] == x):
            return ini
        else:
            return busquedaLinealRecursiva(A, x, ini+1, fin)

def main():
    lista = [23,6,4,3,6,31,12,89,6,78,54,19]
    print("La lista es: ", lista)
    llave = 6
    print("La llave es: ", llave)

    print("\nBUSQUEDA LNIEAL")
    a = busquedaLineal(lista, len(lista), llave)
    print("El indice es: ", a, "\nT el elemento es: ", lista[a])

    print("\nBUSQUEDA LINEAL MEJORADA 1")
    b = busquedaLinealMejorado1(lista, len(lista), llave)
    print("El indice es: ", b, "\nT el elemento es: ", lista[b])

    print("\nBUSQUEDA LINEAL CENTINELA")
    c = busquedaLinealCentinela(lista, len(lista), llave)
    print("El indice es: ", c, "\nT el elemento es: ", lista[c])

    print("\nBUSQUEDA LINEAL MEJORADA 2")
    d = busquedaLinealMejorado2(lista, len(lista), llave)
    print("El indice es: ", d, "\nT el elemento es: ", lista[d])
    
    print("\nBUSQUEDA LINEAL RECURSIVA")
    e = busquedaLinealRecursiva(lista, llave, 0, len(lista))
    print("El indice es: ", e, "\nT el elemento es: ", lista[e])

main()
