from Grafos import Grafos

grafos = Grafos()

grafos.add_grafo(8)
grafos.add_grafo(10)
grafos.add_grafo(15)
grafos.add_grafo(8)

grafos.add_arestas(0, '1 7,1 2,2 6,3 7,3 8,3 5,4 5,4 8,4 6,5 8,6 8')
grafos.add_arestas(1, '1 2,1 9,1 3,1 7,2 6,3 7,3 8,3 5,4 5,4 8,5 8,5 6,6 10,6 8,9 10')
grafos.add_arestas(2, '1 3,1 7,1 8,1 5,1 15,2 7,2 3,4 8,4 5,6 11,6 14,7 12,9 13,10 11,11 15,13 14')
grafos.add_arestas(3, '1 2,1 7,1 8,1 6,2 8,2 6,2 5,3 7,3 8,3 4,3 5,4 8,4 6,4 5,5 8,6 8')

# grafos.e_euleriano(0)
# grafos.e_euleriano(1)
# grafos.e_euleriano(2)
# grafos.e_euleriano(3)

grafos.hierholzer(0)
grafos.hierholzer(1)
grafos.hierholzer(2)
grafos.hierholzer(3)

# grafos.remove_grafo(2)
# grafos.add_vertice(1, 5)
# grafos.remove_vertices(3, '1,3,2')
# grafos.remove_arestas(3, '2 8,3 4')
# grafos.grau(0, 2)
# grafos.vizinhos(0, '3,5')
