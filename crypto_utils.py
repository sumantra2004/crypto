from Crypto.Cipher import AES, DES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os

# Hardcoded keys as specified
AES_KEY = b'ranjeetranjeet12'  # 16-byte key for AES
DES_KEY = b'ranjeet!'          # 8-byte key for DES

# Generate RSA key pair (for demonstration)
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

# Store RSA keys globally for this session
RSA_PRIVATE_KEY, RSA_PUBLIC_KEY = generate_rsa_keys()

def encrypt_text(plaintext, algorithm):
    """Encrypt text using the specified algorithm"""
    try:
        if algorithm == 'AES':
            return encrypt_aes_text(plaintext)
        elif algorithm == 'DES':
            return encrypt_des_text(plaintext)
        elif algorithm == 'RSA':
            return encrypt_rsa_text(plaintext)
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    except Exception as e:
        raise Exception(f"Encryption failed: {str(e)}")

def decrypt_text(ciphertext, algorithm):
    """Decrypt text using the specified algorithm"""
    try:
        if algorithm == 'AES':
            return decrypt_aes_text(ciphertext)
        elif algorithm == 'DES':
            return decrypt_des_text(ciphertext)
        elif algorithm == 'RSA':
            return decrypt_rsa_text(ciphertext)
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")

def encrypt_file(file_data, algorithm):
    """Encrypt file data using the specified algorithm"""
    try:
        if algorithm == 'AES':
            return encrypt_aes_file(file_data)
        elif algorithm == 'DES':
            return encrypt_des_file(file_data)
        else:
            raise ValueError(f"File encryption not supported for {algorithm}")
    except Exception as e:
        raise Exception(f"File encryption failed: {str(e)}")

def decrypt_file(encrypted_data, algorithm):
    """Decrypt file data using the specified algorithm"""
    try:
        if algorithm == 'AES':
            return decrypt_aes_file(encrypted_data)
        elif algorithm == 'DES':
            return decrypt_des_file(encrypted_data)
        else:
            raise ValueError(f"File decryption not supported for {algorithm}")
    except Exception as e:
        raise Exception(f"File decryption failed: {str(e)}")

# AES Implementation
def encrypt_aes_text(plaintext):
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    padded_text = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    
    # Combine IV and ciphertext, then encode to base64
    encrypted_data = cipher.iv + ciphertext
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_aes_text(ciphertext):
    encrypted_data = base64.b64decode(ciphertext.encode('utf-8'))
    iv = encrypted_data[:16]  # AES block size is 16 bytes
    ciphertext_bytes = encrypted_data[16:]
    
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext_bytes)
    plaintext = unpad(padded_plaintext, AES.block_size)
    
    return plaintext.decode('utf-8')

def encrypt_aes_file(file_data):
    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    padded_data = pad(file_data, AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    
    # Combine IV and ciphertext
    return cipher.iv + ciphertext

def decrypt_aes_file(encrypted_data):
    iv = encrypted_data[:16]  # AES block size is 16 bytes
    ciphertext = encrypted_data[16:]
    
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    
    return unpad(padded_data, AES.block_size)

# DES Implementation
def encrypt_des_text(plaintext):
    cipher = DES.new(DES_KEY, DES.MODE_CBC)
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    
    # Combine IV and ciphertext, then encode to base64
    encrypted_data = cipher.iv + ciphertext
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_des_text(ciphertext):
    encrypted_data = base64.b64decode(ciphertext.encode('utf-8'))
    iv = encrypted_data[:8]  # DES block size is 8 bytes
    ciphertext_bytes = encrypted_data[8:]
    
    cipher = DES.new(DES_KEY, DES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext_bytes)
    plaintext = unpad(padded_plaintext, DES.block_size)
    
    return plaintext.decode('utf-8')

def encrypt_des_file(file_data):
    cipher = DES.new(DES_KEY, DES.MODE_CBC)
    padded_data = pad(file_data, DES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    
    # Combine IV and ciphertext
    return cipher.iv + ciphertext

def decrypt_des_file(encrypted_data):
    iv = encrypted_data[:8]  # DES block size is 8 bytes
    ciphertext = encrypted_data[8:]
    
    cipher = DES.new(DES_KEY, DES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    
    return unpad(padded_data, DES.block_size)

# RSA Implementation (for text only)
def encrypt_rsa_text(plaintext):
    cipher = PKCS1_OAEP.new(RSA_PUBLIC_KEY)
    
    # RSA can only encrypt small amounts of data
    max_length = RSA_PUBLIC_KEY.size_in_bytes() - 42  # OAEP padding overhead
    
    if len(plaintext.encode('utf-8')) > max_length:
        raise ValueError(f"Text too long for RSA encryption. Maximum length: {max_length} bytes")
    
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_rsa_text(ciphertext):
    cipher = PKCS1_OAEP.new(RSA_PRIVATE_KEY)
    ciphertext_bytes = base64.b64decode(ciphertext.encode('utf-8'))
    plaintext = cipher.decrypt(ciphertext_bytes)
    
    return plaintext.decode('utf-8')
