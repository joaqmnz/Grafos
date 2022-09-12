class Grafo:
    def __init__(self, qtd_vertices: int) -> None:
        self.grafo = []
        self.qtd_vertices = qtd_vertices
        self.init()
    
    def __str__(self) -> str:
        return str(self.grafo)
    
    def init(self) -> None:
        for _ in range(self.qtd_vertices):
            self.grafo.append([])
    
    def add_vertice(self) -> None:
        self.grafo.append([])
    
    def remove_vertice(self, vertices: str) -> None:
        vertices = vertices.split(',')
        for vertice in vertices:
            vertice = int(vertice) - 1
            if(0 <= vertice <= self.qtd_vertices):
                aux = []
                for i in range(self.qtd_vertices):
                    if [vertice, False] in self.grafo[i]:
                        self.grafo[i].remove([vertice, False])
                    if i == vertice:
                        continue
                    aux.append(self.grafo[i])
                self.grafo = aux

    def add_aresta(self, arestas: str) -> bool:
        arestas = arestas.split(',')
        for par in arestas:
            vertices = par.split(' ')
            string = f'{vertices[1]} {vertices[0]}'
            if string in arestas:
                arestas.remove(string)
        cont = 0
        for aresta in arestas:
            vertices = aresta.split(' ')
            v1 = int(vertices[0]) - 1
            v2 = int(vertices[1]) - 1
            if(0 <= v1 <= self.qtd_vertices) and (0 <= v2 <= self.qtd_vertices):
                self.grafo[v1].append([v2, False])
                self.grafo[v2].append([v1, False])
                cont += 1
        return (cont == len(arestas))
    
    def remove_aresta(self, arestas: str) -> bool:
        arestas = arestas.split(',')
        for aresta in arestas:
            vertices = aresta.split(' ')
            v1 = int(vertices[0]) - 1
            v2 = int(vertices[1]) - 1
            if(0 <= v1 <= self.qtd_vertices) and (0 <= v2 <= self.qtd_vertices):
                self.grafo[v1].remove([v2, False])
                self.grafo[v2].remove([v1, False])
                cont += 1
        return (cont == len(arestas))
    
    def grau(self, vertice: int) -> int:
        vertice -= 1
        if(0 <= vertice <= self.qtd_vertices):
            return len(self.grafo[vertice])
        else:
            return -1
    
    def vizinhos(self, vertices: str) -> bool:
        vertices = vertices.split(',')
        vertices[0] = int(vertices[0]) - 1
        vertices[1] = int(vertices[1]) - 1
        if(0 <= vertices[0] <= self.qtd_vertices) and (0 <= vertices[1] <= self.qtd_vertices):
            return ([vertices[1], False] in self.grafo[vertices[0]]) and ([vertices[0], False] in self.grafo[vertices[1]])
        else:
            return False

    def e_euleriano(self) -> bool:
        graus = []
        for i in range(len(self.grafo)):
            graus.append(self.grau(i+1))
        for grau in graus:
            if not grau % 2 == 0:
                return False
        return True

    def hierholzer_aux(self, j: int, s: list, t: list) -> list:
        for aresta in self.grafo[j]:
            if not aresta[1]:
                s.append(aresta[0])
                aresta[1] = True
                for incidencia in self.grafo[aresta[0]]:
                    if incidencia[0] == j:
                        incidencia[1] = True
                self.hierholzer_aux(aresta[0], s, t)
        t.append(s.pop())
        if not s:
            return t

    def hierholzer(self) -> list:
        s, t = [], []
        s.append(0)
        return self.hierholzer_aux(0, s, t)
