from PIL import Image

Image1 = Image.open('icon/test.png')

croppedIm = Image1.crop((130, 70, 300, 800))

croppedIm.show() 