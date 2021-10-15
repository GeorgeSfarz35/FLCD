class BSTNode:
    def __init__(self, identifier=None,  value=None):
        self.left = None
        self.right = None
        self.ident = identifier
        self.val = value

    def insert(self, ident, val):
        if self.ident == ident:
            return -1

        if ident < self.ident:
            if self.left:
                self.left.insert(ident, val)
                return
            self.left = BSTNode(ident, val)
            return

        if self.right:
            self.right.insert(ident, val)
            return
        self.right = BSTNode(ident, val)
