import qrcode
import image

qr = qrcode.QRCode(version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=2)

data = "https://www.linkedin.com/in/avirup171/"

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill = 'Black',back_color = 'White')

img.save("Image.png")
