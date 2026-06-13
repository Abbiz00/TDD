from my_app.search import add, compare_names
def test_add():
    #Arrange
    expected = 3
    x = 1
    y = 2

    # Act
    actual = add(x,y)

    #Assert
    assert actual == expected

def test_compare_names__input_is_not_string():
    # Arrange
    expected = False
    test_input = 123

    # Act
    actual = compare_names(test_input,"olle")

    #Assert
    assert actual == expected

