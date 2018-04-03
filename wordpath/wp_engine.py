import logging

class WordPath(object):

    def __init__(self, file, sword="", eword=""):
        self.sword = sword
        self.eword = eword
        self.file = file

    def process(self):
        logging.debug("Starting Process")
        if len(self.sword) != len(self.eword): raise ValueError('Start and End words should have the same len()')
        wt = WordPathTools()
        #read all words from file
        wlist = wt.read_words(self.file, len(self.sword))
        logging.debug("Word list processed with ["+str(len(wlist))+"] words")

        graph = {}
        #build a dictionary with all nodes and vertices
        wt.build_graph(self.sword, self.eword, graph, wlist)

        logging.debug("Finding Path")
        path = []
        return wt.find_path(graph, self.sword, self.eword, path)

class WordPathTools(object):
    def diff_1_letter(self, s1="", s2=""):
        """ Returns a boolean value checking if 2 words have exactly 1 char different between them """
        if len(s1) != len(s2): return False

        diff = 0
        for a, b in zip(s1, s2):
            if a != b: diff += 1
            if diff > 1: return False

        if diff == 1: return True
        return False

    def read_words(self, file, size=0):
        """ read all words from fname file path and return in list """
        with open(file, 'r') as f:
            content = f.readlines()
        content = [x.strip().lower() for x in content if (len(x.strip()) == size)]  # lowercase n filtering by size and
        return list(set(content))  # removing duplicates

    def find_children(self, oword="", wlist=[]):
        """ return in a list all words 1 different char from wlist list """
        children = []
        for w in wlist:
            if self.diff_1_letter(oword, w): children.append(w)
        return children

    def build_graph(self, sword, eword, graph, wlist=[]):
        """ build a dictionary with nodes and list of vertices """
        logging.debug("starting to build Graph...")
        if sword not in wlist: wlist.append(sword)
        if eword not in wlist: wlist.append(eword)
        for w in wlist:
            if w not in graph.keys(): graph[w] = self.find_children(w, wlist)
        logging.debug("Graph finished")
        return graph

    def find_path(self, graph, start, end, path=[]):
        #
        # Recursively visit children nodes, returns the path found
        # Can be considerably improved with a implementation of A*
        # Decision taken considering deadline and not mention of shortest path as a requirement
        #
        path = path + [start]
        if start == end:
            return path
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None
