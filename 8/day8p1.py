class Namegetter:
    def __init__(self):
        self._letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._current_nodeindex = 0
        self._current_nodenum = 0
    
    def get_name(self):
        nodename = self._letters[self._current_nodeindex] + str(self._current_nodenum)
        self._current_nodeindex = (self._current_nodeindex + 1) % len(self._letters)
        if self._current_nodeindex == 0:
            self._current_nodenum += 1
        return nodename

class Node:
    def __init__(self, name, parent, num_children, num_metas):
        self.name = name
        self.parent = parent
        self.num_children = num_children
        self.num_metas = num_metas
        self.children = []
        self.metadatas = []

    def add_child(self, child):
        self.children.append(child)

    def add_metadata(self, metadata):
        self.metadatas.append(metadata)


#get a node name
def get_nodename(current_nodeindex, current_nodenum, letters):
    nodename = letters[current_nodeindex] + str(current_nodenum)
    current_nodeindex = (current_nodeindex + 1) % len(letters)
    if current_nodeindex == 0:
        current_nodenum += 1
    return nodename

    

def process_nodes(namegetter, parent, num_children, num_metadata, line, index):
    node = Node(namegetter.get_name(), parent, num_children, num_metadata)
    for _ in range(0, num_children):
        index, child = process_nodes(namegetter, node, int(line[index]), int(line[index+1]), line, index+2)
        node.add_child(child)
    for metaindex in range(index, index + num_metadata):
        node.add_metadata(int(line[metaindex]))
    return index+num_metadata, node

def add_metas(node):
    # if we don't have any children, just add the metadatas and return it
    if len(node.children) == 0:
        metasum = 0
        for meta in node.metadatas:
            metasum += meta
        return metasum
    #if we do have metadata, get the sum from each of the children
    metasum = 0
    for child in node.children:
        metasum += add_metas(child)
    #and our metadata and return it
    for meta in node.metadatas:
        metasum += meta
    return metasum



namegetter = Namegetter()
root = None
with open(r'C:\Users\jeremymill\Documents\AoC2018\8\input.txt') as f:
    for line in f:
        line = line.split(' ')
        index, root = process_nodes(namegetter, None, int(line[0]), int(line[1]), line, 2)
metasum = add_metas(root)
print('done. Sum: ', metasum)

