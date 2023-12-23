from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64
import qrcode

def encrypt_text(text, key, iv):
    # Pad the input text using PKCS7
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    # Create an AES CBC cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Encode the ciphertext in Base64
    encrypted_text = base64.b64encode(ciphertext).decode()
    return encrypted_text

def generate_qr_code(data, filename='qrcodeV2.png'):
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    # Set your parameters
    secret_key = b'VISION4000007015'  # 128-bit key
    iv = bytes([0] * 16)  # 16 bytes IV

    # Get user input
    input_text = input("Enter the text to encrypt: ")

    # Encrypt the text
    encrypted_text = encrypt_text(input_text, secret_key, iv)
    print(f"Encrypted Text: {encrypted_text}")

    # Generate and display the QR code
    generate_qr_code(encrypted_text)
    print("QR code generated and saved as 'qrcode V2.png'")
