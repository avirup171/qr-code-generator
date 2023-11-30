import qrcode
import image
from PIL import Image, ImageDraw

from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask

class GenerateQrCode():
    def __init__(self) -> None:
        self.qr=qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=2)

    def generateQrFromUrl(self,url,isRounded):
        self.qr.add_data(url)
        self.qr.make(fit=True)
        img=self.qr.make_image(fill = 'Black',back_color = 'White')
        if(not isRounded):
            return img
        # else:
        #     # Make the edges rounded
        #     width, height = img.size
        #     mask = Image.new("L", (width, height), 0)
        #     draw = ImageDraw.Draw(mask)
            
        #     img = Image.composite(img, Image.new("RGB", img.size, "white"), mask)
        #     return img  


def main():
    url='https://www.linkedin.com/in/avirup171/'
    gqr=GenerateQrCode()
    img=gqr.generateQrFromUrl(url,False)
    img.save("img.png")

if __name__=='__main__':
    main()

    