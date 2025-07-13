// Pure Vanilla JavaScript - No frameworks or libraries
class CryptoSystem {
  constructor() {
    this.initializeEventListeners()
    this.selectedFile = null
    this.lastOperation = null
  }

  initializeEventListeners() {
    // Text encryption buttons
    document.getElementById("encryptTextBtn").addEventListener("click", () => this.encryptText())
    document.getElementById("decryptTextBtn").addEventListener("click", () => this.decryptText())
    document.getElementById("clearTextBtn").addEventListener("click", () => this.clearText())

    // File upload handling
    const uploadArea = document.getElementById("uploadArea")
    const fileInput = document.getElementById("fileInput")

    uploadArea.addEventListener("click", () => fileInput.click())
    uploadArea.addEventListener("dragover", this.handleDragOver.bind(this))
    uploadArea.addEventListener("dragleave", this.handleDragLeave.bind(this))
    uploadArea.addEventListener("drop", this.handleDrop.bind(this))

    fileInput.addEventListener("change", (e) => this.handleFileSelect(e.target.files[0]))

    // File encryption buttons
    document.getElementById("encryptFileBtn").addEventListener("click", () => this.encryptFile())
    document.getElementById("decryptFileBtn").addEventListener("click", () => this.decryptFile())
    document.getElementById("clearFileBtn").addEventListener("click", () => this.clearFile())

    // Download button
    document.getElementById("downloadBtn").addEventListener("click", () => this.downloadResult())

    // Algorithm change for RSA warning
    document.getElementById("textAlgorithm").addEventListener("change", this.checkRSALimitation.bind(this))
  }

