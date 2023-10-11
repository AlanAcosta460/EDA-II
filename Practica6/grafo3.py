class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = []
        self.distancia = 9999
        self.pred = -1
        self.color = 'white'
        
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
            
    def bfs(self, vini):
        print("\nLa distancia del vertice " + vini.nombre)
        vini.distancia = 0
        vini.color = 'gris'
        vini.pred = None
        cola = []
        cola.append(vini.nombre)
        
        while(len(cola)) > 0:
            u = cola.pop()
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gris'
                    node_v.distancia = node_u.distancia+1
                    node_v.pred = node_u.nombre
                    cola.append(v)
            self.vertices[u].color = 'black'
            
    def imprimirBFS(self, v):
        if v.pred is not None:
            print("Al vertice " + v.nombre + " es de " + str(v.distancia) + " su predecesor es " + v.pred)
        else:
            print("Al vertice " + v.nombre + " es de " + str(v.distancia) + " su predecesor es None")

    def imprimirRuta(self, v, u):
        if v == u:
            print(v.nombre, end=" ")
        else:
            if u.pred == None:
                print("No hay ruta de " + v.nombre + " a " + u.nombre)
            else:
                self.imprimirRuta(v, self.vertices[u.pred])
                print(u.nombre, end=" ")
        
def controladora():
    g = Grafo(0)
    v = ["r", "s", "t", "u", "v", "w", "x", "y"]
    a = [["v", "r"], ["r", "s"], ["s", "w"], ["w", "t"], ["w", "x"], ["t", "x"], ["t", "u"], ["x", "u"], ["x", "y"], ["u", "y"]]
   
    for i in v:
        g.agregarVertice(i)
        
    for i in a:
        g.agregarArista(i[0], i[1])
    
    g.imprimirGrafo()
    
    g.bfs(g.vertices["s"])
    
    for v in g.vertices:
        g.imprimirBFS(g.vertices[v])
    
    print("\nRuta del vertice s al vertice v: ")
    g.imprimirRuta(g.vertices["s"], g.vertices["v"])

controladora()
