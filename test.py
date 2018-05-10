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
    print "Last Mined: " + str(chain.blocks[-1].timestamp)
    print "Block Limit: " + str(blocklimit) + "bytes"
    print "Latest Block:"
    print "\tRoot Hash:\n\t\t" + chain.blocks[-1].roothash
    print "\tPrev Hash:\n\t\t" + chain.blocks[-1].prevhash
    print "\tTransactions:"
    for tx in chain.blocks[-1].transactions:
        print "\t\t" + tx

log()
