from queue import Queue

INITIALSTATE = [12, 8, 3] #Beginning state of problem
FAILSTATES = [] # Contain all states that have been checked and dont work

class JugTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        if child_node.data not in FAILSTATES:
            self.children.append(child_node)


    def isGoalState(self):
        if 1 in self.data:
            return True

def expand(node):
    capacity_12 = 12
    capacity_8 = 8
    capacity_3 = 3

    #Fill slot 1
    currState = node
    currState.data[0] = 12
    node.add_child(currState)
    #Fill slot 2
    currState = node
    currState.data[1] = 8
    node.add_child(currState)
    #Fill slot 3
    currState = node
    currState.data[2] = 3
    node.add_child(currState)
    #Empty slot 1
    currState = node
    currState.data[0] = 0
    node.add_child(currState)
    #Empty slot 2
    currState = node
    currState.data[1] = 0
    node.add_child(currState)
    #Empty slot 3
    currState = node
    currState.data[2] = 0
    node.add_child(currState)
    #Transfer slot 1 to slot 2
    currState = node
    amount = min(currState.data[0], capacity_8 - currState.data[1])
    currState.data[0] -= amount
    currState.data[1] += amount
    node.add_child(currState)
    #Transfer slot 1 to slot 3
    amount = min(currState.data[0], capacity_3 - currState.data[2])
    currState.data[0] -= amount
    currState.data[2] += amount
    node.add_child(currState)
    #Transfer slot 2 to slot 1
    amount = min(currState.data[1], capacity_12 - currState.data[0])
    currState.data[1] -= amount
    currState.data[0] += amount
    node.add_child(currState)
    #Transfer slot 2 to slot 3
    amount = min(currState.data[1], capacity_3 - currState.data[2])
    currState.data[1] -= amount
    currState.data[2] += amount
    node.add_child(currState)
    #Transfer slot 3 to slot 1
    amount = min(currState.data[2], capacity_12 - currState.data[0])
    currState.data[2] -= amount
    currState.data[0] += amount
    node.add_child(currState)
    #Transfer slot 3 to slot 2
    amount = min(currState.data[2], capacity_8 - currState.data[1])
    currState.data[2] -= amount
    currState.data[1] += amount
    node.add_child(currState)

def jugBFS():
    gallonJugs = JugTreeNode(INITIALSTATE)

    if gallonJugs.isGoalState():
        return gallonJugs.data #Goal state
    
    nodeQueue = Queue() # Contains Nodes waiting to be checked
    nodeQueue.put(gallonJugs)

    while not nodeQueue.empty():
        node = nodeQueue.get()

        if node.isGoalState():
            return node.data
        
        else:
            FAILSTATES.append(node.data)
        
        expand(node)

        for child in node.children:
            nodeQueue.put(child)
    
    return None


def main():
    pass

main()