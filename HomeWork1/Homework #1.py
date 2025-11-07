def my_function():
    # Define function without predefined arguments
    print("Enter the first number")
    num1 = float(input())  # Read first number and convert to float

    print("Enter the second number")
    num2 = int(input())  # Read second number and convert to integer

    # Perform basic math operations
    add = num1 + num2
    mult = num1 * num2

    # Check division by zero
    if num2 == 0:
        div = None
    else:
        div = num1 / num2

    # Return results as tuple
    return add, mult, div


# Call function and unpack results
sum_result, mult_result, div_result = my_function()

# Output results
print(f"Result of addition: {sum_result}")  # Print sum
print(f"Result of multiplication: {mult_result}")  # Print multiplication

# Handle division output separately if divisor was zero
if div_result is None:
    print("Result of division: Division by zero is not allowed!")
else:
    print(f"Result of division: {div_result:.3f}")  # Round division result to 3 decimals
