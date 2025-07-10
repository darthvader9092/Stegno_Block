from steg_utils import decode_text_from_image

def view_hash(image_path, key):
    hidden_hash = decode_text_from_image(image_path, key)
    print(f"Hidden hash: {hidden_hash}")

if __name__ == "__main__":
    path = input("Enter image path (e.g., blocks/block_1.png): ")
    auth_key = input("Enter Auth Key: ")
    private_key = input("Enter Private Key: ")
    view_hash(path, auth_key + private_key)