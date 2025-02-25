# AICTE_CYBER_INTERNSHIP
# Image Steganography Using Python

## 📌 Overview
This project is a **Python-based Image Steganography** application that allows users to securely hide and retrieve messages within images. The encryption process ensures that only users with the correct passcode can decrypt and view the hidden message.

## 🔥 Features
- **Hide Messages in Images**: Uses LSB (Least Significant Bit) steganography.
- **Passcode Protection**: Only users with the correct passcode can decrypt.
- **User-Friendly GUI**: Built with Tkinter for easy interaction.
- **Supports PNG Format**: Maintains high image quality.
- **Efficient Encryption & Decryption**: Fast and lightweight processing.
- **Error Handling**: Prevents incorrect inputs and unauthorized access.

## 📂 Technologies Used
- **Python** (Programming Language)
- **Tkinter** (Graphical User Interface)
- **OpenCV** (Image Processing)
- **OS & File Handling**

## 🚀 How to Run the Project
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/image-steganography.git
cd image-steganography
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install required libraries:
```bash
pip install opencv-python
```

### 3️⃣ Run the Application
```bash
python steganography.py
```

## 🛠️ How It Works
1. **Encryption Process**:
   - Select an image (.png format).
   - Enter a secret message and passcode.
   - The message is embedded into the image.
   - The encrypted image is saved.
2. **Decryption Process**:
   - Load the encrypted image.
   - Enter the passcode to retrieve the hidden message.

## 📸 Screenshots
| Encryption | Decryption |
|------------|-------------|
| ![Encryption GUI](screenshots/encryption.png) | ![Decryption GUI](screenshots/decryption.png) |

## 🔮 Future Enhancements
- Support for JPEG and BMP image formats.
- Audio and video steganography.
- Cloud storage integration for secure sharing.
- Mobile app version for Android and iOS.

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to fork the repository and submit pull requests for improvements.

## 📬 Contact
For any queries or collaboration, reach out via **your-email@example.com** or visit [GitHub Profile](https://github.com/yourusername).
