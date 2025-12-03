
def load_test_data() -> list[str]:
    with open("test.txt") as f:
        return list(map(lambda x: x.replace("\n", ""), f.readlines()))

def load_data() -> list[str]:
    with open("input.txt") as f:
        return list(map(lambda x: x.replace("\n", ""), f.readlines()))

STARTING_POSITION_CONST = 50
LEFT_DIRECTION_CONST = "L"  
RIGHT_DIRECTION_CONST = "R"

def get_move_direction(instruction: str) -> str:
    return LEFT_DIRECTION_CONST if instruction.startswith("L") else RIGHT_DIRECTION_CONST

def get_move_count(instruction: str) -> int:
    return int(instruction[1:])

def move_left(curent_possition_count: int, move_count: int) -> int:
    
    if curent_possition_count - move_count < 0:
        return 100 + (curent_possition_count - move_count)
    
    return curent_possition_count - move_count

def move_right(curent_possition_count: int, move_count: int) -> int:
    
    if curent_possition_count + move_count > 100:
        return (curent_possition_count + move_count) - 100
    
    return curent_possition_count + move_count


def count_ticks_at_zero(current_position: int) -> int:
    return 1 if current_position % 100 == 0 else 0


def run(moves: list[str], counter_function: callable) -> int:
    current_position = STARTING_POSITION_CONST
    zero_counter = 0
    
    for move in moves:
        direction = get_move_direction(move)
        count = get_move_count(move)
        
        if direction == LEFT_DIRECTION_CONST:
            current_position = move_left(current_position, count)
        else:
            current_position = move_right(current_position, count)
        
        zero_counter += counter_function(current_position)
        
    return zero_counter


def count_all_points_zero(moves: list[str]) -> int:
    return run(moves)

