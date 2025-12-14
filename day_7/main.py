def find_starting_point(data: list[list[str]]) -> int:
    '''
        y row: + 2 from 0
        x el: entry point 'S'
    '''    
    return 2, data[0].index("S")

def find_next_splitter(starting: tuple[int, int], data: list[list[str]]):
    '''Split into two directions'''
    
    y, x = starting
    
    results = []
    
    for row_i in range(y, len(data), 2):
        if data[row_i][x-1] == "^":
            results.append((row_i, x-1))
            break
        
    for row_i in range(y, len(data), 2):
        if data[row_i][x+1] == "^":
            results.append((row_i, x+1))
            break
    
    return results
        
        
def find_all_splitters(starting: tuple[int, int], data: list[list[str]], splitters=None):

    if splitters is None:
        splitters = set()

    next_splitters = find_next_splitter(starting, data)
    
    for splitter in next_splitters:
        
        if splitter in splitters:
            continue
        
        splitters.add(splitter)
        find_all_splitters(splitter, data, splitters)
        
    # return unique splitters    
    return list(set(splitters))


class Node:
    def __init__(self, value: tuple[int, int], parent=None):
        self.parent = parent
        self.value = value
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)
        
        return child_node


def find_next_path(starting: tuple[int, int], data: list[list[str]] = None):
    '''Split into two directions'''
    
    y, x = starting
    
    results = []
    
    for row_i in range(y, len(data), 2):
        if data[row_i][x] == "^":
            results.append((row_i, x-1))
            results.append((row_i, x+1))

    
    return results
        

def find_splitting_paths(parent: Node, data: list[list[str]]):
    '''
    Instead to we creare tree with relations parent -> children (multiple)
    '''
    children = find_next_path(parent.value, data)
    
    for child in children:
        find_splitting_paths(parent.add_child(Node(child, parent)), data)
            
    return parent