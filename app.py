from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import os
import io
import base64
from werkzeug.utils import secure_filename
from crypto_utils import encrypt_text, decrypt_text, encrypt_file, decrypt_file

app = Flask(__name__)
CORS(app)

# Configure upload settings
UPLOAD_FOLDER = 'uploads'
ENCRYPTED_FOLDER = 'encrypted'
DECRYPTED_FOLDER = 'decrypted'

# Create directories if they don't exist
for folder in [UPLOAD_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER]:
    if not os.path.exists(folder):
        os.makedirs(folder)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt-text', methods=['POST'])
def encrypt_text_route():
    try:
        data = request.get_json()
        plaintext = data.get('text', '')
        algorithm = data.get('algorithm', 'AES')
        
        if not plaintext:
            return jsonify({'error': 'No text provided'}), 400
        
        encrypted_text = encrypt_text(plaintext, algorithm)
        
        return jsonify({
            'success': True,
            'encrypted_text': encrypted_text,
            'algorithm': algorithm
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt-text', methods=['POST'])
def decrypt_text_route():
    try:
        data = request.get_json()
        ciphertext = data.get('text', '')
        algorithm = data.get('algorithm', 'AES')
        
        if not ciphertext:
            return jsonify({'error': 'No ciphertext provided'}), 400
        
        decrypted_text = decrypt_text(ciphertext, algorithm)
        
        return jsonify({
            'success': True,
            'decrypted_text': decrypted_text,
            'algorithm': algorithm
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/encrypt-file', methods=['POST'])
def encrypt_file_route():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        algorithm = request.form.get('algorithm', 'AES')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read file data
        file_data = file.read()
        original_filename = secure_filename(file.filename)
        
        # Encrypt file
        encrypted_data = encrypt_file(file_data, algorithm)
        
        # Save encrypted file
        encrypted_filename = f"encrypted_{original_filename}.enc"
        encrypted_path = os.path.join(ENCRYPTED_FOLDER, encrypted_filename)
        
        with open(encrypted_path, 'wb') as f:
            f.write(encrypted_data)
        
        return jsonify({
            'success': True,
            'encrypted_filename': encrypted_filename,
            'original_filename': original_filename,
            'algorithm': algorithm,
            'file_size': len(file_data)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt-file', methods=['POST'])
def decrypt_file_route():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        algorithm = request.form.get('algorithm', 'AES')
        original_filename = request.form.get('original_filename', 'decrypted_file')
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read encrypted file data
        encrypted_data = file.read()
        
        # Decrypt file
        decrypted_data = decrypt_file(encrypted_data, algorithm)
        
        # Save decrypted file
        decrypted_filename = f"decrypted_{original_filename}"
        decrypted_path = os.path.join(DECRYPTED_FOLDER, decrypted_filename)
        
        with open(decrypted_path, 'wb') as f:
            f.write(decrypted_data)
        
        return jsonify({
            'success': True,
            'decrypted_filename': decrypted_filename,
            'algorithm': algorithm,
            'file_size': len(decrypted_data)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    try:
        if folder not in ['encrypted', 'decrypted']:
            return jsonify({'error': 'Invalid folder'}), 400
        
        file_path = os.path.join(folder, filename)
        
        if not os.path.exists(file_path):
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(file_path, as_attachment=True, download_name=filename)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
