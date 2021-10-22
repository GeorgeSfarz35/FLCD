class BSTNode:
    def __init__(self, identifier=None):
        self.left = None
        self.right = None
        self.ident = identifier

    def insert(self, ident):
        if self.ident == ident:
            return -1

        if ident < self.ident:
            if self.left:
                self.left.insert(ident)
                return
            self.left = BSTNode(ident)
            return

        if self.right:
            self.right.insert(ident)
            return
        self.right = BSTNode(ident)

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


if __name__ == "__main__":
    identifiers = BSTNode()
    constants = BSTNode()
    identifiers.ident = "name1"
    identifiers.insert("name2")
    print(identifiers.get("name2").ident)
