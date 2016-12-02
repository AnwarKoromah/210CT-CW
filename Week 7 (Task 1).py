class Graph:
    def __init__(self):
        self.adjList = {}

    def define(self, node, edge):
        self.adjList[node] = edge

    def printing(self):
        for i in range(1, len(self.adjList)+1, 1):
            print(i, ":", self.adjList[i])

    def newEdge(self, node, edge):
        for i in range(1, len(self.adjList), 1):
            dictKeys = list(self.adjList.keys())
            nodeNo = int(node)
            edgeNo = int(edge)
            if nodeNo == dictKeys[i] or edgeNo == dictKeys[i]:
                self.adjList[nodeNo].append(edgeNo)
                self.adjList[edgeNo].append(nodeNo)
                break
        adjListLength = len(self.adjList)


if __name__ == '__main__':
    g = Graph()
    g.define(1, [2,3])
    g.define(2, [4])
    g.define(3, [4,5])
    g.define(4, [5])
    g.define(5, [])
    g.newEdge(2, 5)
    g.printing()


