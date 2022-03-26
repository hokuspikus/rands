def palindrome_checker(strng):
        return str(strng) == str(strng)[::-1]


def palindrome_checker_v2(strng):
        return str(strng).lower() == str(strng).lower()[::-1]

example_1 = "kayak"
example_2 = "Kayak"
example_3 = 9875789
example_4 = {"example": 17}

print(palindrome_checker(example_1))
print(palindrome_checker(example_2))
print(palindrome_checker(example_3))
print(palindrome_checker(example_4))
print(palindrome_checker_v2(example_4))
print(palindrome_checker_v2(example_3))
print(palindrome_checker_v2(example_2))
print(palindrome_checker_v2(example_1))
