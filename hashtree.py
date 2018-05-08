from hashlib import sha256

class HashTree:
    
    def __init__(self, transactions=None):
        self.transactions = transactions
        self.root = None

    def hash(self, transactions=None):
        cache = []
        txs = transactions or self.transactions
        length = len(txs) / 2 + len(txs) % 2
        
        for i in range(length):
            left = txs[i]
            right = txs[i + 1] or ''
            node = sha256(left).hexdigest() + sha256(right).hexdigest()
            cache.append(sha256(node).hexdigest())

        if len(cache) != 1:
            self.hash(cache)
        else:
            self.root = cache[0]
 
    def root(self):
        return self.root
