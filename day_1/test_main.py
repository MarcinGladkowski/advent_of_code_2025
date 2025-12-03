from main import *

def test_regognize_direction():
    assert get_move_direction("L10") == LEFT_DIRECTION_CONST
    assert get_move_direction("R5") == RIGHT_DIRECTION_CONST
    
def test_count_all_dial_points():
    assert count_all_dial_points(100, 0) == 1

def test_get_move_count():
    assert get_move_count("L10") == 10
    assert get_move_count("R5") == 5
    
def test_left_move():
    assert move_left(50, 68)[0] == 82
    assert move_left(82, 30)[0] == 52
    assert move_left(0, 1) == (99, 0)
    assert move_left(50, 1000) == (50, 10)
    assert move_left(50, 1020) == (30, 10)

def test_right_move():
    assert move_right(50, 68)[0] == 18
    assert move_right(82, 30)[0] == 12
    assert move_right(50, 1000)[0] == 50
    assert move_right(50, 1020) == (70, 10)
    assert move_right(50, 1068) == (18, 11)
        
def test_result_for_R1000_after_start():    
    assert run(['R1000'], count_all_dial_points) == 10

def test_result_for_test_data():
    assert run(load_data("test.txt"), count_ticks_at_zero) == 3
    
def test_result_for_input_data():
    assert run(load_data("input.txt"), count_ticks_at_zero) == 1191
    
# def test_count_all_dial_points_for_test_data():
#     assert run(load_data("test.txt"), count_all_dial_points) == 6
    
