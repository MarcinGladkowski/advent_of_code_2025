def load_data(file: str) -> list[str]:
    with open(file) as f:
        return list(map(lambda x: x.replace("\n", ""), f.readlines()))

STARTING_POSITION_CONST = 50
LEFT_DIRECTION_CONST = "L"  
RIGHT_DIRECTION_CONST = "R"

def get_move_direction(instruction: str) -> str:
    return LEFT_DIRECTION_CONST if instruction.startswith("L") else RIGHT_DIRECTION_CONST

def get_move_count(instruction: str) -> int:
    return int(instruction[1:])

def move_left(curent_possition_count: int, move_count: int) -> tuple[int, int]  :
    
    full_circles = int(move_count / 100) if move_count > 100 else 0
        
    if curent_possition_count - move_count < 0 and curent_possition_count != 0:
        full_circles += 1
    
    move_count = move_count % 100 if move_count > 100 else move_count
    
    if move_count > curent_possition_count:
        return 100 - abs(curent_possition_count - move_count), full_circles
    
    return abs(curent_possition_count - move_count), full_circles

def move_right(curent_possition_count: int, move_count: int) -> tuple[int, int]:
    
    full_circles = int(move_count / 100) if move_count > 100 else 1
    
    if curent_possition_count + move_count > 100:      
        move_count = move_count % 100 if move_count > 100 else move_count
        
        if (curent_possition_count + move_count) > 100:
            return (curent_possition_count + move_count) - 100, full_circles
        
        return curent_possition_count + move_count, full_circles
    
    return curent_possition_count + move_count, 0


def count_ticks_at_zero(current_position: int, full_dial_circles: int) -> int:
    return 1 if current_position % 100 == 0 else 0


def count_all_dial_points(current_position: int, full_dial_circles: int) -> int:
    
    if full_dial_circles >= 1:
        return full_dial_circles
    
    return 1 if current_position % 100 == 0 else 0
    

def run(moves: list[str], counter_function: callable) -> int:
    current_position = STARTING_POSITION_CONST
    zero_counter = 0
    
    for move in moves:
        direction = get_move_direction(move)
        count = get_move_count(move)
                
        if direction == LEFT_DIRECTION_CONST:
            current_position, full_dial_circles = move_left(current_position, count)
        else:
            current_position, full_dial_circles = move_right(current_position, count)
        
        zero_counter += counter_function(current_position, full_dial_circles)
        
        
    return zero_counter


