from chain import Chain
import os
import threading

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

chain = Chain(5)


for i in range(50000):
    chain.transact(os.urandom(40))

def log():
    print "Blockheight: " + str(len(chain.blocks))
    print "Last Mined: " + str(chain.blocks[0].timestamp)
    print "Latest Block:"
    print "\tRoot Hash:\n\t\t" + chain.blocks[0].roothash
    print "\tTransactions:"
    for tx in chain.blocks[0].transactions:
        print "\t\t" + tx

log()
