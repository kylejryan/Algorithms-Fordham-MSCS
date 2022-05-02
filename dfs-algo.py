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

    # DFS Util Returns Arrival & Departure Times and What Type of Edge the Node is
    def DFSUtil(self, v, visited, list, arrival, departure):
        
        global time
        nodeNum = int(ord(v) - 64)

        arrival[nodeNum] = time
        time += 1

        visited.add(v)
        list.append(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                print('Tree Edge:', f'{str(v)} --> {str(neighbour)}')
                self.DFSUtil(neighbour, visited, list, arrival, departure)
            else:
                print('Back Edge:', f'{str(v)} --> {str(neighbour)}')

        departure[nodeNum] = time
        time += 1
        print(v, arrival[nodeNum], departure[nodeNum])
        
    def DFS(self, v):
        
        # Initializing Size of Lists and Sets
        numNodes = 9
        visited = set()
        dfsList = []

        arrival = [0 for _ in range(numNodes + 1)]
        departure = [0 for _ in range(numNodes + 1)]


        self.DFSUtil(v, visited, dfsList, arrival, departure)
        print(f'DFS: {dfsList}' + '\n')
        
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

 
g.DFS('A')
g.DFS('D')
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

g.DFS('A')