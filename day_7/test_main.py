from loader import load_data
from main import find_starting_point, find_next_splitter, find_all_splitters

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

def test_find_next_splitters_recursively():
    test_input = [
        '.......^.......',
        '...............',
        '......^.^......',
        '...............'
    ]     
    
    assert find_all_splitters((0, 7), test_input) == [(2, 6), (2, 8)]
    
def test_find_next_splitters_none_next():
    test_input = [
        '.......^.......',
        '...............',
        '......^........',
        '...............'
    ]     
    
    assert find_all_splitters((0, 7), test_input) == [(2, 6)]

def test_find_all_splitters_for_testing_data():
    assert 21 == len(find_all_splitters((0, 7), testing)) + 1 # starting point
    
# 1603 is too high
print("### Part 1 ###")
print(len(find_all_splitters((2, 71), load_data("day_7/input.txt"))) + 1)