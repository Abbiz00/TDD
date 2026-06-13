def add(x,y):
    """" lägger ihop två tal och returnerar resultatet """
    return x + y

def compare_names(user_input, name):
    if not isinstance(user_input, str):
        return False
    return user_input in name

# TODO: test med små och stora bokstäver