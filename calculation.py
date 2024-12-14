
class Memory:

    memory_cash = []




def calculate(inp1, inp2, operation):
    if operation == '+':
        return calculate_addition(inp1, inp2)
    elif operation == '-':
        return calculate_subtraction(inp1, inp2)
    elif operation == '/':
        return calculate_division(inp1, inp2)
    elif operation == '*':
        return calculate_multiplication(inp1, inp2)
    else:
        return 0

def calculate_addition(inp1, inp2):
    return float(inp1) + float(inp2)

def calculate_subtraction(inp1, inp2):
    return float(inp1) - float(inp2)

def calculate_division(inp1, inp2):
    return float(inp1) / float(inp2)

def calculate_multiplication(inp1, inp2):
    return float(inp1) * float(inp2)