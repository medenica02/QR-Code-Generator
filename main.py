import qrcode

url= input('Enter the URL: ').strip()
filename=input('Ebter the filename: ').strip()

qr=qrcode.QRCode(box_size=10,border=4)

qr.add_data(url)
image=qr.make_image(fill_color='black',back_color='white')
image.save(filename)
