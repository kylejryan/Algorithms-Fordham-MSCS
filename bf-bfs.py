from collections import defaultdict

time = 1
class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v, w):
        self.graph[u].append(v)
    
    def BFS(self, v):
     
        queue = [v]
        visited = [v]

        numNodes = 9
        arrival = [0 for _ in range(numNodes + 1)]
        departure = [0 for _ in range(numNodes + 1)]

        global time
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
        

g = Graph()
g.addEdge('A', 'B', 1)
g.addEdge('A', 'E', 4)
g.addEdge('A', 'F', 8)
g.addEdge('B', 'C', 2)
g.addEdge('B', 'F', 6)
g.addEdge('B', 'G', 6)
g.addEdge('C', 'D', 1)
g.addEdge('C', 'G', 2)
g.addEdge('D', 'H', 4)
g.addEdge('D', 'G', 1)
g.addEdge('E', 'F', 5)
g.addEdge('G', 'F', 1)
g.addEdge('G', 'H', 1)


g.BFS('A')