# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

from collections import defaultdict

time = 1
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, v):
     
        # Initializing Queue and Visited Array
        queue = [v]
        visited = [v]

        # Initializing Arrival and Departure of Each Node
        numNodes = 9
        arrival = [0 for _ in range(numNodes + 1)]
        departure = [0 for _ in range(numNodes + 1)]

        global time
        
        # Converting NodeNum from String to Int to Easily Traverse
        nodeNum = int(ord(v) - 64)

        while queue:

            arrival[nodeNum] = time
            time += 1

            v = queue.pop(0)

            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    print('Tree Edge:', f'{str(v)} --> {str(neighbour)}')
                    queue.append(neighbour)
                    visited.append(neighbour)
                else:
                    print('Back Edge:', f'{str(v)} --> {str(neighbour)}')

            departure[nodeNum] = time
            time += 1
            print(v, arrival[nodeNum], departure[nodeNum])

        print(f'BFS: {visited}' + '\n')
        
'''
g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'E')
g.addEdge('B', 'C')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('E', 'F')
g.addEdge('F', 'I')

g.addEdge('D', 'G')
g.addEdge('D', 'H')
g.addEdge('G', 'H')

g.BFS('A')
g.BFS('D')
'''

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'D')
g.addEdge('B', 'C')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('D', 'H')
g.addEdge('E', 'A')
g.addEdge('F', 'I')
g.addEdge('G', 'D')
g.addEdge('H', 'G')
g.addEdge('H', 'F')
g.addEdge('H', 'I')
g.addEdge('I', 'H')

g.BFS('A')