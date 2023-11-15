import qrcode
import image
import PIL

class GenerateQrCode():
    def __init__(self) -> None:
        self.qr=qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2)

    def generateQrFromUrl(self,url):
        self.qr.add_data(url)
        self.qr.make(fit=True)
        img=self.qr.make_image(fill = 'Black',back_color = 'White')
        return img
    
    

    