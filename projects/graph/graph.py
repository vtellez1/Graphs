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
        self.vertices[vertex_id] = set() #set of edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Breadth-First Traversal -- QUEUE -- FIFO
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        #Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:

            #dequeue first vert
            v = q.dequeue()
            #If it hasn't been visited yet:
            if v not in visited:
                print(v)
                #Add to visited
                visited.add(v)
                # enqueue neighbor verts
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Depth-First Traversal -- STACK -- LIFO
        Print each vertex in depth-first order
        beginning from starting_vertex.

        """
        s = Stack()
        #Add starting node to a stack
        s.push(starting_vertex)

        #Keep track of visited nodes
        visited = set()

        #While stack isn't empty:
        while s.size() > 0:
            # Pop the first vert
            v = s.pop()
            # If that vert isn't visited:
            if v not in visited:
                print(v)
                #Mark as visited                
                visited.add(v)
                #Push all its unvisited neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #If visted is None, create set to keep track of visited nodes
        if visited is None:
            visited = set()
        #Add starting node to set
        visited.add(starting_vertex)
        #Print starting vert / current vert
        print(starting_vertex)
        #Get starting vert/ current vert's neighbors
        neighbors = self.get_neighbors(starting_vertex)
        #Loop through neighbors
        for neighbor in neighbors:
            #if we haven't visited vert:
            if neighbor not in visited:
                #run recursivily, which will print each time neighbor becomes starting vert
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Breadth-First Traversal -- QUEUE -- FIFO
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            #Dequeue the first PATH
            path = q.dequeue()
            #Grab the last vertex from the PATH
            last_ver = path[-1]
            # If that vertex has not been visited...
            if last_ver not in visited:
                 # CHECK IF IT'S THE TARGET               
                if last_ver == destination_vertex:
                # IF SO, RETURN PATH                    
                    return path
                # Mark it as visited...                    
                visited.add(last_ver)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_ver):
                    # _COPY_ THE PATH                    
                    prev_path = list(path)
                    # APPEND THE NEIGHOR TO THE BACK                    
                    prev_path.append(next_vert)
                    q.enqueue(prev_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Depth-First Traversal -- STACK -- LIFO
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])

        # Create a Set to store visited vertices
        visited = set()

        # While the stack is not empty...
        while s.size() > 0:
            #pop the first PATH
            path = s.pop()
            #Grab the last vertex from the PATH
            last_ver = path[-1]
            # If that vertex has not been visited...
            if last_ver not in visited:
                 # CHECK IF IT'S THE TARGET               
                if last_ver == destination_vertex:
                # IF SO, RETURN PATH                    
                    return path
                # Mark it as visited...                    
                visited.add(last_ver)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_vert in self.get_neighbors(last_ver):
                    # _COPY_ THE PATH                    
                    prev_path = list(path)
                    # APPEND THE NEIGHOR TO THE BACK                    
                    prev_path.append(next_vert)
                    s.push(prev_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #If visted is None, create set to keep track of visited nodes
        if visited is None:
            visited = set()
        #If path is None, create list to keep track of path
        if path is None:
            path = []
        #Add starting node/current vert to set and path
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        #If starting ver/current vert is destination ver, return path
        if starting_vertex == destination_vertex:
            return path

        #Loop through starting vert/ current vert's neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            #if we haven't visited vert:
            if neighbor not in visited:
                #run recursivily
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path) 
                #If new path is not None, we return  
                if new_path:
                    return new_path    




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
    print(graph.vertices)

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
    print(graph.dfs(1, 6))
   
    print(graph.dfs_recursive(1, 6))
