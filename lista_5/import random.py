import random


class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.adjacent = [[] for _ in range(num_of_vertices)]
        self.weights = {}
        self.genGraph()
        self.index = max(self.connectedComponents(), key=len)

    def addEdge(self, x, y, weight):
        if x != y:
            self.adjacent[x].append(y)
            self.adjacent[y].append(x)
            self.weights[(x, y)] = weight
            self.weights[(y, x)] = weight

    def genGraph(self):
        for each in range(self.num_of_vertices):
            self.addEdge(each, random.randint(1, self.num_of_vertices - 1), random.randint(1, 10))
        self.printGraph()

    def printGraph(self):
        print(f'Wylosowany graf:')
        [print(f'{i} {self.adjacent[i]}') for i in range(self.num_of_vertices)]
        print(f'\n===================================\n')

    def dfsSearch(self, temp, vert, visited):
        visited[vert] = True
        temp.append(vert)
        for each in self.adjacent[vert]:
            if not visited[each]:
                temp = self.dfsSearch(temp, each, visited)
        return temp

    def connectedComponents(self):
        visited = []
        concomp = []
        for i in range(self.num_of_vertices):
            visited.append(False)
        for j in range(self.num_of_vertices):
            if not visited[j]:
                temp = []
                concomp.append(self.dfsSearch(temp, j, visited))
        return concomp

    def consistentGraph(self):
        listed = [self.adjacent[i] for i in self.index]
        connected_graph = {self.index[i]: listed[i] for i in range(len(self.index))}
        return connected_graph

    def dijsktra(self):
        connected_graph = self.consistentGraph()
        d_in, d_out = random.sample(self.index, 2)

        optimal_path = {d_in: (None, 0)}
        current_vert = d_in
        visited = set()
        while current_vert != d_out:
            visited.add(current_vert)
            neighbours = connected_graph[current_vert]
            current_weight = optimal_path[current_vert][1]
            for next_vert in neighbours:
                weight = self.weights[(current_vert, next_vert)] + current_weight
                if next_vert not in optimal_path:
                    optimal_path[next_vert] = (current_vert, weight)
                else:
                    current_optimal_weight = optimal_path[next_vert][1]
                    if current_optimal_weight > weight:
                        optimal_path[next_vert] = (current_vert, weight)
            next_neighbours = {vert: optimal_path[vert] for vert in optimal_path if vert not in visited}
            current_vert = min(next_neighbours, key=lambda k: next_neighbours[k][1])
        final_path = []
        while current_vert:
            final_path.append(current_vert)
            next_vert = optimal_path[current_vert][0]
            current_vert = next_vert
        final_path = final_path[::-1]

        print(*final_path, sep=' -> ')
        for i in range(len(final_path) - 1):
            final_weight = self.weights[(final_path[i], final_path[i + 1])]
            print(f'Waga pomiędzy {final_path[i]} i {final_path[i + 1]} to {final_weight}')
