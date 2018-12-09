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
# find the node with no parent
roots = []
for nodename, node in nodes.items():
    if len(node.parents) == 0:
        roots.append(nodename)
roots = sorted(roots)
print(roots)
#start with node C
eligible_children = []
eliminated_children = [roots[0]]
for child in nodes[roots[0]].children:
    print('root child: ', child)
    eligible_children.append(child)
for root in roots[1:]:
    eligible_children.append(root)
#result variable
result = roots[0]
print("e-children: ", eligible_children)
while len(eligible_children) > 0:
    #sort alphabetically
    eligible_children = sorted(eligible_children)
    #make sure the next lowest eligible has eliminated parents
    count = 0
    childzero = eligible_children[0]
    while True:
        curr_count = count
        for parent in nodes[eligible_children[count]].parents:
            if parent not in eliminated_children:
                count += 1
                break
        if curr_count == count:
            break
    #add the lowest eligible to the result
    result += eligible_children[count]
    eliminated_children.append(eligible_children[count])
    #add the children of the lowest to eligible children
    for child in nodes[eligible_children[count]].children:
        if child not in eliminated_children:
            eligible_children.append(child)
    #remove the child
    eligible_children.remove(eligible_children[count])
    eligible_children = set(eligible_children)
    print("e-children: ", eligible_children)
print(result)

