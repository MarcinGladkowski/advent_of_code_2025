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

def calculate_invalid_ids(source_file: str) -> int:    
    number_ranges = list(map(lambda x: (int(x.split('-')[0]), int(x.split('-')[1])), load_data(source_file)))
    
    results = [sum(find_invalid_repeated_ids(x)) for x in number_ranges]
    
    return sum(results)