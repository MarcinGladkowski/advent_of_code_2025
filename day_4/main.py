def get_area(area: list, x: int, y: int) -> list[str]:
    return [
        get_key_area(area, x-1, y-1),
        get_key_area(area, x, y-1),
        get_key_area(area, x+1, y-1),
        get_key_area(area, x-1, y),
        get_key_area(area, x+1, y),
        get_key_area(area, x-1, y+1),
        get_key_area(area, x, y+1),
        get_key_area(area, x+1, y+1),
    ]
    
def is_applicable(elements: list[str], less_than: int = 4) -> bool:
    return len(list(filter(lambda x: x == '@', elements))) < less_than
    
def get_key_area(area: list, x: int, y: int) -> list[str]:
    
    if (x < 0) or (y < 0):
        return None
    
    if (x >= len(area[0])) or (y >= len(area)):
        return None
        
    try:
        return area[y][x] # y:row, x:element
    except IndexError:
        return None
    

def get_paper_roll(area: list) -> int:
    count = 0
    for y in range(len(area)):
        for x in range(len(area[0])):
            if is_applicable(get_area(area, x, y)):
                count += 1
    return count   