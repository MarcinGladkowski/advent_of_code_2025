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

def move_left(pointer: int, steps: int) -> tuple[int, int]  :
    
    full_dials = int(steps / 100) if steps > 100 else 0
    
    if steps > 100:
        steps = 0 if steps % 100 == 0 else steps % 100
    
    result = pointer - steps
    
    if result < 0:
        return 100 - abs(result), full_dials + (1 if pointer != 0 else 0) 
    
    return result, full_dials # position, full dials
        

def move_right(pointer: int, steps: int) -> tuple[int, int]:
    
    full_dials = int(steps / 100) if steps > 100 else 0
    
    if steps > 100:
        steps = 0 if steps % 100 == 0 else steps % 100
    
    result = pointer + steps
    
    if result == 100 and full_dials > 0:
        return 0, full_dials # 0 is not a full circle
    
    if result == 100:
        return 0, 0 # 0 is not a full circle
    
    if result > 100:
        return result - 100, full_dials + 1
    
    return result, full_dials # position, full dials
    

def count_ticks_at_zero(current_position: int, full_dial_circles: int) -> int:
    return 1 if current_position % 100 == 0 else 0

def count_all_dial_points(current_position: int, dials: int) -> int:

    zero_position = 1 if current_position % 100 == 0 else 0
    
    return dials + zero_position

    
def run(moves: list[str], counter_function: callable) -> int:
    pointer = STARTING_POSITION_CONST
    count_result = 0
    
    for move in moves:
        direction = get_move_direction(move)
        count = get_move_count(move)
                        
        if direction == LEFT_DIRECTION_CONST:
            pointer, dials = move_left(pointer, count)
        else:
            pointer, dials = move_right(pointer, count)
            
        result = counter_function(pointer, dials)    
        count_result += result
        
    return count_result


