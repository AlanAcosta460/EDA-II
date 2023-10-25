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
    
    def preOrden(self, nodo):
        if nodo != None:
            print(nodo.valor)
            self.preOrden(nodo.hijoIzq)
            self.preOrden(nodo.hijoDer)
    
    def postOrden(self, nodo):
        if nodo != None:
            self.postOrden(nodo.hijoIzq)
            self.postOrden(nodo.hijoDer)
            print(nodo.valor)
            
    def inOrden(self, nodo):
        if nodo != None:
            self.inOrden(nodo.hijoIzq)
            print(nodo.valor)
            self.inOrden(nodo.hijoDer)

def controladora():
    arbol = Arbol()
    nodos = [10, 3, 2, 18, 7, 12, 7, 4, 20, 0]
    
    for n in nodos:
        arbol.insertar(n)
        
    print("Recorrido PreOrden")
    arbol.preOrden(arbol.raiz)
    
    print("\nRecorrido PostOrden")
    arbol.postOrden(arbol.raiz)
    
    print("\nRecorrido InOrden")
    arbol.inOrden(arbol.raiz)
                
controladora()
