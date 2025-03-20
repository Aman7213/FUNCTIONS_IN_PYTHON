# Add data to the txt file without overwritting the existing data.
# IF File Doesn't Exist It Will Create and Append Data.

def add_data():
    x = (input("Enter The Name Of File: ")).upper()
    y = input("Enter Data To Be added: ")
    with open(f"{x}.txt", "a") as file:
        file.write(f"\n{y}")
        print("Data Is Added")