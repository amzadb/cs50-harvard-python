# Read an arithmetic expression and calculate the result using the eval() function
input_expr = input("Enter an arithmetic expression: ")
result = eval(input_expr)

# Convert the result to a float
result = float(result)

print(result)