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