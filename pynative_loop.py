# Print First 10 natural numbers using while loop

def loop_till_10():
    result = ""
    for i in range(1, 11):
        result += f"{i}\n"
    return result


print(loop_till_10())

# Calculate the sum of all numbers from 1 to a given number

def hot_summer():
    num = int(input("Please provide a number: "))
    result = 0
    for i in range (1, num + 1):
        result += i
    return result


print(hot_summer())

# Write a program to print multiplication table of a given number

def multi_table():
    num = int(input("Please provide a number: "))
    multi_table = [x * num for x in range(1, 11)]
    result = ""
    for ele in multi_table:
        result += f"{ele}\n"
    return result

print(multi_table())

# Write a program to display only those numbers from a list that satisfy the following conditions:
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

another_list = [120, 77, 15, 160, 80, 501, 20]

def strange_list_shower(the_list):
    result = ""
    for ele in the_list:
        if ele > 500:
            break
        else:
            if ele > 150:
                continue
            if ele % 5 == 0:
                result += f"{str(ele)}\n"
    return(result)

print(strange_list_shower(another_list))
