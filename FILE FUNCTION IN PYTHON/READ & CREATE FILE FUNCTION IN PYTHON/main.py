# Read the txt file and Create a txt file if txt file doesn't exist

def read_create():
    x = (input("Enter The Name Of File: ")).upper()
    try:
        with open (f"{x}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        with open(f"{x}.txt", "x") as file:
            file.write("THIS IS NEW FILE")
            print("This File Doesn't Exist...")
            print(f"{x}, File Is Created")