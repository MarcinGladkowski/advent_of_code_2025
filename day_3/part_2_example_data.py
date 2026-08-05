from loader import load_data
from main import *

assert (3121910778619
        == calculate_max_voltage_sum_for_big_factor_from_chunks(load_data('test_input.txt')))