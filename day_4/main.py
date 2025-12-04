import copy

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
    
    return area[y][x] # y:row, x:element
    
    
def get_paper_roll(area: list) -> int:
    rolls_to_remove = []
    for y in range(len(area)):
        for x in range(len(area[0])):
            element_area = get_area(area, x, y)            
            if is_applicable(element_area) and area[y][x] == '@': # must be paper roll @ :D
                rolls_to_remove.append((x, y))
    return len(rolls_to_remove), rolls_to_remove

def get_until_replace_all_paper_rolls(area: list) -> int:
    
    area_to_apply = copy.deepcopy(area)
    total_replaced = 0
    
    while True:
        
        count_to_replace, rolls_to_replace = get_paper_roll(area_to_apply)
        
        if count_to_replace == 0:
            return total_replaced
        
        total_replaced += count_to_replace
        
        for x, y in rolls_to_replace:
            area_to_apply[y][x] = '.'
        