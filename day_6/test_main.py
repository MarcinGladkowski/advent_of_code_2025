from tokenize import group
from main import calculate
import re

def load_data(file: str) -> list[str]:
    problems = {}
    with open(file) as f:
        for line in f.readlines():
            elements = list(filter(lambda x: x != "", line.replace("\n", "").split(" ")))
            for i, el in enumerate(elements):
                problems.setdefault(i, []).append(el)

    return problems

def recognize_spacing(line: str) -> list[str]:
    spacing = re.findall("([\*|\+]\s+)", line)
    return "".join([f"(.{{{len(space)}}})" for space in spacing])

def spacing_lengts(line: str) -> list[int]:
    return [len(space)-1 for space in re.findall("([\*|\+]\s+)", line)]

def load_data_part_2(file: str) -> list[str]:
    problems = {}
    with open(file) as f:
        # get last line and determine spaces
        lines = f.readlines()
        
        last_line = lines[-1]
        
        regex_pattern = recognize_spacing(last_line)
        
        operators = last_line.replace(" ", "")
        
        for i, line in enumerate(lines):
            
            if i == len(lines) - 1:
                break
            
            for j, group_number in enumerate(re.match(regex_pattern, line).groups()):
                problems.setdefault(j, []).append(group_number.rstrip())
        
        for i, el in problems.items():
            problems[i] = [] 
            for x, number in enumerate(el):
                for j, n in enumerate(number):
                    try:
                        problems[i][j]
                    except IndexError:
                        problems[i].append(n)
                        continue   
                    problems[i][j] += n
                    
        for key, numbers in problems.items():
            numbers.append(operators[key])
                                
    return problems


def test_is_maching_spaces():
    assert "(.{4})(.{3})(.{3})(.{4})" == recognize_spacing("*   *  *  +   ")
    
def test_get_row_by_pattern():
    matches = re.match("(.{4})(.{3})(.{3})(.{4})", '1   95 97 1177')
    assert ('1   ', '95 ', '97 ', '1177') == matches.groups()
    
def test_fill_missing_spaces():
    # 2 is coming from space 4 - 1
    testing = '1   '
    replacing = len(list(filter(lambda x: x != ' ', testing)))
    assert '1xx' == testing.replace(' ', 'x', 4 - replacing - 1).replace(' ', '')
    
def test_calculate():    
    assert 33210 == calculate({0: ['123', '45', '6', '*']})
    assert 4277556 == calculate(load_data('day_6/test_input.txt'))
    assert 3263827 == calculate(load_data_part_2('day_6/test_input.txt'))
    assert 3968933219902 == calculate(load_data('day_6/input.txt'))
    assert 6019576291014 == calculate(load_data_part_2('day_6/input.txt'))