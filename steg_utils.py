import base64
from stegano import lsb

HEADER = "BLOCKHASH::"

def xor_encrypt_decrypt(text, key):
    # XOR each character with the key (looped if shorter)
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def encode_text_into_image(image_path, text, key):
    # Encrypt the data
    encrypted_text = xor_encrypt_decrypt(text, key)
    # Base64 encode for hiding in image
    encoded = base64.b64encode((HEADER + encrypted_text).encode()).decode()
    # Hide the result in the image
    secret = lsb.hide(image_path, encoded)
    secret.save(image_path)

def decode_text_from_image(image_path, key):
    try:
        # Reveal and decode
        raw_data = lsb.reveal(image_path)
        if not raw_data:
            return "No hidden data."

        decoded = base64.b64decode(raw_data).decode()

        # Check header integrity
        if not decoded.startswith(HEADER):
            return "Invalid format or tampered image."

        # Remove header and decrypt
        encrypted_part = decoded[len(HEADER):]
        original_text = xor_encrypt_decrypt(encrypted_part, key)
        return original_text
    except Exception as e:
        return f"Decoding failed: {str(e)}"

