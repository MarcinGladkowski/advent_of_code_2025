from loader import load_data
from pathlib import Path
from main import *


result = calculate_max_voltage_sum_for_big_factor(load_data('input.txt'))

# too low: 146804855762104
print(f"total sum: {result}")