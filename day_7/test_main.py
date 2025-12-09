from loader import load_data
from main import find_starting_point, find_next_splitter

testing = load_data("day_7/test_input.txt")

def test_find_starting_point():
    assert find_starting_point(testing) == (2, 7)


def test_find_next_splitter():
    test_input = [
        '.......^.......',
        '...............',
        '......^.^......',
        '...............'
    ]     
    
    assert find_next_splitter((0, 7), test_input) == [(2, 6), (2, 8)]