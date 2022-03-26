def odd_and_even(array_1, array_2):
    """Function takes every odd element from the first array and every even element from the second array to put them into the new list"""
    odds = [x for x in array_1 if x % 2 == 1]
    even = [x for x in array_2 if x % 2 == 0]
    new_list = odds + even
    return new_list


array_1 = [1, 2, 3, 4, 5, 6, 7, 8]
array_2 = [9, 10, 11, 12, 13, 14, 15, 16]

print(odd_and_even(array_1, array_2))



def list_slicer(array_3):
    """Function checks if its possible to slice the list into parts with exact provided number of elements and so, it does the work"""
    number = int(input("Please provide the number of elements you want into each slice: "))
    if len(array_3) % number == 0:
        new_list = []
        for i in range(1, (len(array_3) // number) + 1):
            new_list.append(array_3[number * (i-1):number * i])
        return new_list
    else:
        return "You cannot slice it in equal parts"


array_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_4 = [x for x in range(12)]
print(list_slicer(array_3))
print(list_slicer(array_4))



def count_the_list(array_to_count):
    """Function that counts the occurances of the elements in the list and saves them to the dictionary"""
    dict = {}
    for element in array_to_count:
        if element not in dict:
            dict[element] = array_to_count.count(element)
    return dict


array_5 = [1, 2, 3, 4, 5, 3, 4, 5, 5]
print(count_the_list(array_5))


def lists_to_set(array_1, array_2):
    """Function takes two lists of the same length and makes a set with i elements in pairs"""
    new_set = set()
    for i in range(len(array_1)):
        new_set.add((array_1[i], array_2[i]))
    return new_set


print(lists_to_set(array_1, array_2))
