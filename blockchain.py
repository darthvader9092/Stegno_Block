import hashlib, os, shutil
from steg_utils import encode_text_into_image

def create_block(user_id, data):
    with open(f'users/{user_id}.txt', 'r') as f:
        auth_key, private_key, _ = f.read().splitlines()

    previous_hash = "0" if not os.listdir("blocks") else f"block_{len(os.listdir('blocks'))}.png"
    block_content = f"{data}|{previous_hash}|{auth_key}|{private_key}"
    block_hash = hashlib.sha256(block_content.encode()).hexdigest()

    block_number = len(os.listdir("blocks")) + 1
    block_filename = f"blocks/block_{block_number}.png"
    shutil.copy("template.png", block_filename)

    encode_text_into_image(block_filename, block_hash, auth_key + private_key)
    print(f"Block {block_number} created with hash: {block_hash}")
    
