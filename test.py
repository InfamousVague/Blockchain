from chain import Chain
import os
import threading

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


blocklimit = 300 # 200 byte limit
sampletxs = 50000
chain = Chain(blocklimit)


for i in range(sampletxs):
    chain.transact(os.urandom(40))

def log():
    print "Blockheight: " + str(len(chain.blocks))
    print "Last Mined: " + str(chain.blocks[0].timestamp)
    print "Block Limit: " + str(blocklimit) + "bytes"
    print "Latest Block:"
    print "\tRoot Hash:\n\t\t" + chain.blocks[0].roothash
    print "\tTransactions:"
    for tx in chain.blocks[0].transactions:
        print "\t\t" + tx

log()
