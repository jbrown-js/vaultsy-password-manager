# 🔐 Vaultsy

> **A modern desktop password manager built with Python and CustomTkinter.**

Vaultsy is a lightweight password manager designed to securely store, organise and manage your login credentials through a clean, dark-themed interface.

---

## ✨ Features

✅ Add new logins

✏️ Edit existing logins

🗑️ Remove saved logins

📋 Copy passwords to your clipboard

📂 Organise passwords into categories

🔎 Filter passwords by category

💾 Automatically save your vault

🔒 Encrypt all saved passwords using **Fernet (AES-128)**

🌙 Modern dark UI built with **CustomTkinter**

---

## 📂 Categories

- 👤 Personal
- 💼 Work
- 💳 Finance
- ⚙️ Utilities
- 📦 Other

---

## 🛠️ Built With

- 🐍 Python 3
- 🎨 CustomTkinter
- 🔐 Cryptography (Fernet)
- 📄 JSON

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Vaultsy.git
```

### 2. Enter the project folder

```bash
cd Vaultsy
```

### 3. Install the required libraries

```bash
pip install customtkinter cryptography
```

### 4. Generate an encryption key

```bash
python keyGen.py
```

### 5. Launch Vaultsy

```bash
python main.py
```

---

## 🔒 Encryption

Vaultsy uses **Fernet symmetric encryption** from Python's `cryptography` library.

Every password is encrypted before being saved to disk, meaning your vault cannot be read without the generated encryption key.

Passwords are stored inside an encrypted file rather than plain text, keeping your credentials protected from anyone browsing your files.

---

## 📁 Project Structure

```
Vaultsy/
│
├── main.py
├── keygen.py
├── key.key
├── passwords.dat
├── install.bat
└── README.md
```

---

## ⚠️ Disclaimer

Vaultsy is a personal learning project created to explore Python GUI development, encryption and secure data storage.

While it uses modern encryption techniques, it has **not** been professionally audited and should not be considered a replacement for established password managers for highly sensitive data.

---

## 📜 License

Licensed under the **MIT License**.

---

<div align="center">

### 🔐 Built with Python • 🎨 CustomTkinter • ❤️ By You

⭐ If you like the project, consider giving it a star!

</div>
