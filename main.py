import pyqrcode
import os, shutil

title = input("Give a title to your QR code!!")
text = input("What would you like QR code to say !")
# Create qrcode object with data and error correction level.

file_name_svg = title + '.svg'
file_name_png = title + '.png'

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=10)

url.png(file_name_png, scale=8)

os.mkdir(fr"C:\Users\Public\Downloads\{title}")

shutil.move(f"{file_name_png}", fr"C:\Users\Public\Downloads\{title}")
shutil.move(f"{file_name_svg}", fr"C:\Users\Public\Downloads\{title}")

