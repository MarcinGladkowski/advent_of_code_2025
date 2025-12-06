def count_fresh_ingredients(fresh_range: list, ingredients: list[int]) -> str:
    
    fresh_ranges = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1) for x in fresh_range]
    
    count = 0
    for ingredient in map(int, ingredients):
        if any(is_fresh(fresh_range, ingredient) for fresh_range in fresh_ranges):
            count += 1
    return count


def is_fresh(fresh_range: range, ingredient: int) -> bool:
    return ingredient in fresh_range


def considered_as_fresh(fresh_range: list):
    fresh_ranges = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1) for x in fresh_range]
    
    fresh_ranges.sort(key=lambda r: r.start)
    
    print(f"\n{fresh_ranges}")
    
    range_ingredients_count = 0
    for i, fresh_range in enumerate(fresh_ranges):
        if i == 0:
            range_ingredients_count = len(fresh_range)
            print(f"First range: {fresh_range}, adding {len(fresh_range)}")
            continue
        
        previous_fresh_range = fresh_ranges[i - 1]
              
        # no overlap from left side
        if previous_fresh_range.start < fresh_range.start and previous_fresh_range.stop < fresh_range.start:
            range_ingredients_count += len(fresh_range)
            continue
        
        # full inclusion
        if previous_fresh_range.start >= fresh_range.start and previous_fresh_range.stop <= fresh_range.stop:
            continue
    
        # partial overlap from left side
        if previous_fresh_range.start < fresh_range.start and previous_fresh_range.stop <= fresh_range.stop:
            range_ingredients_count += fresh_range.stop - previous_fresh_range.stop
            print(f"Left overlap: {fresh_range}, {previous_fresh_range}, adding {fresh_range.stop - previous_fresh_range.stop}")
            continue
        
        # partial overlap from right side
        if previous_fresh_range.start >= fresh_range.start and previous_fresh_range.stop > fresh_range.stop:
            range_ingredients_count += previous_fresh_range.start - fresh_range.start
            print(f"Right overlap: {fresh_range}, {previous_fresh_range}, adding {previous_fresh_range.start - fresh_range.start}")
            continue
        
        if previous_fresh_range.start < fresh_range.start and previous_fresh_range.stop > fresh_range.stop:
            # full outside inclusion
            print(f"FULL OUTSIDE CASE: {fresh_range}, {previous_fresh_range}")
            # range_ingredients_count
            continue
        
        # no overlap
        print(f"NO OVERLAP CASE: {fresh_range}, {previous_fresh_range}")
        range_ingredients_count += len(fresh_range)    
        
        
    return range_ingredients_count
