def busquedaBinaria(A, x, p, r):
    if(p > r):
        return -1
    medio = int((p + r)/2)
    if(x == A[medio]):
        return medio
    else:
        if(x < A[medio]):
            return busquedaBinaria(A, x, p, medio-1)
        else:
            return busquedaBinaria(A, x, medio+1, r)

def main():
    print("Entrada: ")
    m = int(input())    
    P = [int(m) for m in input().split()]
    
    n = int(input())
    L = [int(n) for n in input().split()]
    
    print("\nSalida: ")
    for i in range(n):
        print(busquedaBinaria(P, L[i], 0, m-1) + 1, end = " ")
    
main()
