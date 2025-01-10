# EXERCISE 4: Working with Functions

# Write a function that accepts a list of dictionaries with employee age (see example list from Exercise 3)
# and prints out the name and age of the youngest employee.

def name_and_age_of_youngest(employees):
    ages = []
    for person in employees:
        ages.append(person['age'])
    
    min_age = min(ages)
    index_of_youngest_person_in_list = ages.index(min_age)
    youngest_person = employees[index_of_youngest_person_in_list]
    print(f"Youngest person is { youngest_person['name']}, age: {youngest_person['age']}")
    
# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.

def calculate_uppercase_and_lowercase(str):
    uppercase_count = 0
    lowercase_count = 0

    for char in str:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    
    print(f"upper case count: { uppercase_count }")
    print(f"lower case count: { lowercase_count }")

# Write a function that prints the even numbers from a provided list.

def print_even_numbers(input_list):
    for element in input_list:
        element % 2 == 0 and print(element)

# For cleaner code, declare these functions in its own helper Module and use them in the main.py file