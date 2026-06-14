from my_app.sum_list_app  import number_list

def test_sum_list_5():
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    expected = 15

    # Act
    actual = number_list(numbers)

    # Assert
    assert number_list([1, 2, 3, 4, 5]) == 15
    assert actual == expected


def test_sum_list_2():
    numbers = [5,2]
    expected = 7

    # Act
    actual = number_list(numbers)

    # Assert
    assert number_list([5, 2]) == 7
    assert actual == expected


def test_sum_list_1():
    numbers = [5]
    expected = 5

    # Act
    actual   = number_list(numbers)

    # Assert
    assert number_list([5]) == 5
    assert actual == expected


