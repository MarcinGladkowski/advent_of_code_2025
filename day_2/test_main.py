from main import *

def test_invalid_repeated_ids():
    assert find_invalid_repeated_ids([11, 22]) == [11, 22]
    assert find_invalid_repeated_ids([99, 115]) == [99]
    assert find_invalid_repeated_ids([998, 1012]) == [1010]
    assert find_invalid_repeated_ids([1188511880, 1188511890]) == [1188511885]
    assert find_invalid_repeated_ids([222220, 222224]) == [222222]
    assert find_invalid_repeated_ids([1698522, 1698528]) == []
    assert find_invalid_repeated_ids([446443, 446449]) == [446446]
    assert find_invalid_repeated_ids([38593856, 38593862]) == [38593859]
    
def test_invalid_at_least_twice():
    assert find_invalid_repeated_ids_more_than_twice([11, 22]) == [11, 22]
    assert find_invalid_repeated_ids_more_than_twice([95, 115]) == [99, 111]
    assert find_invalid_repeated_ids_more_than_twice([998, 1012]) == [999, 1010]
    assert find_invalid_repeated_ids_more_than_twice([1188511880, 1188511890]) == [1188511885]
    assert find_invalid_repeated_ids_more_than_twice([222220, 222224]) == [222222]
    assert find_invalid_repeated_ids_more_than_twice([1698522, 1698528]) == []
    assert find_invalid_repeated_ids_more_than_twice([446443, 446449]) == [446446]
    assert find_invalid_repeated_ids_more_than_twice([38593856, 38593862]) == [38593859]
    assert find_invalid_repeated_ids_more_than_twice([565653, 565659]) == [565656]
    assert find_invalid_repeated_ids_more_than_twice([824824821, 824824827]) == [824824824]
    assert find_invalid_repeated_ids_more_than_twice([2121212118, 2121212124]) == [2121212121]
    
def test_invalid_find_pattern():
    assert find_repeat_pattern('1212121212') == True
    
def test_sum_invalid_ids_for_test_data():
    assert calculate_invalid_ids('day_2/test_input.txt') == 1227775554
    
def test_sum_invalid_ids_for_input_data():
    assert calculate_invalid_ids('day_2/input.txt') == 18595663903
    
def test_sum_invalid_repeated_ids_for_test_data():
    assert calculate_invalid_repeated_ids('day_2/test_input.txt') == 4174379265
    
    
print(calculate_invalid_repeated_ids('day_2/input.txt'))