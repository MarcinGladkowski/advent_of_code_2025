def count_fresh_ingredients(fresh_range: list, ingredients: list[int]) -> str:
    
    fresh_ranges = [range(int(x.split('-')[0]), int(x.split('-')[1]) + 1) for x in fresh_range]
    
    count = 0
    for ingredient in map(int, ingredients):
        if any(is_fresh(fresh_range, ingredient) for fresh_range in fresh_ranges):
            count += 1
    return count


def is_fresh(fresh_range: range, ingredient: int) -> bool:
    return ingredient in fresh_range