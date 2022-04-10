# Write a program to accept two numbers from the user and calculate multiplication

def take_and_multiply():
    a = int(input("Please provide first number: "))
    b = int(input("Please provide second number: "))
    return a * b


print(take_and_multiply())


# Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

print('Name', 'Is', 'James', sep="**")


# Display float number with 2 decimal places using print()

number = 89738.7823

print("%.2f" % number)

# Convert Decimal number to octal using print() output formatting

number2 = 9

print("%o" % number2)

# Accept a list of 5 float numbers as an input from the user

def list_of_floats():
    the_list = []
    for i in range(5):
        num = float(input(f"Please provide 5 float numbers ({i+1}/5): "))
        the_list.append(num)
    return the_list

print(list_of_floats())

# Accept any three string from one input() call

def three_names():
    names = input("Please write three names separated with whitespace: ")
    names_split = names.split()
    return f"""
    First name: {names_split[0]}
    Second name: {names_split[1]}
    Third name: {names_split[2]}
    """


print(three_names())