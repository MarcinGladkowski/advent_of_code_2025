from loader import load_data, list_transformer
from main import *

example_data = list_transformer(load_data('day_4/test_input.txt'))
task_data = list_transformer(load_data('day_4/input.txt'))


def test_return_begging_area():
    start_area = get_area(example_data, 0, 0)

    assert 8 == len(start_area)
    assert 3 == len(list(filter(lambda x: x is not None, start_area)))
    
def test_return_is_applicable_true():
    assert is_applicable(get_area(example_data, 2, 0)) is True
    assert is_applicable(get_area(example_data, 3, 0)) is True
    assert is_applicable(get_area(example_data, 5, 0)) is True
    assert is_applicable(get_area(example_data, 6, 0)) is True
    assert is_applicable(get_area(example_data, 8, 0)) is True
    assert is_applicable(get_area(example_data, 0, 1)) is True
    assert is_applicable(get_area(example_data, 6, 2)) is True
    assert is_applicable(get_area(example_data, 0, 4)) is True
    assert is_applicable(get_area(example_data, 9, 4)) is True
    assert is_applicable(get_area(example_data, 0, 7)) is True
    assert is_applicable(get_area(example_data, 0, 9)) is True
    assert is_applicable(get_area(example_data, 2, 9)) is True
    assert is_applicable(get_area(example_data, 8, 9)) is True
    
def test_count_all_applicable():
    assert get_paper_roll(example_data)[0] == 13
    assert get_paper_roll(task_data)[0] == 1478
    
def test_count_all_replaces_rolls():
    assert get_until_replace_all_paper_rolls(example_data) == 43



print(get_until_replace_all_paper_rolls(task_data))