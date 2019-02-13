from graph import *
from queue import *

class VertexNotFound(Exception):
    '''
    raises the exception if the vertex is not found
    '''
    pass

class GraphBFS(Graph):
    def get_vertex(self, vertex_key):
        for vertex in self._vertices.keys():
            if vertex_key == vertex:
                return self._vertices[vertex]
        return None

    def BFS(self, start_vertex):
        start_vertex = self.get_vertex(start_vertex)

        if start_vertex is None:
            raise Exception("The vertex is not present in the graph.")

        visited = [False] * len(self._vertices)
        traversed = []

        q = queue()
        q.enqueue(start_vertex)

        while not q.isEmpty():                  #this loop goes on until every node is traversed
            v = q.dequeue()
            key = v.get_key()

            if not visited[key]:
                visited[key] = True
                traversed.append(key)

            for neighbor in v.get_connections():
                if not visited[neighbor[0].get_key()]:
                    q.enqueue(neighbor[0])

        return traversed

if __name__ == "__main__":


    g = GraphBFS()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 5)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 6)


    print(g.BFS(0))



