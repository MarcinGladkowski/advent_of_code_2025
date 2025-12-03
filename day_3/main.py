from itertools import combinations

def get_largest_voltage(value: str):
    return str(max(list(map(lambda x: int(x[0] + x[1]), combinations(value, 2)))))

def calculate_max_voltage_sum(values: list[str]) -> int:
    return sum(map(lambda x: int(get_largest_voltage(x)), values))
    