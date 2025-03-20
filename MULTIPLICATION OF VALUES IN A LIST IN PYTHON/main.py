def multiplication():
    value = list(map(float, input("Enter the numbers seprated by space: ").split()))
    Result= 1 # Initialize the Result to 1
    for num in value:
        Result *= num # Multiply Result by each num from the list(value)
    return Result

# Can also be "Result = Result*num".
# Run the command as example
# print(multiplication())