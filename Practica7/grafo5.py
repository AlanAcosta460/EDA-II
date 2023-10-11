class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = []
        self.d = 0
        self.f = 0
        self.pred = -1
        self.predNombre = ""
        self.color = "white"
    
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

    def dfs(self):
        global tiempo
        tiempo = 0
        for u in self.vertices:
            if self.vertices[u].color == "white":
                self.dfsVisitar(self.vertices[u])

    def dfsVisitar(self, u):
        global tiempo
        tiempo += 1
        u.d = tiempo
        u.color = "gray"
        for v in u.vecinos:
            if self.vertices[v].color == "white":
                self.vertices[v].pred = u
                self.vertices[v].predNombre = u.nombre
                self.dfsVisitar(self.vertices[v])
        u.color = "black"
        tiempo += 1
        u.f = tiempo

    def dfsImprimir(self):
        for v in self.vertices:
            print(f"Vertice {v}. Descubrimeinto/Termino: {self.vertices[v].d}/{self.vertices[v].f}. Predecesor: {self.vertices[v].predNombre}")
    
def controladora():
    g1 = Grafo(1)
    v = ["u", "v", "w", "x", "y", "z"]

    for i in v:
        g1.agregarVertice(i)

    a = [["u", "v"], ["u", "x"], ["x", "v"], ["v", "y"], ["y", "x"], ["w", "y"], ["w", "z"], ["z", "z"]]
    
    for i in range(len(a)):
        g1.agregarArista(a[i][0], a[i][1])

    g1.imprimirGrafo()

    g1.dfs()

    g1.dfsImprimir()

controladora()
