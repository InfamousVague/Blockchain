from time import time

class Block:
    def __init__(self, transactions, roothash, tree):
        self.timestamp = time()
        self.transactions = transactions
        self.roothash = roothash
        self.tree = tree
