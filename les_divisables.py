from gettext import find


def find_divisables():
    print("""This function will list you all the divisable numbers in range of your choice, by the divisor of your choice.
    Please enjoy.""")
    to_range = int(input("Please provide range of search: "))
    divisor = int(input("Please provide the divisor: "))
    return [x for x in range(1, to_range) if x % divisor == 0]


print(find_divisables())