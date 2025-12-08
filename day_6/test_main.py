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


def load_data_part_2(file: str) -> list[str]:
    problems = {}
    with open(file) as f:
        # get last line and determine spaces
        lines = f.readlines()
        
        last_line = lines[-1]
        # spacing determines fill empty spaces
        # for last column do not remove 1 space
        spacing = re.findall("([\*|\+]\s+)", last_line)
        
        print(f"spacing: {spacing}")
        
        for line in lines:
            print(f"line: '{line}'")    
            for i, space in enumerate(spacing):
                print(line[i:len(space)-1])

    return problems


print(load_data_part_2('day_6/test_input.txt'))

def test_maching_spaces():
    matched = re.findall("([\*|\+]\s+)", "*   +   *   +  ")
    assert matched == ['*   ', '+   ', '*   ', '+  ']


def test_calculate():    
    assert 33210 == calculate({0: ['123', '45', '6', '*']})
    assert 4277556 == calculate(load_data('day_6/test_input.txt'))
    assert 3968933219902 == calculate(load_data('day_6/input.txt'))
