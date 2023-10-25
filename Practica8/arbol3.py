class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.padre = None
        self.valor = valor
        
class Arbol:
    def __init__(self):
        self.raiz = None
    
    def obtenerRaiz(self):
        return self.raiz
    
    def insertar(self, valor):
        if(self.raiz == None):
            self.raiz = Nodo(valor)
        else:
            self.agregarNodo(valor, self.raiz)
    
    def agregarNodo(self, valor, nodoActual):
        if valor < nodoActual.valor:
            if nodoActual.hijoIzq != None:
                self.agregarNodo(valor, nodoActual.hijoIzq)
            else:
                nodoNuevo = Nodo(valor)
                nodoActual.hijoIzq = nodoNuevo
                nodoActual.hijoIzq.padre = nodoActual
        else:
            if nodoActual.hijoDer != None:
                self.agregarNodo(valor, nodoActual.hijoDer)
            else:
                nodoNuevo = Nodo(valor)
                nodoActual.hijoDer = nodoNuevo
                nodoActual.hijoDer.padre = nodoActual
    
    def busquedaIter(self, nodo, valor):
        while nodo != None and valor != nodo.valor:
            if valor < nodo.valor:
                nodo = nodo.hijoIzq
            else:
                nodo = nodo.hijoDer
        return nodo

def controladora():
    arbol = Arbol()
    nodos = [10, 3, 2, 18, 7, 12, 7, 4, 20, 0]
    
    for n in nodos:
        arbol.insertar(n)
    
    print("Se buscaran las llaves 3, 100, 20")
    
    valor = 3
    print(f"Se busca {valor}")
    if arbol.busquedaIter(arbol.raiz, valor) != None:
        print(f"Se encontro un nodo cuyo atributo es {valor}")
    else: 
        print("No se encuentra el valor")
        
    valor = 100
    print(f"\nSe busca {valor}")
    if arbol.busquedaIter(arbol.raiz, valor) != None:
        print(f"Se encontro un nodo cuyo atributo es {valor}")
    else: 
        print("No se encuentra el valor")
        
    valor = 20
    print(f"\nSe busca {valor}")
    if arbol.busquedaIter(arbol.raiz, valor) != None:
        print(f"Se encontro un nodo cuyo atributo es {valor}")
    else: 
        print("No se encuentra el valor")
                
controladora()
