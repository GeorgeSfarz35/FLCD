from queue import Queue



class BSTNode:
    def __init__(self, index, identifier=None):
        self.left = None
        self.right = None
        self.ident = identifier
        self.index = index

    def insert(self, ident, index):
        if self.ident == None :
            self.ident = ident
            self.index = index
            return index
            
        if self.ident == ident:
            return -1
        if self.get(ident) != "Identifier does not exist" :
            return -1


        if ident < self.ident:
            if self.left:
                self.left.insert(ident, index)
                return index
            self.left = BSTNode(index, ident)
            return index

        if self.right:
            self.right.insert(ident, index)
            return index
        self.right = BSTNode(index, ident)
        return index

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
    def __init__(self, root = BSTNode(0), capacity = 100):
        self.capacity = capacity
        self.root = root
        self.size = 0

    def add(self, ident):
        returnValue = self.root.insert(ident, self.size + 1)
        if returnValue != -1 :
            self.size += 1
        return returnValue
        

    def get (self, ident):
        return self.root.get(ident)

    
    
    def getTreeAsList(self):
        def myCriteria(e):
            return e[0]
        finalList = list(tuple())
        queue = Queue()
        queue.put(self.root)
        while queue.qsize() > 0 :
            queuedNode = queue.get(0)
            if queuedNode.left != None :
                queue.put(queuedNode.left)
            if queuedNode.right != None :
                queue.put(queuedNode.right)
            finalList.append((queuedNode.index, queuedNode.ident))
        finalList.sort(key=myCriteria)
        return finalList