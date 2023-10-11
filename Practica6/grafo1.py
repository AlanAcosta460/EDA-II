class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = []
        
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()     
        
class Grafo:
    def __init__(self, tipo):
        self.vertices = {}
        self.tipo = tipo
        
    def agregarVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)
            
    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            if self.tipo == 1:
                self.vertices[u].agregarVecino(v)
            else:
                self.vertices[u].agregarVecino(v)
                self.vertices[v].agregarVecino(u)
                
    def imprimirGrafo(self):
        for v in self.vertices:
            print(v, self.vertices[v].vecinos)     

def controladora():
    g = Grafo(0)
    v = ["r", "s", "t", "u", "v", "w", "x", "y"]
    a = [["v", "r"], ["r", "s"], ["s", "w"], ["w", "t"], ["w", "x"], ["t", "x"], ["t", "u"], ["x", "u"], ["x", "y"], ["u", "y"]]
   
    for i in v:
        g.agregarVertice(i)
        
    for i in a:
        g.agregarArista(i[0], i[1])
    
    g.imprimirGrafo()
    
controladora()    
    