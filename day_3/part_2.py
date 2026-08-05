from loader import load_data
from main import *


result = calculate_max_voltage_sum_for_big_factor_from_chunks(load_data('input.txt'))

# too low: 146804855762104
# too low  167469726540999
print(f"total sum: {result}")