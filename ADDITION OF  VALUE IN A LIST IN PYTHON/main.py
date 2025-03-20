def addition():
    num =list(map(int, input("Enter the numbers seprated by space: ").split())) 
    return sum(num)

 # Here "int" can be replaced by "float" for taking decimal values.

# Run the command given below.
print(addition())