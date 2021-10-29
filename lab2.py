from typing import List, Tuple


class BSTNode:
    def __init__(self, index, identifier=None):
        self.left = None
        self.right = None
        self.ident = identifier
        self.index = index

    def insert(self, ident, index):
        if self.ident == ident:
            return -1

        if ident < self.ident:
            if self.left:
                self.left.insert(ident, index)
                return
            self.left = BSTNode(index, ident)
            return

        if self.right:
            self.right.insert(ident, index)
            return
        self.right = BSTNode(index, ident)

    def get(self, ident):
        if self.ident == ident:
            return self

        if ident < self.ident:
            if self.left:
                return self.left.get(ident)               
            return "Identifier does not exist"

        if self.right:
            return self.right.get(ident)
        return "Identifier does not exist"

class SymbolTable:
    def __init__(self, root, capacity = 100):
        self.capacity = capacity
        self.root = BSTNode(None)
        self.size = 0
        self.root.index = 0

    def insert(self, ident):
        self.root.insert(ident, self.size + 1)
        self.size += 1

    def get (self, ident):
        self.root.get(ident)
    
    def getTreeAsList(self):
        finalList = List(Tuple())
        queue = List[BSTNode]
        queue.insert(self.root)
        while(queue.__sizeof__ > 0):
            if(queue[0].left != None):
                queue.insert(queue[0].left)
            if(queue[0].left != None):
                queue.insert(queue[0].left)
            finalList.insert((queue[0].index, queue.pop(0).ident))

if __name__ == "__main__":
    identifiers = BSTNode()
    constants = BSTNode()
    identifiers.ident = "name1"
    identifiers.insert("name2")
    print(identifiers.get("name2").ident)
