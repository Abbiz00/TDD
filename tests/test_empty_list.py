from my_app.sum_list_app import empty_list

def test_empty_list():
    # Arrange
    expected = None

    # Act
    actual   = empty_list()

    # Assert
    assert actual == expected