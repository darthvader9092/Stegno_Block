from flask import Flask, render_template, request, redirect, send_from_directory
import os
from blockchain import create_block
from steg_utils import decode_text_from_image

app = Flask(__name__)

@app.route('/')
def index():
    block_images = sorted(os.listdir('blocks'))
    return render_template('index.html', blocks=block_images)

@app.route('/add_block', methods=['POST'])
def add_block():
    user_id = request.form['user_id']
    data = request.form['data']
    
    # Create a new block
    create_block(user_id, data)
    
    # Get the block number
    block_number = len(os.listdir('blocks'))  # Assuming blocks are saved in the 'blocks' folder
    
    # Save the block data in a text file in blocks_data/
    os.makedirs('blocks_data', exist_ok=True)
    block_data_filename = f"block{block_number}_data.txt"
    
    with open(f"blocks_data/{block_data_filename}", 'w') as f:
        f.write(f"User ID: {user_id}\nData: {data}\n")
    
    return redirect('/')

@app.route('/blocks/<filename>')
def get_block_image(filename):
    return send_from_directory('blocks', filename)

@app.route('/view_hash', methods=['POST'])
def view_hash():
    block = request.form['block']
    auth_key = request.form['auth_key']
    private_key = request.form['private_key']
    full_key = auth_key + private_key
    hash_value = decode_text_from_image(f"blocks/{block}", full_key)
    return {'hash': hash_value}



@app.route('/register_user', methods=['POST'])
def register_user():
    user_id = request.form['user_id']
    auth_key = request.form['auth_key']
    private_key = request.form['private_key']

    # Ensure users/ directory exists
    os.makedirs('users', exist_ok=True)

    # Write to a dedicated user file like `users/003.txt`
    with open(f'users/{user_id}.txt', 'w') as f:
        f.write(f"{auth_key}\n{private_key}\n{user_id}")
    
    print(f"User {user_id} registered.")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
