from hashtree import HashTree
from block import Block
from sys import getsizeof
from hashlib import sha256

class Chain:
    def __init__(self, limit, difficulty):
        self.limit = limit
        self.difficulty = difficulty
        self.blocks = []
        self.pending_transactions = []

    def make_block(self):
        block = []
        while getsizeof(block) < self.limit:
            block.append(self.pending_transactions[len(block) - 1])
        return block

    def build_block(self, transactions, tree):
        prevhash = len(self.blocks) > 0 and self.blocks[-1].roothash or ''
        return Block(transactions, tree.root, tree.tree, prevhash)

    def submit_block(self, hashkey, transactions):
        tree = HashTree(transactions)
        tree.hash()
        hashed = sha256(tree.root + hashkey).hexdigest()
        if hashed[0:self.difficulty] is self.difficulty * '0':
            for tx in transactions:
                self.pending_transactions.remove(tx)
            block = self.build_block(transactions, tree) 
            self.blocks.append(block) 
            return True
        else:
            return False
    
    def transact(self, transaction):
        self.pending_transactions.append(transaction)
