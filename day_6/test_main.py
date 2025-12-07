from main import calculate

def load_data(file: str) -> list[str]:
    problems = {}
    with open(file) as f:
        for line in f.readlines():
            elements = list(filter(lambda x: x != "", line.replace("\n", "").split(" ")))
            for i, el in enumerate(elements):
                problems.setdefault(i, []).append(el)

    return problems


def test_calculate():    
    assert 33210 == calculate({0: ['123', '45', '6', '*']})
    assert 4277556 == calculate(load_data('day_6/test_input.txt'))
    assert 3968933219902 == calculate(load_data('day_6/input.txt'))
