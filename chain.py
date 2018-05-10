from hashtree import HashTree
from block import Block

class Chain:
    def __init__(self, limit):
        self.limit = limit
        self.blocks = []
        self.pending_transactions = []

    def info(self):
        return {
            blockheight: len(self.blocks)
        }

    def new_block(self):
        tree = HashTree(self.pending_transactions)
        tree.hash()
        block = Block(tree.transactions, tree.root, tree.tree)
        self.blocks.append(block)
        self.pending_transactions = []

    def transact(self, transaction):
        self.pending_transactions.append(transaction)
        if len(self.pending_transactions) is self.limit:
            self.new_block()
