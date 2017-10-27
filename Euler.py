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
def balanced(key):
    key[2] = len(key[1]) - len(key[0])
    if key[2] == 0:
        return True
    else:
        return False
fake_start = []
for start in keys:
    path = str(start)
    copygraph = graph
    opennode ={}
    if copygraph[start][0] is not []:
        opennode[start] = True
    while openode != {}:
        copygraph = graph
        x = start
        subpath = x
        for smer in opennode:#moves used degrees to end of degrees list
            if len(smer) == 4:
                copygraph[smer[0:2]][1].pop(smer[2:]) #moves outdegrees
                copygraph[smer[0:2]][1].append(smer[2:])
                copygraph[smer[2:]][0].pop(smer[0:2]) #moves indegrees
                copygraph[smer[2:]][0].append(smer[0:2])
        while copygraph[x][1] != []:
            
            x = copygraph[x][1]
            subpath = subpath + x[1]
            copygraph[x][1].pop(0)
            #if copygraph[x][1][0] in
            if copygraph[x][1] == []:
                if isinstance(x+copygraph[x][1][0],opennode):
                    opennode.pop(x+copygraph[x][1][0])
            elif copygraph[x][1] != []:
                opennode[x+copygraph[x][1][0]] = True
            copygraph[x][2] = len(copygraph[x][1])-len(copygraph[x][0])
            if isinstance(start,opennode):
                opennode.pop(start)
            #was figuring a way to tie balance into everything
