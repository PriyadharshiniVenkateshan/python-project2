import qrcode
import matplotlib.pyplot as plt
#from PIL import image

data = "https://youtu.be/OP5v48Wz7u8"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="lightgreen")
img.save("AreaBaana.png")
fig, ax = plt.subplots()
ax.imshow(img)
ax.axis("off")

plt.show()
