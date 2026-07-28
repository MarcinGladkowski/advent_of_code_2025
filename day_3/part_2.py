from loader import load_data
from pathlib import Path
from main import *

result = calculate_max_voltage_sum_for_big_factor(load_data(Path('day_3/input.txt').resolve()))

print(result)