  async encryptText() {
    const text = document.getElementById("textInput").value.trim()
    const algorithm = document.getElementById("textAlgorithm").value

    if (!text) {
      this.showStatus("Please enter text to encrypt", "error")
      return
    }

    // Check RSA text length limitation
    if (algorithm === "RSA" && text.length > 200) {
      this.showStatus("RSA can only encrypt small text (max ~200 characters)", "error")
      return
    }

    try {
      this.showProgress(true, "Encrypting text...")

      const response = await fetch("/encrypt-text", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
          algorithm: algorithm,
        }),
      })

      const result = await response.json()

      if (result.success) {
        document.getElementById("textOutput").value = result.encrypted_text
        this.showStatus(`✅ Text encrypted successfully using ${algorithm}`, "success")
      } else {
        throw new Error(result.error)
      }
    } catch (error) {
      this.showStatus(`❌ Encryption failed: ${error.message}`, "error")
    } finally {
      this.showProgress(false)
    }
  }

  async decryptText() {
    const text = document.getElementById("textInput").value.trim()
    const algorithm = document.getElementById("textAlgorithm").value

    if (!text) {
      this.showStatus("Please enter ciphertext to decrypt", "error")
      return
    }

    try {
      this.showProgress(true, "Decrypting text...")

      const response = await fetch("/decrypt-text", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
          algorithm: algorithm,
        }),
      })

      const result = await response.json()

      if (result.success) {
        document.getElementById("textOutput").value = result.decrypted_text
        this.showStatus(`✅ Text decrypted successfully using ${algorithm}`, "success")
      } else {
        throw new Error(result.error)
      }
    } catch (error) {
      this.showStatus(`❌ Decryption failed: ${error.message}`, "error")
    } finally {
      this.showProgress(false)
    }
  }

  clearText() {
    document.getElementById("textInput").value = ""
    document.getElementById("textOutput").value = ""
    this.showStatus("Text fields cleared", "success")
  }

  handleDragOver(e) {
    e.preventDefault()
    document.getElementById("uploadArea").classList.add("dragover")
  }

  handleDragLeave(e) {
    e.preventDefault()
    document.getElementById("uploadArea").classList.remove("dragover")
  }

  handleDrop(e) {
    e.preventDefault()
    document.getElementById("uploadArea").classList.remove("dragover")

    const files = e.dataTransfer.files
    if (files.length > 0) {
      this.handleFileSelect(files[0])
    }
  }

  handleFileSelect(file) {
    if (!file) return

    // Check file size (50MB limit)
    const maxSize = 50 * 1024 * 1024 // 50MB
    if (file.size > maxSize) {
      this.showStatus("File too large! Maximum size is 50MB", "error")
      return
    }

    this.selectedFile = file

    // Display file information
    document.getElementById("fileName").textContent = file.name
    document.getElementById("fileSize").textContent = this.formatFileSize(file.size)
    document.getElementById("fileType").textContent = file.type || "Unknown"

    document.getElementById("fileInfo").style.display = "block"
    document.getElementById("encryptFileBtn").disabled = false
    document.getElementById("decryptFileBtn").disabled = false

    this.showStatus(`📁 File selected: ${file.name}`, "success")
  }

  async encryptFile() {
    if (!this.selectedFile) {
      this.showStatus("Please select a file first", "error")
      return
    }

    const algorithm = document.getElementById("fileAlgorithm").value

    try {
      this.showProgress(true, "Encrypting file...")

      const formData = new FormData()
      formData.append("file", this.selectedFile)
      formData.append("algorithm", algorithm)

      const response = await fetch("/encrypt-file", {
        method: "POST",
        body: formData,
      })

      const result = await response.json()

      if (result.success) {
        this.lastOperation = {
          type: "encrypt",
          filename: result.encrypted_filename,
          originalFilename: result.original_filename,
          algorithm: result.algorithm,
        }

        document.getElementById("resultText").textContent =
          `🔒 File encrypted successfully! (${this.formatFileSize(result.file_size)})`
        document.getElementById("resultArea").style.display = "block"

        this.showStatus(`✅ File encrypted successfully using ${algorithm}`, "success")
      } else {
        throw new Error(result.error)
      }
    } catch (error) {
      this.showStatus(`❌ File encryption failed: ${error.message}`, "error")
    } finally {
      this.showProgress(false)
    }
  }

  async decryptFile() {
    if (!this.selectedFile) {
      this.showStatus("Please select an encrypted file first", "error")
      return
    }

    const algorithm = document.getElementById("fileAlgorithm").value

    try {
      this.showProgress(true, "Decrypting file...")

      const formData = new FormData()
      formData.append("file", this.selectedFile)
      formData.append("algorithm", algorithm)
      formData.append("original_filename", this.selectedFile.name.replace(".enc", ""))

      const response = await fetch("/decrypt-file", {
        method: "POST",
        body: formData,
      })

      const result = await response.json()

      if (result.success) {
        this.lastOperation = {
          type: "decrypt",
          filename: result.decrypted_filename,
          algorithm: result.algorithm,
        }

        document.getElementById("resultText").textContent =
          `🔓 File decrypted successfully! (${this.formatFileSize(result.file_size)})`
        document.getElementById("resultArea").style.display = "block"

        this.showStatus(`✅ File decrypted successfully using ${algorithm}`, "success")
      } else {
        throw new Error(result.error)
      }
    } catch (error) {
      this.showStatus(`❌ File decryption failed: ${error.message}`, "error")
    } finally {
      this.showProgress(false)
    }
  }

  clearFile() {
    this.selectedFile = null
    document.getElementById("fileInfo").style.display = "none"
    document.getElementById("resultArea").style.display = "none"
    document.getElementById("encryptFileBtn").disabled = true
    document.getElementById("decryptFileBtn").disabled = true
    document.getElementById("fileInput").value = ""
    this.showStatus("File selection cleared", "success")
  }

  downloadResult() {
    if (!this.lastOperation) {
      this.showStatus("No file to download", "error")
      return
    }

    const folder = this.lastOperation.type === "encrypt" ? "encrypted" : "decrypted"
    const filename = this.lastOperation.filename

    const downloadUrl = `/download/${folder}/${filename}`

    // Create a temporary link and trigger download
    const link = document.createElement("a")
    link.href = downloadUrl
    link.download = filename
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)

    this.showStatus("⬇️ Download started", "success")
  }

  checkRSALimitation() {
    const algorithm = document.getElementById("textAlgorithm").value
    const textInput = document.getElementById("textInput")

    if (algorithm === "RSA") {
      textInput.placeholder = "Enter small text (RSA limitation: ~200 characters max)"
    } else {
      textInput.placeholder = "Enter your text here..."
    }
  }

  showProgress(show, message = "Processing...") {
    const progressBar = document.getElementById("progressBar")
    const progressFill = document.getElementById("progressFill")
    const progressText = document.getElementById("progressText")

    if (show) {
      progressBar.style.display = "block"
      progressFill.style.width = "0%"
      progressText.textContent = message

      // Simulate progress
      let progress = 0
      const interval = setInterval(() => {
        progress += Math.random() * 30
        if (progress > 90) progress = 90
        progressFill.style.width = progress + "%"
      }, 200)

      // Store interval to clear it later
      this.progressInterval = interval
    } else {
      if (this.progressInterval) {
        clearInterval(this.progressInterval)
      }
      progressFill.style.width = "100%"
      progressText.textContent = "Complete!"
      setTimeout(() => {
        progressBar.style.display = "none"
      }, 500)
    }
  }

  showStatus(message, type) {
    const statusElement = document.getElementById("statusMessage")
    statusElement.textContent = message
    statusElement.className = `status-message ${type}`
    statusElement.style.display = "block"

    setTimeout(() => {
      statusElement.style.display = "none"
    }, 4000)
  }

  formatFileSize(bytes) {
    if (bytes === 0) return "0 Bytes"

    const k = 1024
    const sizes = ["Bytes", "KB", "MB", "GB"]
    const i = Math.floor(Math.log(bytes) / Math.log(k))

    return Number.parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i]
  }
}

// Initialize the crypto system when the page loads
document.addEventListener("DOMContentLoaded", () => {
  new CryptoSystem()
  console.log("🔐 Cryptographic System initialized - Pure HTML/CSS/JS Frontend with Flask Backend")
})
