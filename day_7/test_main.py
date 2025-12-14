from logging import root
from unittest import result
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

def unpack_unique_leafs(root_node: Node, leafs=None):
    
    if leafs is None:
        leafs = []
    
    if root_node.parent is not None:
        print(root_node.parent.value, '->' , root_node.value)
    
    if root_node.parent is None:
        print("\nROOT:", root_node.value)
    
    if not root_node.children:
        print(root_node.value, "is LEAF")
        leafs.append(root_node.value)
    
    for child in root_node.children:
        unpack_unique_leafs(child, leafs=leafs)    

    return leafs

def test_find_path_for_two_splitters():
    
    test_input = [
        '.......S.......',
        '...............',
        '.......^.......',
        '...............',
        '......^.^......',
        '...............'
    ]
    
    tree_result = find_splitting_paths(Node((0, 7)), test_input)

    # assert 4 == len(unpack_unique_leafs(tree_result))
    assert isinstance(tree_result, Node)
    
    
    
# print(len(unpack_unique_leafs(find_splitting_paths(Node((0, 7)), testing))))