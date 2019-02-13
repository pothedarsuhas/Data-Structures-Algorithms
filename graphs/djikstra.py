#not working

# shortest path
from stack import *
from graph import *
import sys

print(sys.maxint)

class Dijkstra(Graph):

    def _min_distance(self, distance, fringe):
        pass


    def dijkstra(self, source, destination):
        # initialize the distance of all nodes to infinity
        distance = [(sys.maxint, -1)] * len(self._vertices)

        #distance of source from source is 0
        distance[source] = (0, 0)

        # initially none of the nodes is visited
        visited = [False] * len(self._vertices)

        fringe = [source] #yet to be visited nodes in the same level

        # while there are still entries in the fringe
        while fringe:
            # find node with min distance in fringe as current vertex
            current_vertex_key = self._min_distance(distance, fringe)

            fringe.remove(current_vertex_key)
            visited[current_vertex_key] = True
            current_vertex = self.get_vertex(current_vertex_key)

            for neighbor in current_vertex.get_connections():
                neighbor_vertex = neighbor[0].get_key()
                neighbor_weight = neighbor[1]

            if neighbor_vertex not in fringe and visited[neighbor_vertex]:
                fringe.append(neighbor_vertex)

            if distance[neighbor_vertex][0] > distance[current_vertex_key][0] + neighbor_weight:
                distance[neighbor_vertex][0] = (distance[current_vertex_key][0] + neighbor_weight, current_vertex_key[0])

        s = stack()
        x = destination

        while x!= source:
            s.push(x)
            x = distance[x][1]
        s.push(x)

        shortest_path = []
        while not s.isEmpty():
            shortest_path.append(s.pop())

        return (distance)


if __name__ == "__main__":
    g = Dijkstra()
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(2, 1, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 5)
    g.add_edge(4, 3, 1)
    g.add_edge(2, 4, 6)
    g.dijkstra(1,3)