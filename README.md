# Cryptographic System - Pure HTML/CSS/JS + Flask

A comprehensive web-based encryption and decryption system using **pure HTML, CSS, JavaScript** frontend with **Flask** backend. No frameworks or libraries on the frontend!

## 🛠️ Technology Stack

### Frontend (Pure Web Technologies)
- **HTML5**: Semantic markup and structure
- **CSS3**: Custom styling with gradients and animations
- **Vanilla JavaScript**: DOM manipulation and Fetch API
- **No frameworks**: No React, Vue, Angular, or jQuery

### Backend (Python)
- **Flask**: Lightweight web framework
- **PyCryptodome**: Cryptographic operations
- **Werkzeug**: File handling utilities

## 🔐 Supported Algorithms

### RSA (Rivest-Shamir-Adleman)
- **Type**: Asymmetric encryption
- **Key Size**: 2048 bits
- **Use Case**: Small text encryption (~200 chars max)
- **Security**: High for key exchange

### AES (Advanced Encryption Standard)
- **Type**: Symmetric encryption
- **Key Size**: 128 bits
- **Key**: `ranjeetranjeet12` (hardcoded)
- **Use Case**: Text and file encryption
- **Security**: Very high, industry standard

### DES (Data Encryption Standard)
- **Type**: Symmetric encryption
- **Key Size**: 64 bits
- **Key**: `ranjeet!` (hardcoded)
- **Use Case**: Educational purposes
- **Security**: Low, deprecated

## 🚀 Features

### Text Encryption & Decryption
- ✅ Support for RSA, AES, DES algorithms
- ✅ Real-time encryption/decryption
- ✅ Base64 encoded output
- ✅ Algorithm-specific limitations
- ✅ Clear button functionality

### File Encryption & Decryption
- ✅ Drag & drop file upload
- ✅ Support for any file type (images, documents, audio, video, PDFs)
- ✅ AES and DES for files (RSA for small text only)
- ✅ Progress indicators
- ✅ File download functionality
- ✅ File size validation (50MB limit)

### User Interface
- ✅ Responsive design (mobile-friendly)
- ✅ Color-coded algorithm sections
- ✅ Real-time status notifications
- ✅ File information display
- ✅ Clean, modern design
- ✅ Pure CSS animations and transitions

## 📁 Project Structure

\`\`\`
cryptographic-system/
├── app.py                    # Main Flask application
├── crypto_utils.py           # Cryptographic operations
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html           # Main HTML template (pure HTML)
├── static/
│   ├── style.css           # Pure CSS styling
│   └── script.js           # Vanilla JavaScript
├── scripts/
│   └── setup.py            # Setup script
├── uploads/                # Temporary file uploads
├── encrypted/              # Encrypted file storage
└── decrypted/              # Decrypted file storage
\`\`\`

## 🔧 Installation & Setup

### Method 1: Automatic Setup
\`\`\`bash
python scripts/setup.py
\`\`\`

### Method 2: Manual Setup
\`\`\`bash
# Install dependencies
pip install -r requirements.txt

# Create directories
mkdir uploads encrypted decrypted

# Run the application
python app.py
\`\`\`

### Access the Application
Open your browser and navigate to: **http://localhost:5000**

## 🌐 API Endpoints

### Text Operations
- `POST /encrypt-text` - Encrypt text using specified algorithm
- `POST /decrypt-text` - Decrypt text using specified algorithm

### File Operations  
- `POST /encrypt-file` - Encrypt uploaded file
- `POST /decrypt-file` - Decrypt uploaded file
- `GET /download/<folder>/<filename>` - Download processed files

## 💻 Frontend Implementation

### Pure HTML Features
- Semantic HTML5 elements
- Form handling without frameworks
- File upload with drag & drop
- Responsive meta tags

### Pure CSS Features
- CSS Grid and Flexbox layouts
- Custom animations and transitions
- Gradient backgrounds
- Mobile-first responsive design
- No CSS frameworks (Bootstrap, Tailwind, etc.)

### Vanilla JavaScript Features
- ES6+ syntax (classes, async/await)
- Fetch API for HTTP requests
- DOM manipulation
- Event handling
- File handling with FileReader API
- No JavaScript libraries (jQuery, Axios, etc.)

## 🔒 Security Implementation

### Encryption Details
- **RSA**: OAEP padding for security
- **AES**: CBC mode with random IV
- **DES**: CBC mode with random IV

### File Handling
- Secure filename handling
- File size validation
- Temporary file cleanup
- CORS enabled for development

### Key Management
- Hardcoded symmetric keys as specified
- RSA key pair generated at startup
- Session-based key storage

## 📱 Browser Compatibility

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ Mobile browsers

## 🎯 Usage Examples

### Text Encryption
1. Enter text in the input field
2. Select algorithm (RSA/AES/DES)
3. Click "Encrypt" button
4. Copy encrypted result
5. Paste back and click "Decrypt"

### File Encryption
1. Drag & drop file or click to browse
2. Select algorithm (AES/DES recommended)
3. Click "Encrypt File"
4. Download encrypted file (.enc)
5. Upload encrypted file and decrypt

## ⚡ Performance

### Text Operations
- **Encryption**: Near-instantaneous
- **Decryption**: Near-instantaneous
- **Algorithm Speed**: AES > DES > RSA

### File Operations
- **Small files** (<1MB): Very fast
- **Medium files** (1-10MB): Fast
- **Large files** (>10MB): Several seconds

## 🐛 Troubleshooting

### Common Issues

**"Text too long for RSA encryption"**
- RSA limited to ~200 characters
- Use AES or DES for longer text

**File upload fails**
- Check file size (max 50MB)
- Ensure stable connection

**Decryption fails**
- Use same algorithm for encryption/decryption
- Verify encrypted data integrity

## 🎓 Educational Value

This system demonstrates:
- Pure web technologies without frameworks
- Cryptographic algorithm differences
- Symmetric vs asymmetric encryption
- File handling in web applications
- RESTful API design
- Responsive web design principles

## 🔮 Future Enhancements

- [ ] Hybrid encryption (RSA + AES)
- [ ] Custom key input
- [ ] Multiple file encryption
- [ ] Performance benchmarking
- [ ] File integrity verification
- [ ] Encryption strength visualization

## 📄 License

Educational project demonstrating cryptographic concepts with pure web technologies.

---

**Built with ❤️ using Pure HTML, CSS, JavaScript + Flask**
