class Node:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parents = set()

    def add_child(self, child):
        self.children.add(child)

    def add_parent(self, parent):
        self.parents.add(parent)

# parse the nodes
nodes = {}
with open(r'C:\Users\jeremymill\Documents\AoC2018\7\input.txt') as f:
    for line in f:
        line = line.split(' ')
        nodename = line[1]
        child = line[7]
        #if the nodename doesn't exist, create it
        if nodename not in nodes:
            nodes[nodename] = Node(nodename)
            nodes[nodename].add_child(child)
        #if the nodename does exist, add a child to it
        else:
            nodes[nodename].add_child(child)
        #if the child isn't a node, create it and add a parent
        if child not in nodes:
            nodes[child] = Node(child)
            nodes[child].add_parent(nodename)
        #if the child is a node, just add a parent
        else:
            nodes[child].add_parent(nodename)

# find the node with no parents
# sort them, add the lowest root to eliminated children
# and the rest of the nodes to 'eligible' children
roots = []
for nodename, node in nodes.items():
    if len(node.parents) == 0:
        roots.append(nodename)
roots = sorted(roots)
print(roots)
#start with node C
eligible_children = []
eliminated_children = []
for root in roots:
    eligible_children.append(root)
print(eligible_children)

#start processing
# num workers
num_workers = 5
#num_workers = 2
ord_adjustment = 4
#ord_adjustment = 64
# result var
seconds = 0
results = ''
# store nodes in process, a map of name->time done:
in_process = {}
for root in eligible_children:
    in_process[root] = seconds + ord(root) - ord_adjustment
for keyname in in_process:
    eligible_children.remove(keyname)
print(seconds)
print(in_process)
while True:
    #exit condition
    if len(in_process) == 0:
        print('final is seconds: ', seconds)
        break
    seconds += 1
    print(seconds)    
    #see if any in_process are done
    todel = []
    for nodename, tdone in in_process.items():
        if tdone == seconds:
            results += nodename
            todel.append(nodename)
    for nodename in todel:
        #add the children of the finished node
        #to eligible children
        for child in nodes[nodename].children:
            if child not in eligible_children:
                eligible_children.append(child)
        #add the nodename to eliminated
        eliminated_children.append(nodename)
        # delete from in process
        del in_process[nodename]
    #early return if our workers are all busy
    available_workers = num_workers - len(in_process)
    if available_workers == 0:
        print(in_process)
        continue
    #since we're here, we have available workers
    for _ in range(0,available_workers):
        eligible_children = sorted(eligible_children)
        if len(eligible_children) == 0:
            break
        # from eligible children, get the next available
        # to be worked on
        count = 0
        while True:
            curr_count = count
            if count >= len(eligible_children):
                break
            for parent in nodes[eligible_children[count]].parents:
                if parent not in eliminated_children:
                    count += 1
                    break
            if curr_count == count:
                break
        # add the next eligible child to in process
        if count >= len(eligible_children):
            break
        in_process[eligible_children[count]] = seconds + ord(eligible_children[count]) - ord_adjustment
        eligible_children.remove(eligible_children[count])
    print(in_process)
#print(results)


