#!/usr/bin/env python3
"""
Setup script for the Cryptographic System
Pure HTML, CSS, JavaScript Frontend with Flask Backend
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    directories = ['uploads', 'encrypted', 'decrypted', 'templates', 'static']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")
        else:
            print(f"📁 Directory already exists: {directory}")

def main():
    """Setup the cryptographic system"""
    print("🔧 Setting up Cryptographic System...")
    print("📋 Technology Stack: HTML, CSS, JavaScript + Flask")
    print("=" * 60)
    
    # Create directories
    print("\n📁 Creating directories...")
    create_directories()
    
    # Install packages
    print("\n📦 Installing Python packages...")
    packages = [
        "Flask==2.3.3",
        "Flask-CORS==4.0.0", 
        "pycryptodome==3.19.0",
        "Werkzeug==2.3.7"
    ]
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("=" * 60)
    print(f"✅ Setup complete! {success_count}/{len(packages)} packages installed successfully.")
    
    if success_count == len(packages):
        print("\n🚀 You can now run the application with:")
        print("   python app.py")
        print("\n🌐 Then open your browser and go to:")
        print("   http://localhost:5000")
        print("\n💡 Features:")
        print("   • Pure HTML, CSS, JavaScript frontend")
        print("   • Flask backend with cryptographic operations")
        print("   • RSA, AES, DES encryption/decryption")
        print("   • Text and file encryption support")
        print("   • Drag & drop file upload")
        print("   • Responsive design")
    else:
        print("\n⚠️  Some packages failed to install. Please check the errors above.")

if __name__ == "__main__":
    main()
