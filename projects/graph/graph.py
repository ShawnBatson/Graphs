"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with the vertex id, set value to an empty set (no edges yet)
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # find vertex v1 in our vertices, add v2 to set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting_vertex.
        box = Queue()
        # Create an empty set to track visited verties
        box.enqueue(starting_vertex)
        visited_vert = set()

        # while the queue is not empty,
        while box.size() > 0:
            #     get current vertex (dequeue from queue)
            current = box.dequeue()
            # check if the current vertex has not been visited, if it hasn't:
            if current not in visited_vert:
                # print the current vertex.
                print(current)
                # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_vert.add(current)
                for neighbor in self.get_neighbors(current):
                    # queue up all current vertices neighbors so we can visit them next
                    box.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack and push the starting_vertex.
        box = Stack()
        box.push(starting_vertex)
        # Create an empty set to track visited verties
        visited_vert = set()

        # while the stack is not empty,
        while box.size() > 0:
            current = box.pop()  # get current vertex (pop from stack)

            # check if the current vertex has not been visited, if it hasn't:
            if current not in visited_vert:
                print(current)  # print the current vertex.
                visited_vert.add(current)  # mark the current vertex as visited
                for neighbor in self.get_neighbors(current):
                    # push up all current vertices neighbors so we can visit them next
                    box.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        box = Queue()  # Create an empty queue and enqueue the PATH TO starting_vertex.
        visited_vert = set()  # Create an empty set to track visited verties
        box.enqueue([starting_vertex])
        while box.size() > 0:  # while the queue is not empty

            current_path = box.dequeue()  # get current vertex (dequeue from queue)

            # set the current vertex to the LAST element of the path.
            # print(current_path)
            node = current_path[-1]

            if node is destination_vertex:  # CHECK IF THE CURRENT VERTEX IS DESTINATION
                return current_path  # if it is, stop and return
            # check if the current vertex has not been visited, if it hasn't:
            if node not in visited_vert:  # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_vert.add(node)

                # queue up NEW paths with each neighbor:
                for neighbor in self.get_neighbors(node):
                    copy_path = current_path.copy()  # Take current path
                    copy_path.append(neighbor)  # append neightbor to it
                    box.enqueue(copy_path)  # queue up NEW path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        box = Stack()
        visited_vert = set()
        box.push([starting_vertex])
        while box.size() > 0:
            current_path = box.pop()
            node = current_path[-1]

            if node is destination_vertex:
                return current_path
            if node not in visited_vert:
                visited_vert.add(node)

                for neighbor in self.get_neighbors(node):
                    copy_path = current_path.copy()
                    copy_path.append(neighbor)
                    box.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if len(path) == 0:
            path = [starting_vertex]
        if starting_vertex is destination_vertex:
            return path
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                current_path = path.copy()
                current_path.append(neighbor)
                true_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, current_path)
            if true_path:
                return true_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
