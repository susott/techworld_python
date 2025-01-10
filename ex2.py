# EXERCISE 2: Working with Dictionaries

# Using the following dictionary:

employee = {
    "name": "Tim",
    "age": 30,
    "birthday": "1990-03-10",
    "job": "DevOps Engineer"
}

# Write a Python Script that:

# Updates the job to Software Engineer
employee["job"] = "Software Engineer"

# Removes the age key from the dictionary
del employee["age"]

# Loops through the dictionary and prints the key:value pairs one by one
for key, val in employee.items():
    print(f"{key}: {val}")

# Using the following 2 dictionaries:

dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

# Write a Python Script that:

# Merges these two Python dictionaries into 1 new dictionary.
dict_combined = dict_one | dict_two

# Sums up all the values in the new dictionary and prints it out
print(sum(dict_combined.values()))

# Prints the max and minimum values of the dictionary
print(max(dict_combined.values()))
print(min(dict_combined.values()))
