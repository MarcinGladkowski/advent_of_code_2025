from pprint import pprint
from loader import load_data
from main import Node, find_starting_point, find_next_splitter, find_all_splitters, find_splitting_paths

testing = load_data("day_7/test_input.txt")

# def test_find_starting_point():
#     assert find_starting_point(testing) == (2, 7)

# def test_find_next_splitter():
#     test_input = [
#         '.......^.......',
#         '...............',
#         '......^.^......',
#         '...............'
#     ]     
    
#     assert find_next_splitter((0, 7), test_input) == [(2, 6), (2, 8)]

# def test_find_next_splitters_recursively():
#     test_input = [
#         '.......^.......',
#         '...............',
#         '......^.^......',
#         '...............'
#     ]     
    
#     assert find_all_splitters((0, 7), test_input) == [(2, 6), (2, 8)]
    
# def test_find_next_splitters_none_next():
#     test_input = [
#         '.......^.......',
#         '...............',
#         '......^........',
#         '...............'
#     ]     
    
#     assert find_all_splitters((0, 7), test_input) == [(2, 6)]

# def test_find_all_splitters_for_testing_data():
#     assert 21 == len(find_all_splitters((0, 7), testing)) + 1 # starting point
    
    
# def test_find_all_splitters_for_full_data():
#     assert 1602 == len(find_all_splitters((2, 71), load_data("day_7/input.txt")))

def unpack_paths(root_node: Node, paths=None):
    
    if paths is None:
        paths = []
    
    if root_node.parent is not None:
        paths.append(root_node.value)
    
    if root_node.parent is None:
        paths.append(root_node.value)
    
    for child in root_node.children:
        unpack_paths(child, paths=paths)

    return paths

def test_find_path_for_two_splitters():
    # 4 unique paths expected
    test_input = [
        '.......S.......',
        '...............',
        '.......^.......',
        '...............',
        '......^.^......', # for last step
        '...............'
    ]
    
    tree_result = find_splitting_paths([Node((0, 7))], test_input)
    
    assert 4 == len(tree_result)
    

def test_find_path_for_testing_data():
    tree_result = find_splitting_paths([Node((0, 7))], testing)
    
    # remove duplicates ?
    
    
    print("TREE RESULT")
    pprint(tree_result)
    
    assert True
    