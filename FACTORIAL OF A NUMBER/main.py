def factorial():
    num = int(input("Enter the number: "))
    fact = 1 # Initialize the factorial result to 1
    for i in range(1, num+1):
        fact *= i # Multiply fact by each number from 1 to num
    return fact

# Can also be "fact = fact*num".
# Use this for example
# print(factorial())