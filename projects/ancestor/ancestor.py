
"""
How to solve any graph problem
1. Translate the problem into graph terminology
2. Build the graph
3. Traverse it

Thought process: 
Pull out each number from the ancestor data set given, set them to verts. 
Using their parent child relationship, create edges.
And then implement dfs... ?
"""
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph if does not already exist.
        """
        if vertex_id not in self.vertices:
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
        
    def dft(self, starting_vertex):
        """
        Depth-First Traversal -- STACK -- LIFO
        Print each vertex in depth-first order
        beginning from starting_vertex.

        """
        s = Stack()
        #Add starting pair to stack, (vert we're on, distance)
        s.push((starting_vertex, 0))

        #Keep track of visited verts and visited pairs
        visited = set()
        visited_pairs = set()

        #While stack isn't empty:
        while s.size() > 0:
            # Pop the first pair
            current_pair = s.pop()
            #Add to visited
            visited_pairs.add(current_pair)

            #first of pair is our current vert, second of pair is distance
            current_vert = current_pair[0]
            current_distance = current_pair[1]

            # If that vert isn't visited:
            if current_vert not in visited:
                #Mark as visited vert               
                visited.add(current_vert)

                #Push all its unvisited neighbors to the stack
                for next_vert in self.get_neighbors(current_vert):
                    next_distance = current_distance + 1
                    s.push((next_vert, next_distance))

        #default distance at 0
        distance_traveled = 0
        #default eldest to -1
        eldest_one = -1

        #Loop through our visited pairs
        for pair in visited_pairs:
            #first of pair is our vert, second of pair is distance
            vert = pair[0]
            distance = pair[1]
            #if distance of pair is greater than distance traveled...
            if distance > distance_traveled:
                #distance of pair becomes distance traveled
                distance_traveled = distance
                #eldest one becomes vert we traveled to
                eldest_one = vert
        return eldest_one

# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input individual. 
# If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
# If the input individual has no parents, the function should return -1.

#The input will not be empty.
#There are no cycles in the input.
#There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
#IDs will always be positive integers.
#A parent may have any number of children.

#(parent, child)
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

"""
    def test_earliest_ancestor(self):
        test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
        self.assertEqual(earliest_ancestor(test_ancestors, 1), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 2), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 3), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 4), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 5), 4)
        self.assertEqual(earliest_ancestor(test_ancestors, 6), 10)
        self.assertEqual(earliest_ancestor(test_ancestors, 7), 4)
        self.assertEqual(earliest_ancestor(test_ancestors, 8), 4)
        self.assertEqual(earliest_ancestor(test_ancestors, 9), 4)
        self.assertEqual(earliest_ancestor(test_ancestors, 10), -1)
        self.assertEqual(earliest_ancestor(test_ancestors, 11), -1)
"""


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        #Create edge with child(ancestor[1] and parent (ancestor[0])), only needs to go one way 
        #Doing it backwards because we want to travel up to the oldest so edge needs to go from child to parent
        graph.add_edge(ancestor[1], ancestor[0])
    print(graph.vertices)

    eldest = graph.dft(starting_node)
    print(eldest)
    return eldest



earliest_ancestor(test_ancestors, 9)