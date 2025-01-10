
# EXERCISE 5: Python Program 'Calculator'

# Write a simple calculator program that:

#     takes user input of 2 numbers and operation to execute
#     handles the following operations: plus, minus, multiply, divide
#     does proper user validation and give feedback: only numbers allowed
#     Keeps the Calculator program running until the user types “exit”
#     Keeps track of how many calculations the user has taken, and when the user
#     exits the calculator program, prints out the number of calculations the user did

# Concepts covered: working with different data types, conditionals, type conversion, user input, user input validation

# notes: tests are missing

def perform_operation(num1, num2, operator):
    match operator:
        case 'plus':
            return num1 + num2
        case 'minus':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            return num1 / num2


def process(user_input):
    str_num1, str_num2, op = user_input.split(',')

    num1 = int(str_num1.strip())
    num2 = int(str_num2.strip())
    operation = op.strip()
    return num1, num2, operation


calculation_counter = 0

while True:
    user_input = input("Enter two numbers and an operation to perform, separated by comma\n")
    allowed_operations = {'plus', 'minus', 'multiply', 'divide'}

    if user_input == 'exit':
        print('Programm is shutting down')
        print(f"You did {calculation_counter} calculations this time.")
        break

    try:
        num1, num2, operation = process(user_input)
    except ValueError:
        print('Please check your input values')
        continue

    if operation not in allowed_operations:
        print(f"operation {operation} not allowed. Use one of the following: {', '.join(allowed_operations)}")
        continue
    elif operation == 'divide' and num2 == 0:
        print('Division by zero is not allowed')
        continue

    result = perform_operation(num1, num2, operation)
    print(f"{num1} {operation} {num2} is {result}")
    calculation_counter += 1
