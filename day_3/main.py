from itertools import combinations, permutations
from pprint import pprint

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
    
    
def mark_numbers(value: str, length: int = 12):    
    value = list(reversed(value))

    index_to_value = {n: { "value": int(x), "mark": False} for n, x in enumerate(value)}
    
    counter = 0
    
    for highest in reversed(range(1, 10)):
        for n in index_to_value:
            if index_to_value[n]['value'] == highest:
                index_to_value[n]['mark'] = True
                counter += 1
                
            if counter == length:
                break
    
    # get number back 
    return ''.join([str(v['value']) if v['mark'] == True else '' for x, v in index_to_value.items()])[::-1]