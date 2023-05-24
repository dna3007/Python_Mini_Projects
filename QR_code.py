import qrcode as qr

image = qr.make("https://www.linkedin.com/in/dipen3007")
image.save("linkedin_qr.png")