
Stegno_Block
Overview
Stegno_Block is a Python-based project that integrates steganography with blockchain technology to securely store and manage data. It uses image files to hide data (steganography) and a simple blockchain structure to ensure data integrity and immutability. The project includes a Flask web application for user interaction, user registration, and hash viewing functionalities.
Features

Steganography: Embeds and extracts hidden data within PNG images using the steg_utils.py module.
Blockchain: Implements a basic blockchain to store data securely, with block data saved in text files and corresponding images in the blocks directory.
Web Interface: A Flask-based web application (app.py) provides a user interface for interacting with the system, served through templates/index.html and enhanced with JavaScript (static/script.js).
User Management: User registration is handled via register_user.py, with user data stored in the users directory.
Hash Viewing: The view_hash.py script allows users to view the hash of blocks for verification.

Project Structure
Stegno_Block/
├── app.py                  # Flask web application
├── blockchain.py           # Blockchain implementation
├── blocks/                 # Directory for block image files (e.g., block_1.png, block_2.png, ...)
├── blocks_data/            # Directory for block data text files (e.g., block1_data.txt, block2_data.txt, ...)
├── __pycache__/            # Python cache files
├── README.md               # Project documentation
├── register_user.py        # Script for user registration
├── static/                 # Static files for the web interface
│   └── script.js           # JavaScript for frontend functionality
├── steg_utils.py           # Steganography utilities for encoding/decoding data in images
├── template.png            # Template image for steganography
├── templates/              # HTML templates for the Flask app
│   └── index.html          # Main web interface
├── users/                  # Directory for user data files (e.g., 001.txt, 002.txt, ...)
└── view_hash.py            # Script to view block hashes

Prerequisites

Python 3.10 or higher
Flask (pip install flask)
PIL (Pillow) for image processing (pip install pillow)
Other dependencies listed in requirements.txt (if applicable)

Installation

Clone the repository:git clone https://github.com/darthvader9092/Stegno_Block.git
cd Stegno_Block


Install dependencies:pip install -r requirements.txt


Run the Flask application:python app.py


Access the web interface at http://localhost:5000.

Usage

Register Users: Run register_user.py to add new users, whose data will be stored in the users directory.
Store Data: Use the web interface (index.html) to input data, which will be encoded into images using steganography and added to the blockchain.
View Hashes: Run view_hash.py to verify block hashes and ensure data integrity.
Blockchain Data: Block data is stored in blocks_data/*.txt, and corresponding images are saved in blocks/*.png.

Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Create a pull request.

License
This project is licensed under the MIT License.
