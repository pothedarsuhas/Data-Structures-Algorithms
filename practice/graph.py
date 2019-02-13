from graphs import *

class Vertex:
    """
    self._neighbors = []
        self._key = key
    get_connections(self)
    get_connections(self)
    get_key(self)
    add_neighbor(self, neighbor_vertex, weight)
    get_weight(self, to_vertex)
    """

    def __init__(self, key):
        self._neighbors = []
        self._key = key

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex[0].get_key() == neighbor[0].get_key():
                return neighbor[1]

class Graph:
    """
    self._vertices = {}
    add_vertex(self, key)
    add_edge(self, from_vertex, to_vertex, weight)
    get_vertices(self)
    get_edges(self)
    """
    def __init__(self):
        self._vertices = {}

    def add_vertex(self, key):
        v = Vertex(key)
        self._vertices[key] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self._vertices.keys():
            self.add_vertex(from_vertex)
        if to_vertex not in self._vertices.keys():
            self.add_vertex(to_vertex)
        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)


    def get_vertices(self):
        v = self._vertices.keys()
        v.sort()
        return v

    def get_edges(self):
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor)))
        return edges


# v1 = Vertex('A')
# v2 = Vertex('B')
# print(v1.get_key())
# print(v2.get_key())
#
# v1.add_neighbor(v2, 10)
#
# print(v1.get_connections())
# print(v1.get_weight(v2))


class BFS(Graph):
    def get_vertex(self, vertex_key):
        for vertex in self._vertices.keys():
            if vertex == vertex_key:
                return self._vertices[vertex_key]
        return None

    def BFS(self, start_vertex):
        #convert start_vertex string to object

        start_vertex = self.get_vertex(start_vertex)

        traversed = []
        q = queue()
        q.enqueue(start_vertex)
        visited = [False] * len(self._vertices)

        while not q.isEmpty():

            v = q.dequeue()
            key = v.get_key()

            if not visited[key] == True:
                visited[key] = True
                traversed.append(key)

            for neighbor in v.get_connections():
                if not visited[neighbor[0].get_key()] == True:
                    q.enqueue(neighbor[0])

        return traversed







if __name__ == "__main__":
    # graph = {                                                       #adjacency list
    # "a" : [("b", 7), ("c", 9), ("f", 14)],
    # "b" : [("a", 7), ("c", 10), ("d", 15)],
    # "c" : [("a", 9), ("b", 10), ("d", 11),("f", 2)],
    # "d" : [("b", 15), ("c", 11), ("e", 6)],
    # "e" : [("d", 6), ("f", 9)],
    # "f" : [("a", 14), ("c", 2), ("e", 9)]
    # }
    # g = Graph()
    #
    # g.add_vertex("a")
    # g.add_vertex("b")
    # g.add_vertex("c")
    # g.add_vertex("d")
    # g.add_vertex("e")
    # g.add_vertex("f")
    #
    # g.add_edge('a', 'b', 7)
    # g.add_edge('a', 'c', 9)
    # g.add_edge('a', 'f', 14)
    #
    # g.add_edge('b', 'a', 7)
    # g.add_edge('b', 'c', 10)
    # g.add_edge('b', 'd', 15)
    #
    # g.add_edge('c', 'a', 9)
    # g.add_edge('c', 'b', 10)
    # g.add_edge('c', 'd', 11)
    # g.add_edge('c', 'f', 2)
    #
    # g.add_edge('d', 'b', 15)
    # g.add_edge('d', 'c', 11)
    # g.add_edge('d', 'e', 6)
    #
    # g.add_edge('e', 'd', 6)
    # g.add_edge('e', 'f', 9)
    #
    # g.add_edge('f', 'a', 14)
    # g.add_edge('f', 'c', 2)
    # g.add_edge('f', 'e', 9)
    #
    # print(g.get_vertices())
    #
    # print(g.get_edges())

    g = BFS()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 5)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 6)

    print(g.BFS(0))