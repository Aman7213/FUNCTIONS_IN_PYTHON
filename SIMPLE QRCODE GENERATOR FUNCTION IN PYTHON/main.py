import qrcode

def qr_maker():  # QR is a variable to take input from user(i.e. URL).
    QR=qrcode.make("{i}")  # Here {i} is the input url from user.
    QR.save("{qr_name}.png")  # Here {qr_name} is the file name for qr png.

# Example
# Run this command

# i=input("Enter URL: ")
# qr_name=input("Enter the name of QRCode: ")