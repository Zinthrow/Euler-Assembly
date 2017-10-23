import os

#class vertice(object):
#    def __init__(self)

filename = "3_10.kmers.txt"
if os.path.exists(filename):
    kmers = open(filename, 'r')


lizt = []
test = {}
for kmer in kmers:
    for x,y in zip(kmer[0:], kmer[1:]):
        if y != "\n":
            lizt.append(x+y)
            test[x+y] =
    
print (lizt)
