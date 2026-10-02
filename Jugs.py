from queue import Queue

NODEQUEUE = Queue() # Contains Nodes waiting to be checked
FAILSTATES = [] # Contain all states that have been checked and dont work

class TreeNode:
    def __init__(self, parent, data):
        self,parent = None
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def jugBFS():
    pass

def main():
    pass

main()