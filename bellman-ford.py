# Kyle Ryan
# CISC 5825 Computer Algorithms
# Professor Josephine Altzman

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    # Add to Graph, Converts Labels to Ints
    def addEdge(self, u, v, w):
        u = int(ord(u) - 65)
        v = int(ord(v) - 65)
        self.graph.append([u, v, w])
         

   # Print Solution
    def printArr(self, dist):
        shortestPath = {}

        print("Distance from Source")
        for i in range(self.V): 
            nodeName = (chr(i + 65))
            nodeDist = dist[i]
            shortestPath[nodeName] = nodeDist
            print("{0}\t\t{1}".format(nodeName, nodeDist))

        # Sorting Shortest Path (Weights/Distance Between Nodes)
        sorted_tuples = sorted(shortestPath.items(), key=lambda item: item[1])
        sorted_dict = dict(sorted_tuples)

        # Returning Keys
        sortedKeys = list(sorted_dict.keys())
        print(f'BFS: {sortedKeys}')

    def BellmanFord(self, src):  # sourcery skip: use-itertools-product
 
        # Initialize Distances to Infinite
        dist = [float("Inf")] * int(self.V)
        dist[int(ord(src) - 65)] = 0
 
        # Find Shortest Path to Edges
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        # Detect Negative Cycle
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print("Graph Contains a Negative Weight Cycle!")
                        return
                         
        self.printArr(dist)


g = Graph(8)
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

g.BellmanFord('A')
