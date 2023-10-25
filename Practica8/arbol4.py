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
    
    def busqueda(self, nodo, valor):
        if nodo == None or valor == nodo.valor:
            return nodo
        
        if valor < nodo.valor:
            return self.busqueda(nodo.hijoIzq, valor)
        else:
            return self.busqueda(nodo.hijoDer, valor)
    
    def imprimeCamino(self, nodo):
        if nodo.padre != None:
            print(nodo.valor)
            self.imprimeCamino(nodo.padre)
        else:
            print(nodo.valor)
    
    def altura(self, nodo):
        if self.raiz == None or nodo == None:
            return 0
        else:
            altura = 1 + max(self.altura(nodo.hijoIzq), self.altura(nodo.hijoDer))
            return altura
    
    def minimo(self, nodo):
        while nodo.hijoIzq != None:
            nodo = nodo.hijoIzq
        return nodo
    
    def maximo(self, nodo):
        while nodo.hijoDer != None:
            nodo = nodo.hijoDer
        return nodo

def controladora():
    arbol = Arbol()
    nodos = [10, 3, 2, 18, 7, 12, 7, 4, 20, 0]
    
    for n in nodos:
        arbol.insertar(n)
    
    print("Camino de nodo 4 a la raiz:")
    arbol.imprimeCamino(arbol.busqueda(arbol.raiz, 4))
    
    print(f"Minimo del arbol: {arbol.minimo(arbol.raiz).valor}")
    print(f"Maximo del arbol: {arbol.maximo(arbol.raiz).valor}")
    print(f"Altura: {arbol.altura(arbol.raiz)}")
                
controladora()
