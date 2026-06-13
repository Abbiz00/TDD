from my_app.sum_list_app import sum_list

def test_sum_list():
    # Arrange
    expected = 6
    x = 3


    # Act
    actual   = sum_list(x)


    # Assert
    assert actual == expected