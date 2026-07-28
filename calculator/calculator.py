from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
    
def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Get a valid number
def get_a_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number.")

# Get a valid operation
def get_an_operation():
    print('Select one of the operations')
    for symbol in operations:
        print(symbol)
    
    while True:
        # .strip() removes extra spaces
        operation_symbol = input("Pick an operation: ").strip()
        if operation_symbol in operations:
            return operation_symbol
        print('Error: Please select one of the allowed operations.')

# Main program execution
n1 = get_a_number('Enter the first number: ')
operation_symbol = get_an_operation()

# Keep asking for n2 until its not zero in case the user chose is division
while True:
    n2 = get_a_number('Enter the second number: ')
    if operation_symbol == '/' and n2 == 0:
        print("Error: You cannot divide by zero. Please enter a non-zero number.")
    else:
        break

# Perform calculation
calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)

# Show answer rounded to 1 decimal place
print(f"{n1} {operation_symbol} {n2} = {answer:.1f}")
