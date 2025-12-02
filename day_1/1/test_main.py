from main import *

def test_regognize_direction():
    assert get_move_direction("L10") == LEFT_DIRECTION_CONST
    assert get_move_direction("R5") == RIGHT_DIRECTION_CONST

def test_get_move_count():
    assert get_move_count("L10") == 10
    assert get_move_count("R5") == 5
    
def test_left_move():
    assert move_left(50, 68) == 82
    assert move_left(82, 30) == 52
    
def test_left_move():
    assert move_left(50, 68) == 82
    assert move_left(82, 30) == 52
    
def test_right_move():
    assert move_right(50, 68) == 18
    assert move_right(82, 30) == 12
    
def test_result_for_test_data():
    assert run(load_test_data(), count_ticks_at_zero) == 3
    
def test_result_for_input_data():
    print(f"Result for data: {run(load_data()), count_ticks_at_zero}")
    assert run(load_data()) == 1191
    