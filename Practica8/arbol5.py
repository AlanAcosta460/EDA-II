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
    
    def borrar(self, valor):
        if self.raiz == None:
            return False
        elif self.raiz.valor == valor:
            if self.raiz.hijoIzq == None and self.raiz.hijoDer == None:
                self.raiz = None
            elif self.raiz.hijoIzq == None:
                self.raiz = self.raiz.hijoDer
            elif self.raiz.hijoDer == None:
                self.raiz = self.raiz.hijoIzq
            else:
                self._borrar(valor, self.raiz)
        else:
            self._borrar(valor, self.raiz)
        
    def _borrar(self, valor, nodoActual):
        if valor < nodoActual.valor:
            if nodoActual.hijoIzq != None:
                self._borrar(valor, nodoActual.hijoIzq)
        elif valor > nodoActual.valor:
            if nodoActual.hijoDer != None:
                self._borrar(valor, nodoActual.hijoDer)
        else:
            if nodoActual.hijoIzq == None and nodoActual.hijoDer == None:
                self._reemplazarNodo(nodoActual, None)
            elif nodoActual.hijoIzq == None:
                self._reemplazarNodo(nodoActual, nodoActual.hijoDer)
            elif nodoActual.hijoDer == None:
                self._reemplazarNodo(nodoActual, nodoActual.hijoIzq)
            else:
                nodoReemplazo = self._obtenerNodoReemplazo(nodoActual)
                if nodoReemplazo != None:
                    self._borrar(nodoReemplazo.valor, nodoReemplazo)
                    nodoActual.valor = nodoReemplazo.valor
                    
    def _reemplazarNodo(self, nodoActual, nodoNuevo):
        if nodoActual.padre != None:
            if nodoActual == nodoActual.padre.hijoIzq:
                nodoActual.padre.hijoIzq = nodoNuevo
            else:
                nodoActual.padre.hijoDer = nodoNuevo
        if nodoNuevo != None:
            nodoNuevo.padre = nodoActual.padre
            
    def _obtenerNodoReemplazo(self, nodoActual):
        nodoReemplazo = None
        if nodoActual != None and nodoActual.hijoDer != None:
            nodoReemplazo = self._obtenerNodoMasIzq(nodoActual.hijoDer)
        return nodoReemplazo
    
    def _obtenerNodoMasIzq(self, nodoActual):
        if nodoActual.hijoIzq == None:
            return nodoActual
        else:
            return self._obtenerNodoMasIzq(nodoActual.hijoIzq)   

def controladora():
    arbol = Arbol()
    nodos = [10, 3, 2, 18, 7, 12, 7, 4, 20, 0]
    
    for n in nodos:
        arbol.insertar(n)
        
    print("Se borrara el nodo 3")
    arbol.borrar(3)

    print("Se borrara el nodo 10")
    arbol.borrar(10)

    print("Se borrara el nodo 18")
    arbol.borrar(18)

    print("\nRecorrido preorden del arbol resultante:")
    arbol.preOrden(arbol.obtenerRaiz())
                
controladora()
