import math
globe = {}

def pythagoras(start, end):
    return math.sqrt((end[0]-start[0])**2 + (end[1] - start[1])**2)

def build2DMap (size):
    nodes  = {}
    for i in range(size):
        for j in range(size):
            children = []
            # top
            if i - 1 >= 0:
                children.append(f'{i-1}:{j}')
            # bottom
            if i + 1 < size:
                children.append(f'{i+1}:{j}')  
            # left
            if j + 1 < size:
                children.append(f'{i}:{j+1}')                                
            # right
            if j - 1 >= size:
                children.append(f'{i}:{j-1}')

            nodes[f'{i}:{j}'] = { 'children':children, 'parent':None, 'distance':None }

    return nodes

def findNextBestNode (nodes, completed):
    bestFit = float('inf')
    nextNode = None
    for node in nodes:
        if node in completed:
            continue
        if nodes[node]['distance'] == None:
            continue
        if nodes[node]['distance'] < bestFit:
            nextNode = node
    return nextNode

def astar (start, end, nodes=build2DMap(100), completed={}):
    currentlyAt = start
    nodes[currentlyAt]['distance'] = 0
    endSplit = [int(x) for x in end.split(':')]
    
    while currentlyAt != end and currentlyAt != None:
        currentSplit = [int(x) for x in currentlyAt.split(':')]
        newDistance = nodes[currentlyAt]['distance'] + 1 + pythagoras(endSplit, currentSplit)

        for childName in nodes[currentlyAt]['children']:
            if nodes[childName]['distance'] == None or nodes[childName]['distance'] > newDistance:
                nodes[childName]['distance'] = newDistance
                nodes[childName]['parent'] = currentlyAt

        completed[currentlyAt] = None
        currentlyAt = findNextBestNode(nodes, completed)

    return nodes

def extractPath (end, nodes):
    currentlyAt = end
    path = [end]
    while currentlyAt in nodes and nodes[currentlyAt]['parent'] != None:
        path.append(nodes[currentlyAt]['parent'])
        currentlyAt = nodes[currentlyAt]['parent']
    print('Nodes traversed ', len(path))

    return path[::-1]

start = '0:0'
end = '99:5'
nodes = astar(start, end)
path = extractPath(end, nodes)
print(path)