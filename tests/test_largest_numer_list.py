from my_app.largest_number import find_max

def test_empty_list():
    assert find_max([]) == None

def test_single_element():
    assert find_max([5]) == 5

def test_max():
    assert find_max([1, 2, 3, 9]) == 9

def test_negative_numbers():
    assert find_max([-5, -2, -9]) == -2

def test_mixed_positive_negative():
    assert find_max([-3, 7, -1, 4]) == 7

def test_duplicate_max():
    assert find_max([4, 9, 9, 2]) == 9

def test_all_equal():
    assert find_max([3, 3, 3]) == 3

def test_floats():
    assert find_max([1.5, 2.7, 2.6]) == 2.7