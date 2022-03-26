def list_sum(array):
    prev_number = 0
    result = """0"""
    for number in array:
        new_number = prev_number + number
        result += f"\n{prev_number} + {number} = {new_number}"
        prev_number = new_number
    return result

my_array = [1, 3, 5, 7, 8, 9, 11, 3, 4, 6, 7]

print(list_sum(my_array))