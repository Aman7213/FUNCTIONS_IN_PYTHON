# This Function Will Write/Overwrite Data In The Txt file.
# IF File Doesn't Exist It Will Create and Write/Overwrite Data.

def write_data():
    x = (input("Enter The Name Of File: ")).upper()
    y = input("Enter Data To Be Written: ")
    with open(f"{x}.txt", "w") as file:
        file.write(f"{y}")
        print("Data Is Written")