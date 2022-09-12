## Implementação 1 de Grafos e Algoritmos Computacionais

> Esta versão pode conter bugs e erros imprevistos ⚠️

#### Manual do código

1. Primeiramente, basta apenas fazer o import da classe *Grafos*:
> from Grafos import Grafos

2. Cria o objeto do tipo *Grafos*:
> g = Grafos()

3. Depois é necessário criar um grafo utilizando a função *add_grafo* e passando, como argumento, a quantidade de *vértices*:
> g.add_grafo(12)

4. Depois é necessário adicionar as *arestas* do grafo com a função *add_arestas*, passando dois argumentos. O primeiro
Deve ser a posição do grafo na lista (0 para o grafo 1, 1 para o grafo 2 etc) e o segundo deve ser uma **string** com o
Seguinte padrão:

> '1 7,1 2,2 6,3 7,3 8,3 5,4 5,4 8,4 6,5 8,6 8'

Informa os vértices, separando-os por espaço, e a *vírgula* serve para separar as *arestas*, ou seja, entre cada vírgula
Há uma aresta

> g.add_arestas(2, '1 7,1 2,2 6,3 7,3 8,3 5,4 5,4 8,4 6,5 8,6 8')

5. Com isso já pode utilizar as demais funções da classe *Grafos*, lembrando de sempre informar, como primeiro argumento
A posição do referido grafo

#### Lista de funções

1. Adicionar grafo
> add_grafo(vertices) -> vertices = número de vértices

2. Adicionar vértices
> add_vertices(grafo, qtd) -> grafo = posição do grafo | qtd = quantidade de vértices a serem inseridos

3. Adicionar arestas
> add_arestas(grafo, arestas) -> grafo = posição do grafo | arestas = arestas seguindo o padrão já informado

4. Remover grafo
> remove_grafo(grafo) -> grafo = posição do grafo

5. Remover vértices
> remove_vertices(grafo, vertices) -> grafo = posição do grafo | vertices = vértices a serem removidos, separados por vírgula

6. Remover arestas
> remove_arestas(grafo, arestas) -> grafo = posição do grafo | arestas = arestas a serem removidas, seguindo o mesmo padrão da adição

7. Grau de um vértice
> grau(grafo, vertice) -> grafo = posição do grafo | vertice = vértice do grafo

8. Saber se dois vértices são vizinhos
> vizinhos(grafo, vertices) -> grafo = posição do grafo | vertices = string contendo dois vértices separados por espaço

9. Saber se um grafo é Euleriano
> e_euleriano(grafo) -> grafo = posição do grafo

10. Determinar cadeia Euleriana com o algoritmo de Hierholzer
> hierholzer(grafo) -> grafo = posição do grafo

11. Imprimir na tela a lista do grafo
> mostrar_grafo(grafo) -> grafo = posição do grafo


## OBS:

*Alguns exemplos foram comentados, descomente-os para utilizá-los, caso queira.*
