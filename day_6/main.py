from functools import reduce
from operator import mul, add

def calculate(problems: dict[int, list[str]]) -> int:
    total = 0
    available_operations = {
        '*': mul, 
        '+': add,
    }
    
    total = 0
    for _, problem_list in problems.items():
        total += reduce(available_operations[problem_list[-1]], map(int, problem_list[:-1]))
        
    return total