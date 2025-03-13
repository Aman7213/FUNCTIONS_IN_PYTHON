# Custom/Advance qr code genrator in python

import qrcode

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("youtube.com")
qr.make(fit=True)

y=qr.make_image(fill_color="black", back_color="white")
y.save("Hi.png")