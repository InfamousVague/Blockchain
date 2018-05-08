from hashtree import HashTree
import numpy as np


data = ['a', 'b', 'c', 'd']
tree = HashTree(data)
tree.hash()

print "Merkle Root: " + tree.root
print "Transactions:"
for hash in tree.transactions:
    print hash
print "Tree:"
print(np.matrix(tree.tree))
