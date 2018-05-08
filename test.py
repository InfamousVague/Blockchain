from hashtree import HashTree

data = ['a', 'b', 'c', 'd']
tree = HashTree(data)
tree.hash()

print "Merkle Root: " + tree.root
print "Transactions:"
for hash in tree.hashes:
    print hash
