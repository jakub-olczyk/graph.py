#/usr/bin/python
from graph import Graph

G = Graph()
G.add('A', ['B', 'C', 'E'])
G.add('B', ['A', 'D'])
G.add('C', ['A', 'F'])
G.add('D', ['B', 'F'])
G.add('E', ['A', 'F'])
G.add('F', ['D', 'C', 'E'])


print G
print "BFS:"
for i,v in enumerate(G.bfs(start='A')):
        print i, v
print "DFS:"
for i,v in enumerate(G.dfs(start='A')):
        print i, v
