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
    
    assert fresh_ranges == ['3-5', '10-14', '16-20', '12-18']
    assert ingredients == ['1', '5', '8', '11', '17', '32']
    
def test_count_fresh_ingredients():
    fresh_ranges, ingredients = split_data(test_data)
    assert count_fresh_ingredients(fresh_ranges, ingredients) == 3
    
def test_input_data():
    fresh_ranges, ingredients = split_data(load_data('day_5/input.txt'))
    assert count_fresh_ingredients(fresh_ranges, ingredients) == 635