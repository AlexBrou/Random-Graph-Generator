import random


def randomGraphGenerator(
    numberOfVertices,
    directed=False,
    weighted=False,
    weightMin=1,
    weightMax=10,
    oneConnectedComponent=True,
):
    numberOfVertices = 5
    assert weightMin <= weightMax
    edges = {}

    for i in range(1, numberOfVertices + 1):
        if oneConnectedComponent:
            minEdgePerVertice = 1
        else:
            minEdgePerVertice = 0
        numberOfEdges = random.randint(minEdgePerVertice, numberOfVertices - 1)
        nn = 0
        while nn != numberOfEdges:
            destVertice = random.randint(1, numberOfVertices)
            if destVertice == i:
                continue
            newEdge = (i, destVertice)
            if not directed:
                if i >= destVertice:
                    newEdge = (destVertice, i)

            if not (newEdge in edges.keys()):
                if weighted:
                    edges[newEdge] = random.randint(weightMin, weightMax)
                else:
                    edges[newEdge] = None
            nn += 1
    return list(edges.keys())


if __name__ == "__main__":
    # for a simple undirected graph, with only one connected component
    print(randomGraphGenerator(5))

    # directed graph
    randomGraphGenerator(5, directed=True)

    # with weights
    randomGraphGenerator(5, weighted=True)
    randomGraphGenerator(5, weighted=True, weightMin=2, weightMax=20)

