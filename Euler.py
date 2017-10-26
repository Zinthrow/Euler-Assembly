import os

import os

#class vertice(object):
#    def __init__(self)

filename = "3_10.kmers.txt"
if os.path.exists(filename):
    kmers = open(filename, 'r')



graph = {} #the key = Nucleotide seq and the value = [indegrees],[outdegrees]

for kmer in kmers:
    prev = None
    for x,y in zip(kmer[0:], kmer[1:]):
        if y != "\n":
            if x+y not in graph:
                graph[x+y] = [[],[]]
            if prev != None:
                graph[prev][1].append(x+y)#makes outdegrees for prev                
                graph[x+y][0].append(prev)#sets indegrees for x+y
            prev = x+y
keys = sorted(keys)            
for edges in keys:
    for degrees in edges:
        degrees = sorted(degrees)
fake_start = []
for start in keys:
    while start not in fake_start:
        path = str(start)
        copygraph = graph
        opennode ={}
        if copygraph[start][0] is not []:
            opennode[start] = True
        while openode != {}:
            dupligraph = copygraph
            subpath = start
            x = start
            while copygraph[x][1] != []:
                x = dupligraph[x][1][0]
                subpath = subpath + x
                dupligraph[x][1].pop(x)
