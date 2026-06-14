from my_app.second_largest import find_second_max

def test_empty_list():
    assert find_second_max([]) == None

def test_single_element():
    assert find_second_max([5]) == None

def test_four_elements():
    assert find_second_max([1, 2, 3, 9]) == 3

def test_negative_numbers():
    assert find_second_max([-5, -2, -9]) == -5

def test_mixed_positive_negative():
    assert find_second_max([-3, 7, -1, 4]) == 4

def test_duplicate():
    assert find_second_max([4, 4, 9, 2]) == 4

def test_all_equal():
    assert find_second_max([3, 3, 3]) == 3

def test_floats():
    assert find_second_max([1.5, 2.7, 2.6]) == 2.6