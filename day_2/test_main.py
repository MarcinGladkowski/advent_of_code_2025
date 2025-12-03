from main import find_invalid_repeated_ids, calculate_invalid_ids

def test_invalid_repeated_ids():
    assert find_invalid_repeated_ids([11, 22]) == [11, 22]
    assert find_invalid_repeated_ids([99, 115]) == [99]
    assert find_invalid_repeated_ids([998, 1012]) == [1010]
    assert find_invalid_repeated_ids([1188511880, 1188511890]) == [1188511885]
    assert find_invalid_repeated_ids([222220, 222224]) == [222222]
    assert find_invalid_repeated_ids([1698522, 1698528]) == []
    assert find_invalid_repeated_ids([446443, 446449]) == [446446]
    assert find_invalid_repeated_ids([38593856, 38593862]) == [38593859]
    
def test_sum_invalid_ids_for_test_data():
    assert calculate_invalid_ids('day_2/test_input.txt') == 1227775554
    
def test_sum_invalid_ids_for_input_data():
    print(f"\nResult: {calculate_invalid_ids('day_2/input.txt')}")
    assert True