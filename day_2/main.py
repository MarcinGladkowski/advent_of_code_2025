import re

def load_data(file: str) -> list[str]:
    with open(file) as f:
        return f.readline().strip().split(',')

def find_invalid_repeated_ids(id_range: tuple[int]):
    invalid_ids = []
    for range_number in range(id_range[0], id_range[1] + 1):
        
        value = str(range_number)
        
        first_half = value[:len(value)//2]
        second_half = value[len(value)//2:]
        
        if first_half == second_half:
            invalid_ids.append(range_number)
        
    return invalid_ids

def find_repeat_pattern(value: str) -> bool:    
    for i in range(1, len(value) + 1):
        pattern = value[:i]
        result = re.findall(pattern, value)
        
        if len(result) >= 2 and ''.join(result) == value:
            return True
    
    return False

def find_invalid_repeated_ids_more_than_twice(id_range: tuple[int]):
    invalid_ids = []
    for range_number in range(id_range[0], id_range[1] + 1):
        if find_repeat_pattern(str(range_number)):
            invalid_ids.append(range_number)
        
    return invalid_ids


def calculate_invalid_ids(source_file: str) -> int:    
    number_ranges = list(map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), load_data(source_file)))
    results = [sum(find_invalid_repeated_ids(x)) for x in number_ranges]
    
    return sum(results)

def calculate_invalid_repeated_ids(source_file: str) -> int:    
    number_ranges = list(map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), load_data(source_file)))
    results = [sum(find_invalid_repeated_ids_more_than_twice(x)) for x in number_ranges]
    
    return sum(results)