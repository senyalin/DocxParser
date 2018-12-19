class Node(object):
    def __init__(self, name, data):
    	self.name = name
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

def save_tree(f, i, r, is_root=False):
    #Process children list
    if not is_root:
        i = i+'\t'
        #print i+'[size of children list:', len(ptr), ']'
        for child in r:
            if isinstance(child, Node):
                f.write(i+child.name+': '+child.data+'\n')
                if child.children:
                    save_tree(f, i, child.children)
                else:
                    continue
    #Process the root
    else:
        f = open('results/ommmltree.txt', mode='wt')
        if isinstance(r, Node):
            f.write(r.name+': '+r.data+'\n')
            if r.children:
                save_tree(f, i, r.children)
            f.close()

def print_tree(i, ptr, is_root=False):
    #Process children list
    if not is_root:
        i = i+'\t'
        #print i+'[size of children list:', len(ptr), ']'
        for child in ptr:
            if isinstance(child, Node):
                print i+child.name+': '+child.data
                if child.children:
                    print_tree(i, child.children)
                else:
                    continue
    #Process the root
    else:
        if isinstance(ptr, Node):
            print ptr.name+': '+ptr.data
            if ptr.children:
                print_tree(i, ptr.children)
#TEST Code by Jason
if __name__ == "__main__":
    obj = Node('root', 'father')
    objc = Node('node', 'child')
    objgc1 = Node('leaf_1', 'grand-child_1')
    objgc2 = Node('leaf_2', 'grand-child_2')
    obj.add_child(objc)
    objc.add_child(objgc1)
    obj.add_child(objgc2)
    indent = ''
    print_tree(indent, obj, True)