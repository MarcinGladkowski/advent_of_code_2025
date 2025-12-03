from itertools import combinations

def get_largest_voltage(value: str, factor: int = 2):
    
    max_combination = 0
    combinations_list = combinations(value, factor)
    
    for combo in combinations_list:
        combination_value = int(''.join(combo))
        if combination_value > max_combination:
            max_combination = combination_value
    
    return str(max_combination)

def calculate_max_voltage_sum(values: list[str], factor: int = 2) -> int:
    return sum(map(lambda x: int(get_largest_voltage(x, factor)), values))
    