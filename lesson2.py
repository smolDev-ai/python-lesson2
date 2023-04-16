my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for value in my_list:
    print(value)

# List Comprehension - General
new_list = [num * 2 for num in my_list]
# multiply every number by 2
# print(new_list)

# List Comprehension - Conditional
second_list = [num for num in my_list if num % 2 == 0]

# only even
# print(second_list)

# List Comprehension - Conditionals Else
third_list = [num * 2 if num % 2 == 0 else num/2 for num in my_list]

# print(third_list)

# Slicing
# print(my_list[0:2])
# Gets last item in a list
# print(my_list[-1:])

# everything except for the last item
# print(my_list[:-1])

# get only the even numbers -- only works because the list is sorted in order.
# print(my_list[1::2])

# get only the odd numbers
# print(my_list[::2])

# Grab the third index up until the 4th index
# print(my_list[3:4])

# Reminder: Lists can be accessed at indices
print(my_list[3])

new_dict = {
    "name": "Owen",
    "age": 26,
    "hobbies": ["Game", "Read", "Hike"]
}

for value in new_dict.values():
    print(value)

for key in new_dict.keys():
    print(key)

for key, value in new_dict.items():
    print(f"{key} has value: {value}")


# Dictionary Comprehensions:
# Create dictionary from numbers in my_list
new_dict2 = {num: num * 2 for num in my_list}

# print(new_dict2)

# Create a dictionary from two strings
letter_string = "ABCDEF"
number_string = "123456"


new_dict3 = {letter_string[i]: number_string[i] for i in range(len(letter_string))}

# print(new_dict3)

new_dict4 = {num: 'even' if num % 2 == 0 else 'odd' for num in my_list}

print(new_dict4)


print(new_dict4.get(4))

another_dict = dict.fromkeys(my_list)

# print(another_dict)