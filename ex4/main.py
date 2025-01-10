# import calculate_uppercase_and_lowercase, name_and_age_of_youngest, print_even_numbers from helper

import helper

# EXERCISE 4: Working with Functions

# Write a function that accepts a list of dictionaries with employee age (see example list from Exercise 3)
# and prints out the name and age of the youngest employee.

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

helper.name_and_age_of_youngest(employees)

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
helper.calculate_uppercase_and_lowercase("FOee")

# Write a function that prints the even numbers from a provided list.
helper.print_even_numbers([2,3,4])

# For cleaner code, declare these functions in its own helper Module and use them in the main.py file
