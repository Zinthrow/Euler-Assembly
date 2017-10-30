import os
import copy

#class vertice(object):
#    def __init__(self)

def balanced(graph):
    graph[2] = len(graph[1]) - len(graph[0])
    return graph[2]

filename = "3_10.kmers.txt"
if os.path.exists(filename):
    kmers = open(filename, 'r')
    
graph = {} #the key = Nucleotide seq and the value = [indegrees],[outdegrees]
keys = []
for kmer in kmers:
    prev = None
    for x,y in zip(kmer[0:], kmer[1:]):
        if y != "\n":
            if x+y not in graph:
                graph[x+y] = [[],[],0]
                keys.append(x+y)
            if prev != None:
                graph[prev][1].append(x+y)#makes outdegrees for prev                
                graph[x+y][0].append(prev)#sets indegrees for x+y
            prev = x+y
            
keys = sorted(keys)            
for edges in keys:
    for degrees in edges:
        degrees = sorted(degrees)
        
outdegrees = 0
for key in keys:
    balanced(graph[key])
    outdegrees += len(graph[key][1])
    if balanced(graph[key]) >= 1:
        s = key
    elif balanced(graph[key]) <= -1:
        t = key
        
path = ""
usededge ={}
count = 0
while len(path) < outdegrees + 2:
    count += 1
    copygraph = copy.deepcopy(graph)
    x = s
    path = x
    for smer in usededge:#moves used degrees to end of degrees list
        if len(smer) == 4:
            copygraph[smer[0:2]][1].pop(0) #moves outdegrees
            copygraph[smer[0:2]][1].append(smer[2:])
            copygraph[smer[2:]][0].pop(0) #moves indegrees
            copygraph[smer[2:]][0].append(smer[0:2])
            
    while copygraph[x][1] != [] and len(path) <= outdegrees + 2:
        if len(copygraph[x][1]) > 1:
            usededge[x+copygraph[x][1][0]] = True
        prev = x
        x = copygraph[x][1][0]
        path = path + x[1]
        for y in copygraph[x][0]:
            if y == prev:
                copygraph[y][1].pop(0)
                
print (path)
