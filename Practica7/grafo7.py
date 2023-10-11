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
        self.ordenT = []
        
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
        self.ordenT.insert(0, u.nombre)
        
    def dfsImprimir(self):
        for v in self.vertices:
            print(f"Vertice {v}. Descubrimeinto/Termino: {self.vertices[v].d}/{self.vertices[v].f}. Predecesor: {self.vertices[v].predNombre}")

    def componentesFuertementeConexas(sellf):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return a
    
def controladora():
    g1 = Grafo(0)
    v1 = ["a", "b", "c", "d", "e", "f", "g", "h"]
    a1 = [["a", "b"], ["b", "c"], ["b", "f"], ["b", "e"], ["e", "a"], 
        ["e", "f"], ["c", "d"], ["d", "c"], ["c", "g"], ["f", "g"], 
        ["g", "f"], ["d", "h"], ["g", "h"], ["h", "h"]]

    for i in v1:
        g1.agregarVertice(i)
    
    for i in range(len(a1)):
        g1.agregarArista(a1[i][0], a1[i][1])

    g1.imprimirGrafo()
    g1.dfs()
    g1.dfsImprimir()
    print("Orden topologico:", g1.ordenT, "\n")

    g2 = Grafo(0)
    v2 = g1.ordenT
    a2 = [["b", "a"], ["c", "b"], ["f", "b"], ["e", "b"], ["a", "e"], 
        ["f", "e"], ["d", "c"], ["c", "d"], ["g", "c"], ["g", "f"], 
        ["f", "g"], ["h", "d"], ["h", "g"], ["h", "h"]]

    for i in v2:
        g2.agregarVertice(i)
    
    for i in range(len(a2)):
        g2.agregarArista(a2[i][0], a2[i][1])

    g2.imprimirGrafo()
    g2.dfs()
    g2.dfsImprimir()
    print("Orden topologico:", g2.ordenT, "\n")

    lista = g2.componentesFuertementeConexas()

    print("Componentes fuertemente conexas:", lista)


controladora()
