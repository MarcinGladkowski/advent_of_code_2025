def count_fresh_ingredients(fresh_range: list, ingredients: list[int]) -> str:
    
    fresh_ranges = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1) for x in fresh_range]
    
    count = 0
    for ingredient in map(int, ingredients):
        if any(is_fresh(fresh_range, ingredient) for fresh_range in fresh_ranges):
            count += 1
    return count


def is_fresh(fresh_range: range, ingredient: int) -> bool:
    return ingredient in fresh_range


def is_fully_inclusive(current_ranges: list[range], new_range: range) -> bool:
    for current_range in current_ranges:
        if current_range.start <= new_range.start and current_range.stop >= new_range.stop:
            return True
    return False
    

def left_overlapping(current_ranges: list[range], new_range: range) -> range|bool:
    for i, current_range in enumerate(current_ranges):
        if current_range.start < new_range.start and current_range.stop >= new_range.start:
            return i, range(current_range.start, new_range.stop)
    return False

def right_overlapping(current_ranges: list[range], new_range: range) -> range|bool:
    for i, current_range in enumerate(current_ranges):
        if current_range.start >= new_range.start and current_range.stop > new_range.stop:
            return i, range(new_range.start, current_range.stop)
    return False


def is_fully_overlapping(current_ranges: list[range], new_range: range) -> range|bool:
    for i, current_range in enumerate(current_ranges):
        if current_range.start >= new_range.start and current_range.stop <= new_range.stop:
            return i, range(new_range.start, new_range.stop)
    return False


def considered_as_fresh(fresh_range: list):
    fresh_ranges = [range(int(x.split('-')[0]), int(x.split('-')[1])) for x in fresh_range]
    
    print(f"ranges to test {fresh_ranges}")
    
    fresh_ranges.sort(key=lambda r: r.start)
    
    print(f"sorted ranges to test {fresh_ranges}")
    
    ranges = []
    for i, fresh_range in enumerate(fresh_ranges):
        
                
        if i == 0:
            ranges.append(fresh_range)
            continue
            
        if is_fully_inclusive(ranges, fresh_range) is True:
            print(f"Range {fresh_range} is fully inclusive in {ranges}, skipping")
            continue
        
        # is fully wider than
        if is_fully_overlapping(ranges, fresh_range) is not False:
            index, new_range = is_fully_overlapping(ranges, fresh_range)
            print(f"fully overlapping found, merging {ranges[index]} and {fresh_range} into {new_range}")
            ranges[index] = new_range
            continue
        
        if left_overlapping(ranges, fresh_range) is not False:
            index, new_range = left_overlapping(ranges, fresh_range)
            print(f"left overlapping found, merging {ranges[index]} and {fresh_range} into {new_range}")
            ranges[index] = new_range
            continue
        
        if right_overlapping(ranges, fresh_range) is not False:
            index, new_range = right_overlapping(ranges, fresh_range)
            print(f"right overlapping found, merging {ranges[index]} and {fresh_range} into {new_range}")
            ranges[index] = new_range
            continue
        
        print(f"Adding range {fresh_range}")
        ranges.append(fresh_range)
    
    print("Final ranges:")
    total = 0
    for r in ranges:
        total += len(r) + 1
        print(f"Range from {r.start} to {r.stop} (len: {len(r) + 1})")
 
    return sum([len(x) + 1 for x in ranges])
