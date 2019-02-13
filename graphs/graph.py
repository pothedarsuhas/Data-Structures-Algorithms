from queue import *

class VertexNotFound(Exception):
    '''
    raises the exception if the vertex is not found
    '''
    pass

class Vertex:
    '''
    an example implementation of a vertex or node of a graph
    '''

    def __init__(self, key):
        '''
        creates a new vertex.
        :param key: vertex identifier
        '''
        self._neighbors = []
        self._key = key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex[0].get_key() == neighbor[0].get_key():
                return neighbor[1]

class Graph:
    '''
    an implementation of a directed graph
    '''

    def __init__(self):
        '''
        creates a new, empty graph
        '''
        self._vertices = {}

    def add_vertex(self, vertex):
        '''
        adds a new vertex into the graph
        :param vertex: the vertex to be added into the graph
        :return: None
        '''
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        '''
        Add a firected edge between two vertices
        :param from_vertex: starting vertex of the edge
        :param to_vertex: where the edge ends
        :param weight: weight of the edge
        :return: None
        '''
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)



    def get_vertices(self):
        '''
        get all the vertices of the directed graph
        :return: List of vertices in the graph
        '''
        vertices = self._vertices.keys()
        vertices.sort()
        return vertices

    def get_edges(self):
        '''
        Get all the edges of the directed graph
        :return: List of edges of the graph
        '''
        edges = []
        for vertex in self._vertices:
            neighbors  = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor)))
        return edges


if __name__ == "__main__":
    graph = {                                                       #adjacency list
    "a" : [("b", 7), ("c", 9), ("f", 14)],
    "b" : [("a", 7), ("c", 10), ("d", 15)],
    "c" : [("a", 9), ("b", 10), ("d", 11),("f", 2)],
    "d" : [("b", 15), ("c", 11), ("e", 6)],
    "e" : [("d", 6), ("f", 9)],
    "f" : [("a", 14), ("c", 2), ("e", 9)]
    }
    g = Graph()

    g.add_vertex("a")
    g.add_vertex("b")
    g.add_vertex("c")
    g.add_vertex("d")
    g.add_vertex("e")
    g.add_vertex("f")

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)

    g.add_edge('b', 'a', 7)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)

    g.add_edge('c', 'a', 9)
    g.add_edge('c', 'b', 10)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)

    g.add_edge('d', 'b', 15)
    g.add_edge('d', 'c', 11)
    g.add_edge('d', 'e', 6)

    g.add_edge('e', 'd', 6)
    g.add_edge('e', 'f', 9)

    g.add_edge('f', 'a', 14)
    g.add_edge('f', 'c', 2)
    g.add_edge('f', 'e', 9)

    print(g.get_vertices())

    print(g.get_edges())



    v1 = Vertex('x')
    v2 = Vertex('y')

    print(v1.get_key())
    print(v2.get_key())
    (v1.add_neighbor(v2, 7))
    print(v1.get_connections())
    print(v1.get_weight(v2))
    print(v1.expose_vertex())


