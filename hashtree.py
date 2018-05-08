from hashlib import sha256

class HashTree:
    
    def __init__(self, transactions=None):
        self.transactions = transactions
        # Root hash
        self.root = None
        # Transaction hashes
        self.hashes = []
        # Tree (e.g. [roothash, [node-e, node-f], [node-a, node-b, node-c, node-d]])
        self.tree = []

    def hash(self, transactions=None):
        # Used to store hashed nodes
        cache = []
        # If transactions are provided, we're hashing nodes, not leaves
        txs = transactions or self.transactions
        # If our transactions are not even, we'll iterate once more
        length = len(txs) / 2 + len(txs) % 2
        
        for i in range(length):
            # Hash the leaves
            left = sha256(txs[i]).hexdigest()
            right = sha256(txs[i + 1] or '').hexdigest()
            # Save leaf node transaction hashes
            if not transactions:
                self.hashes.append(left)
                self.hashes.append(right)
            # Combine nodes
            node = left + right
            # Hash nodes
            cache.append(sha256(node).hexdigest())
        
        # Update tree
        self.tree.insert(0, cache)
        # If we haven't gotten to the root hash, keep going
        if len(cache) is not 1:
            self.hash(cache)
        # Otherwise set our root hash and quit iterating
        else:
            self.root = cache[0]
        

