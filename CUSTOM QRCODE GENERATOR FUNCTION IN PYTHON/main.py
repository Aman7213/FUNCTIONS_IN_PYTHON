# Custom/Advance qr code genrator in python

import qrcode # pip install qrcode

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("youtube.com") # Data from user in the form of url
qr.make(fit=True)

y=qr.make_image(fill_color="black", back_color="white") # Giving different colour to the qr code
y.save("Hi.png") # The name of the saved file