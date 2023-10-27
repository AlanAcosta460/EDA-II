class Nodo:
    def __init__(self,t):
        self.hijos = list()
        self.llaves = list()
        self.hoja=1
        self.n=0
        for k in range(2*t):
            self.llaves.append([None])
        for k in range(2*t+1):
            self.hijos.append([None])

class ArbolB:
    def __init__(self,gradoMinimo):
        self.t= gradoMinimo
        self.raiz = None
    
    def bTreeCreate(self):
        if(self.raiz == None):
            self.raiz = Nodo(self.t)
        return self.raiz
            
    def bTreeInsert(self,nodo, k):
        r=self.raiz
        if r.n == 2*self.t-1:
            s=Nodo(self.t)
            self.raiz=s
            s.hoja=0
            s.n=0
            s.hijos[1]=r
            self.bTreeSplitShild(s,1)
            self.bTreeInsertNonFull(s,k)   
        else:
            self.bTreeInsertNonFull(r,k)
    
    def bTreeSplitShild(self,x,i):
        z=Nodo(self.t)
        y = x.hijos[i]
        z.hoja=y.hoja
        z.n=self.t-1 
        for j in range(1,self.t):
            z.llaves[j]=y.llaves[j+self.t]
            y.llaves[j+self.t]=None    
        if y.hoja==0:
            for j in range(1,self.t+1):
                z.hijos[j]=y.hijos[j+self.t]
                y.hijos[j+self.t]=None
        y.n=self.t-1
        for j in range(x.n+1,i,-1):
            x.hijos[j+1]=x.hijos[j]
        x.hijos[i+1]=z
        for j in range (x.n,i-1,-1):
            x.llaves[j+1]=x.llaves[j]
        x.llaves[i]=y.llaves[self.t]
        y.llaves[self.t]=None
        x.n=x.n+1
        
    def bTreeInsertNonFull(self,x,k):
        i=x.n
        if x.hoja == 1:
            while ( i >= 1) and (k < x.llaves[i]):
                x.llaves[i+1]= x.llaves[i]
                i=i-1
            x.llaves[i+1]=k
            x.n=x.n+1
            print ("llave insertada", k)
        else:
            while (i >= 1) and (k < x.llaves[i]):
                i=i-1
            i=i+1
            if x.hijos[i].n == 2*self.t-1:
                self.bTreeSplitShild(x,i)
                if k > x.llaves[i]:
                    i=i+1
            self.bTreeInsertNonFull(x.hijos[i],k)
            
    def imprimeNodo(self, nodo):
        for i in range(1, 2+self.t, 1):
            a = nodo.llaves[i]
            if(a != [None] and a != None):
                print(nodo.llaves[i], end = " ")
    
    def imprimeTree(self):
        self.imprimeNodo(self.raiz)
        print()
        for i in range (1, 4):
            self.imprimeNodo(self.raiz.hijos[i])
            print(end = "\t")
        print()
        for i in range (1, 4):
            self.imprimeNodo(self.raiz.hijos[1].hijos[i])
            print(end = "\t")
        print(end = "\t")
        for i in range (1, 3):
            self.imprimeNodo(self.raiz.hijos[2].hijos[i])
            print(end = "\t")
        print(end = "\t")
        for i in range (1, 3):
            self.imprimeNodo(self.raiz.hijos[3].hijos[i])
            print(end = "\t")    

    def encontrarMinimo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[1] 
        return nodo.llaves[1]

    def encontrarMaximo(self):
        if self.raiz is None:
            return None
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[nodo.n + 1] 
        return nodo.llaves[nodo.n]

def controladora():
    BT = ArbolB(2)    
    actual = BT.bTreeCreate()
    
    lista = ['B','T','H','M','O','C',
             'Z','G','L','E','N','P',
             'R','D','J','Q','F','W','X']
    
    print("Insercion")
    for n in lista: 
        BT.bTreeInsert(actual, n)
        
    print("\nImpresion")
    BT.imprimeTree()
    
    print("\n\nMinimo")
    print(BT.encontrarMinimo())

    print("\nMaximo")
    print(BT.encontrarMaximo())
    
controladora()
