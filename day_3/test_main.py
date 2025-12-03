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
    
def test_get_largest_voltage_for_factor_twelve():
    assert get_largest_voltage("987654321111111", 12) == '987654321111'
    assert get_largest_voltage("234234234234278", 12) == '434234234278'
    
  
print(calculate_max_voltage_sum(['2252522232121122125212322341424262435212421332333533223124122242222222112222222222423222112211212132'], 12))    
# full_data = load_data("day_3/input.txt")
# total = 0
# n = 1
# for i in range(0, len(full_data)+1, n):
#     total += calculate_max_voltage_sum(full_data[i:i+n], 12)
#     print(total)
