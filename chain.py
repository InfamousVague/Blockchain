from hashtree import HashTree
from block import Block
from sys import getsizeof

class Chain:
    def __init__(self, limit):
        self.limit = limit
        self.blocks = []
        self.pending_transactions = []

    def new_block(self):
        tree = HashTree(self.pending_transactions)
        tree.hash()
        prevhash = len(self.blocks) > 0 and  self.blocks[-1].roothash or ''
        block = Block(tree.transactions, tree.root, tree.tree, prevhash)
        self.blocks.append(block)
        self.pending_transactions = []

    def transact(self, transaction):
        if getsizeof(self.pending_transactions + [transaction]) > self.limit:
            self.new_block()
            self.pending_transactions = [transaction]
        else:
            self.pending_transactions.append(transaction)
