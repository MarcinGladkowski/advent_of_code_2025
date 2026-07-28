from main import *

def test_get_largest_voltage():
    assert get_largest_voltage("987654321111111") == '98'
    assert get_largest_voltage("811111111111119") == '89'
    assert get_largest_voltage("234234234234278") == '78'
    assert get_largest_voltage("818181911112111") == '92'
    
    assert get_largest_voltage("987654321111111", 12) == '987654321111'
    assert get_largest_voltage("811111111111119", 12) == '811111111119'
    assert get_largest_voltage("234234234234278", 12) == '434234234278'
    assert get_largest_voltage("818181911112111", 12) == '888911112111'

def test_get_largest_by_alghoritm():
    assert mark_numbers('818181911112111', 12) == '888911112111'
    assert mark_numbers('987654321111111', 12) == '987654321111'
    assert mark_numbers('811111111111119', 12) == '811111111119'
    assert mark_numbers('234234234234278', 12) == '434234234278'
    
def test_get_largest_for_12_digit_number():
    assert 12 == len(mark_numbers('2252522232121122125212322341424262435212421332333533223124122242222222112222222222423222112211212132'))    