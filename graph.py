#!/usr/bin/python
import collections

class Graph():

    """ This class implements proof of concept graph class with different
    iterators for DFS and BFS
    
    Graph is implemented using adjacency lists, as in this suggestion:
    https://www.python.org/doc/essays/graphs/
    """

    class __dfs_iter():
        """ This class implements the Depth-First Search iterator"""

        def __init__(self, graph, start_v=None):
            self.graph = graph
            self.visited = {} # faster 'in' operation
            self.stack = []
            if not start_v:
                self.stack.append( self.graph._collection.keys()[0])
            else:
                self.stack.append(start_v)

        def __iter__(self):
            return self
        
        def next(self):
            while len(self.stack):
                vertex = self.stack.pop()
                if vertex not in self.visited:
                    self.visited[vertex] = None
                    for n in self.graph._collection[vertex]:
                        self.stack.append(n)
                    break
            else:
                raise StopIteration()

            return vertex

    class __bfs_iter():
        """ This class implements the Breadth-First Search iterator"""
        def __init__(self, graph, start_v=None):

            self.graph = graph
            self.visited = {} # faster 'in' operation
            self.fifo = collections.deque()
            if not start_v:
                self.fifo.append( self.graph._collection.keys()[0])
            else:
                self.fifo.append(start_v)

        def __iter__(self):
            return self
        
        def next(self):
            while len(self.fifo):
                vertex = self.fifo.popleft()
                if vertex not in self.visited:
                    self.visited[vertex] = None
                    for n in self.graph._collection[vertex]:
                        self.fifo.append(n)
                    break
            else:
                raise StopIteration()

            return vertex


    def __init__(self):
        self._collection = {}

    def __repr__(self):
        return "Graph("+repr(self._collection)+")"

    def _connect(self):
        for v in self._collection.keys():
            for e in self._collection[v]:
                if v not in self._collection[e]:
                    self._collection[e].append(v)


    def add(self, vertex, neighbours):
        """ vertex is the label of the vertex
            neighbours is the list of other vertex labels
            Warning : neighbours must be a list!
        """

        assert type(neighbours) is list
        self._collection[vertex] = neighbours

        # create the neighbours for me (useful for maintaining consistent state)
        for n in neighbours:
            if n not in self._collection:
                self._collection[n] = [vertex]
            else:
                if vertex not in self._collection[n]:
                    self._collection[n].append(vertex)
        self._connect()

    def remove(self, vertex):
        del self._collection[vertex]
        for v in self._collection:
            if vertex in self._collection[v]:
                self._collection[v].remove(vertex)


    def dfs(self, start=None):
        """ returns the dfs iterator for the graph"""
        return self.__dfs_iter(self, start_v=start)

    def bfs(self, start=None):
        """ returns the dfs iterator for the graph"""
        return self.__bfs_iter(self, start_v=start)


