graph = {
    1: [2],
    2: [9, 4],
    3: [6, 7],
    4: [3],
    5: [],
    6: [8],
    7: [],
    8: [5],
    9: [5],
}

'''
    Create helper function to:
        Go through a nodes trail.
            If we see the node we are currently working with, we can assume there is a cycle
            So return False.
            If other node found, return True instead of an array.

        Do this for both routes.

    Return if either results are True
'''

def traverseGraph (graph={}, start=None, end=None):
    visitedNodes = []
    options = [] if start not in graph else graph[start]

    while len(options):
        curr = options.pop()
        if curr in visitedNodes:
            if curr == start:
                return False
            continue
            
        if curr == end:
            return True

        nextOptions = graph[curr]
        visitedNodes.append(curr)
        if end in nextOptions:
            return True
        options += nextOptions
    
    return False

def routeBetweenNodes (graph, n1, n2):
    route1 = traverseGraph(graph, n1, n2)
    if route1:
        return True
    
    route2 = traverseGraph(graph, n2, n1)
    if route2:
        return True
    else:
        return False

print(routeBetweenNodes(graph, 7, 4))