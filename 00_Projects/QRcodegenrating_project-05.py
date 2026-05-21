import qrcode

# Data to be stored in QR code
data = input("Enter text or URL: ")

# Create QR code object
qr = qrcode.make(data)

# Save the QR code as image
qr.save("qrcode.png")

print("QR code generated successfully")
