# Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

def sum_or_product():
    num_a = int(input("Please provide first number: "))
    num_b = int(input("Please provide second number: "))
    return num_a * num_b if num_a * num_b > 1000 else num_a + num_b

print(sum_or_product())

# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

def iterate_over_10():
    result = """0"""
    previous_number = 0
    for i in range (1, 10):
        result += f'\n{previous_number} + {i} = {previous_number + i}'
        previous_number = previous_number + i
    return result

print(iterate_over_10())

# Write a program to accept a string from the user and display characters that are present at an even index number.

def even_steven():
    strng = input("Please provide your string: ")
    result = ''
    for i in range(len(strng)):
        if i % 2 == 1:
            result += strng[i] + ' '
    return result

print(even_steven())

# Write a program to remove characters from a string starting from zero up to n and return a new string.

def characters_remover():
    strng = input("Please provide your string: ")
    number_of_chars = int(input("Please provide number of characters to be deleted from the beginning of the string: "))
    if number_of_chars >= len(strng):
        return "Number of characters is greater on equal to string length"
    else:
        new_string = strng[number_of_chars:]
        return new_string

print(characters_remover())

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def first_and_last(arr):
    if not arr:
        return "Array is empty"
    return arr[0] == arr[-1]

array1 = [10, 20, 40, 30, 10]
array2 = [10, 20, 40, 30, 30]

print(first_and_last(array1))
print(first_and_last(array2))

# Iterate the given list of numbers and print only those numbers which are divisible by 5

def divisable_by_5(arr):
    return f'Divisable by 5 are: {[x for x in arr if x % 5 == 0]}'

array3 = [5, 6, 7, 8, 10, 12, 15]

print(divisable_by_5(array3))

# Write a program to find how many times substring “Emma” appears in the given string.

def search_for_emma(strng):
    return f'Emma appeared {strng.count("Emma")} times'

string_with_emmas = "Emma this, Emma that, there should be Emma thrice"

print(search_for_emma(string_with_emmas))

# Print the following pattern (half-pyramid)

def half_pyramid(num):
    for i in range(1, num + 1):
        print(f'{i} ' * i)

half_pyramid(5)

# Write a program to check if the given number is a palindrome number.

def palindrome_number(num):
    return str(num) == str(num)[::-1]

print(palindrome_number(123454321))
print(palindrome_number(123454))

# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def lists_together(arr1, arr2):
    new_list = []
    for i in range(len(arr1)):
        if i % 2 == 0:
            new_list.append(arr1[i])
    for i in range(len(arr2)):
        if i % 2 == 1:
            new_list.append(arr2[i])
    return sorted(new_list)

array4 = [1, 3, 5, 7, 9, 11]        
array5 = [2, 4, 6, 8, 10, 12]

print(lists_together(array4, array5))

