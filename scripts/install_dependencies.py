#!/usr/bin/env python3
"""
Installation script for the Cryptographic System dependencies
"""

import subprocess
import sys

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False
    return True

def main():
    """Install all required packages"""
    packages = [
        "Flask==2.3.3",
        "Flask-CORS==4.0.0",
        "pycryptodome==3.19.0",
        "Werkzeug==2.3.7"
    ]
    
    print("🔧 Installing Cryptographic System dependencies...")
    print("=" * 50)
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print("=" * 50)
    print(f"✅ Installation complete! {success_count}/{len(packages)} packages installed successfully.")
    
    if success_count == len(packages):
        print("\n🚀 You can now run the application with: python app.py")
    else:
        print("\n⚠️  Some packages failed to install. Please check the errors above.")

if __name__ == "__main__":
    main()
