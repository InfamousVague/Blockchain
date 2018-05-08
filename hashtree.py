from hashlib import sha256

class HashTree:
    
    def __init__(self, transactions=None):
        self.transactions = transactions
        self.root = None
        self.hashes = []

    def hash(self, transactions=None):
        cache = []
        txs = transactions or self.transactions
        length = len(txs) / 2 + len(txs) % 2
        
        for i in range(length):
            left = sha256(txs[i]).hexdigest()
            right = sha256(txs[i + 1] or '').hexdigest()
            # Save transaction hashes
            self.hashes.append(left)
            self.hashes.append(right)
            # Combine nodes
            node = left + right
            # Hash nodes
            cache.append(sha256(node).hexdigest())

        if len(cache) != 1:
            self.hash(cache)
        else:
            self.root = cache[0]
 
    def root(self):
        return self.root

    def hashes(self):
        return self.hashes
