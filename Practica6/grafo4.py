class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.num_vertices = len(vertices)
        self.matriz_adyacencia = [[0] * self.num_vertices for _ in range(self.num_vertices)]

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            index_u = self.vertices.index(u)
            index_v = self.vertices.index(v)
            self.matriz_adyacencia[index_u][index_v] = 1
            self.matriz_adyacencia[index_v][index_u] = 1

    def imprimirGrafo(self):
        print(" ", end=" ")
        for vertice in self.vertices:
            print(vertice, end=" ")
        print()
        for i in range(self.num_vertices):
            print(self.vertices[i], end=" ")
            for j in range(self.num_vertices):
                print(self.matriz_adyacencia[i][j], end=" ")
            print()

def controladora():
    vertices = ["r", "s", "t", "u", "v", "w", "x", "y"]
    grafo = Grafo(vertices)

    grafo.agregarArista("v", "r")
    grafo.agregarArista("r", "s")
    grafo.agregarArista("s", "w")
    grafo.agregarArista("w", "t")
    grafo.agregarArista("w", "x")
    grafo.agregarArista("t", "x")
    grafo.agregarArista("t", "u")
    grafo.agregarArista("x", "u")
    grafo.agregarArista("x", "y")
    grafo.agregarArista("u", "y")

    grafo.imprimirGrafo()

controladora()
