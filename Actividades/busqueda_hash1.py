def insertar(T,m,x,valor):
    j = 0
    h1 = h(convertirLlave(x), m)
    while(j < m):
        indice = (h1 + j) % m
        par = [x, valor]
        if(T[indice] == None):
            T[indice] = par
            return indice
        else:
            j += 1
    print("\nNo hay lugar o la llave esta repetida")
    return -1

def formarTabla(m):
    T = [None] * m
    return T

def convertirLlave(x):
    keyNum = 0 # Llave a formar con el RFC
    i = 0 # Iterador
    
    # Ciclo que pasa por cada caracter del RFC
    for char in x:
        keyNum += ord(char) * i # Convertir cada caracter a UNICODE y multiplicarlo por el iterador i
        i += 1 # Incrementar el iterador

    return keyNum # Llave unica de cada RFC

def h(x, m):
    return x % m

def main():
    tabla = formarTabla(11);
    
    for i in range(0,6):
        print("\nPersona ", i + 1)
        rfc = input("RFC: ")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        salario = input("Salario: ")
        
        valor = nombre + ", " + edad + ", " + salario
        
        insertar(tabla, 11, rfc, valor)
        
    print("Tabla Hash\n", tabla)
        
main()
