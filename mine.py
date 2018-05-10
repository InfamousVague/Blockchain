import os
from hashlib import sha256

class Miner:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def attempt_hash(self, root):
        randbytes = os.urandom(8)
        return [sha256(root + randbytes).hexdigest(), randbytes]

    def mine(self, root):
        ds = self.difficulty * '0'
        hash_attempt = self.attempt_hash(root)
        while hash_attempt[0][0:self.difficulty] is not ds:
            hash_attempt = self.attempt_hash(root)
        return hash_attempt 
        # Try to sha the root + random number hope for zeros
        # if we get the right amount of zeros, return
        # otherwise try again
