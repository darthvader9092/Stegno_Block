# Stegno_Block

## Overview
Stegno_Block is a Python-based project that combines steganography with blockchain technology to securely store and manage data. It embeds data within PNG images using steganography and maintains data integrity through a simple blockchain structure. The project includes a Flask web application for user interaction, user registration, and hash verification functionalities.

## Features
- **Steganography**: Encodes and decodes data hidden in PNG images using the `steg_utils.py` module.
- **Blockchain**: Implements a basic blockchain to ensure data immutability, with block data stored in text files and images in the `blocks` directory.
- **Web Interface**: A Flask-based web app (`app.py`) provides a user interface via `templates/index.html`, enhanced with JavaScript (`static/script.js`).
- **User Management**: Handles user registration through `register_user.py`, storing user data in the `users` directory.
- **Hash Viewing**: The `view_hash.py` script allows users to verify block hashes.

## Project Structure
<pre>
  Stegno_Block/
├── app.py                  # Flask web application
├── blockchain.py           # Blockchain implementation
├── blocks/                 # Directory for block image files (e.g., block_1.png, block_2.png, ...)
├── blocks_data/            # Directory for block data text files (e.g., block1_data.txt, block2_data.txt, ...)
├── pycache/            # Python cache files
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
</pre>


## Prerequisites
- Python 3.10 or higher
- Flask (`pip install flask`)
- PIL (Pillow) for image processing (`pip install pillow`)
- Other dependencies listed in `requirements.txt` (if applicable)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/darthvader9092/Stegno_Block.git
   cd Stegno_Block

