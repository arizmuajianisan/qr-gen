import qrcode
from PIL import Image

def generate_qr_code(data, file_name='qr_code.png'):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR Code
        border=4,  # Thickness of the border
    )

    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=False)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(file_name)

    print(f'QR code generated and saved as {file_name}')

# Example usage
if __name__ == "__main__":
    data = "AM1003-test"
    filename= f"{data}.png"
    generate_qr_code(data,filename)
