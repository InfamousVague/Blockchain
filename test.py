from chain import Chain
from mine import Miner
from hashtree import HashTree

import os
import threading

# Colors 

green = '\033[92m'
blue = '\033[94m'
end = '\033[0m'

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


# Setup variables

blocklimit = 300 # 200 byte limit
difficulty = 1 # Number of proceeding zeros
sampletxs = 500000 # Starting TX backlog
chain = Chain(blocklimit, difficulty)

print blue + "Adding mock transactions..." + end

for i in range(sampletxs):
    chain.transact(os.urandom(40))

def log():
    print "Blockheight: " + str(len(chain.blocks))
    print "Block Limit: " + str(blocklimit) + "bytes"
    print "Pending TXs: " + str(len(chain.pending_transactions))
    if len(chain.blocks) > 0:
        print "Last Mined: " + str(chain.blocks[-1].timestamp)
        print "Latest Block:"
        print "\tRoot Hash: " + chain.blocks[-1].roothash
        print "\tPrev Hash: " + chain.blocks[-1].prevhash
        print "\tTransactions: " + str(len(chain.blocks[-1].transactions))
log()


def mine():
    miner = Miner(difficulty)
    new_block = chain.make_block()
    tree = HashTree(new_block)
    tree.hash()
    print blue + "Mining..." + end
    mined = miner.mine(tree.root)
    print "Mined " + tree.root + " with data " + mined[1]
    chain.submit_block(mined[1], new_block)
    log()
    mine()

mine()
