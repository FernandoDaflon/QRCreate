import qrcode

# qr = qrcode.make('Hello World')
# qr.save('myQR.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=9
)

data = 'Cruzeiro ou Ceara?'

# data = 'client: OOGTK-LIBRA' \
#        'Job: 35469 564864 123 2020' \
#        'hub: world cargo logistics'

# data = 'T-Bromstadvegen59Trondheim7047-Tvetenveien32Oslo0666 '

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
# img.save('35469 564864 123 2020.png')
img.save('QRcode.png')