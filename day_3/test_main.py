from main import *
from loader import load_data

def test_get_largest_voltage():
    assert get_largest_voltage("987654321111111") == '98'
    assert get_largest_voltage("811111111111119") == '89'
    assert get_largest_voltage("234234234234278") == '78'
    assert get_largest_voltage("818181911112111") == '92'
    
def test_calculate_max_voltage_sum():
    assert calculate_max_voltage_sum(["987654321111111", "811111111111119", "234234234234278", "818181911112111"]) == 98 + 89 + 78 + 92
    

def test_calculate_max_voltage_sum_for_first_challenge():
    assert calculate_max_voltage_sum(load_data("day_3/input.txt")) == 17142