
def find_second_max(numbers):
    if len(numbers) < 2:
        return None
    sorted_desc = sorted(numbers, reverse=True)
    return sorted_desc[1]