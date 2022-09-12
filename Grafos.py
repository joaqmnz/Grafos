from Grafo import Grafo

class Grafos:
    def __init__(self) -> None:
        self.grafos = []
    
    def add_grafo(self, vertices: int) -> None:
        grafo = Grafo(vertices)
        self.grafos.append(grafo)
    
    def remove_grafo(self, grafo: int) -> None:
        grafos_aux = []
        for i in range(len(self.grafos)):
            if i == grafo:
                continue
            grafos_aux.append(self.grafos[i])
        self.grafos = grafos_aux
    
    def add_vertices(self, grafo: int, qtd: int) -> None:
        for _ in range(qtd):
            self.grafos[grafo].add_vertice()
    
    def remove_vertices(self, grafo: int, vertices: str) -> None:
        self.grafos[grafo].remove_vertice(vertices)
    
    def add_arestas(self, grafo: int, arestas: str) -> None:
        if not self.grafos[grafo].add_aresta(arestas):
            print('Algo deu errado')
    
    def remove_arestas(self, grafo: int, arestas: str) -> None:
        if not self.grafos[grafo].remove_aresta(arestas):
            print('Algo deu errado')
    
    def grau(self, grafo: int, vertice: int) -> None:
        print(f'Grau: {self.grafos[grafo].grau(vertice)}')
    
    def vizinhos(self, grafo: int, vertices: str) -> None:
        if self.grafos[grafo].vizinhos(vertices):
            print('São vizinhos')
        else:
            print('Algo deu errado ou não são vizinhos')
    
    def e_euleriano(self, grafo: int) -> None:
        if self.grafos[grafo].e_euleriano():
            print('É Euleriano')
        else:
            print('Não é Euleriano')
    
    def hierholzer(self, grafo: int) -> None:
        if self.grafos[grafo].e_euleriano():
            cadeia = self.grafos[grafo].hierholzer()
            print(f'Cadeia: {cadeia}')
        else:
            print('Não é Euleriano, portanto não há cadeia')
    
    def mostrar_grafo(self, grafo: int) -> None:
        print(self.grafos[grafo])
