from main import *
from loader import load_data

test_data = load_data('day_5/test_input.txt')

def split_data(data: list[str]) -> list:
    separator = data.index('')
    fresh_ingredients_ranges = data[:separator]
    ingredients = data[separator + 1:]
    
    return fresh_ingredients_ranges, ingredients


def test_ingredient_is_fresh():
    assert is_fresh(range(3, 5), 3) is True
    assert is_fresh(range(3, 5), 1) is False

def test_split_input_data():
    fresh_ranges, ingredients = split_data(test_data)
    
    assert fresh_ranges == ['3-5', '16-20', '12-18', '10-14']
    assert ingredients == ['1', '5', '8', '11', '17', '32']
    
def test_count_fresh_ingredients():
    fresh_ranges, ingredients = split_data(test_data)
    assert count_fresh_ingredients(fresh_ranges, ingredients) == 3
    
def test_input_data():
    fresh_ranges, ingredients = split_data(load_data('day_5/input.txt'))
    assert count_fresh_ingredients(fresh_ranges, ingredients) == 635
    
def test_considered_as_fresh():
    fresh_ranges, _ = split_data(test_data)
    assert considered_as_fresh(fresh_ranges) == 14
    assert considered_as_fresh(['10-15']) == 6
    assert considered_as_fresh(['10-15', '20-30']) == 17
    assert considered_as_fresh(['10-15', '11-14', '20-30']) == 17
    assert considered_as_fresh(['10-15', '1-20']) == 20
    assert considered_as_fresh(['10-15', '5-20']) == 16
    assert considered_as_fresh(['5-20', '10-15']) == 16
    assert considered_as_fresh(['5-20', '10-30']) == 26
    assert considered_as_fresh(['10-10', '10-10']) == 1
    
    
# def test_considered_as_fresh_input():
#     fresh_ranges, _ = split_data(load_data('day_5/input.txt'))
#     result = considered_as_fresh(fresh_ranges)
#     print(f"\nResult for input: {result}")
#     assert result > 341494366700450 # Must be higher than this
#     assert result < 370349436553190