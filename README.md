# 🔐 File Encryption Tool

A powerful AES-256 file encryption desktop app built in Python.
Encrypt any file or entire folders with a password. Includes GUI, secure shredder, password strength checker, and HTML reports.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-3.0-orange)
![Encryption](https://img.shields.io/badge/Encryption-AES--256-red)

---

## 🚀 Features

- **AES-256 Encryption** — Military-grade encryption used by banks and governments
- **GUI App** — Beautiful dark-themed desktop app built with tkinter
- **Password Strength** — Real-time password strength checker using zxcvbn
- **Password-based Key** — Derive secure key using PBKDF2 with 100,000 iterations
- **File Encryption** — Encrypt any file type (.txt, .pdf, .jpg, .docx etc.)
- **Folder Encryption** — Encrypt all files in a folder with one command (CLI)
- **Secure Shredder** — Overwrite original file 3 times before deleting
- **Wrong Password Rejection** — Decryption fails safely with wrong password
- **Activity Report** — HTML report of all encryption/decryption actions
- **Colored CLI Output** — Clean, color-coded terminal output

---

## 📋 Requirements
```
Python 3.x
pip install cryptography colorama zxcvbn
```

---

## 📁 Project Structure
```
file-encryptor/
├── gui.py              ← Desktop GUI app (tkinter)
├── encryptor.py        ← CLI entry point
├── modules/
│   ├── crypto.py       ← AES-256 encryption/decryption
│   ├── shredder.py     ← Secure file shredder
│   ├── password_checker.py  ← Password strength (zxcvbn)
│   └── report.py       ← HTML report generator
└── output/             ← Reports saved here
```

---

## ⚡ Usage

### GUI App (Recommended)
```bash
python gui.py
```

### CLI Usage

**Encrypt a file:**
```bash
python encryptor.py -e secret.txt -p mypassword
```

**Decrypt a file:**
```bash
python encryptor.py -d secret.txt.enc -p mypassword
```

**Encrypt and shred original:**
```bash
python encryptor.py -e secret.txt -p mypassword -s
```

**Encrypt entire folder:**
```bash
python encryptor.py -e myfolder -p mypassword
```

**See all options:**
```bash
python encryptor.py --help
```

---

## 🖥️ GUI Features

| Feature | Description |
|---------|-------------|
| Browse | Select any file from your system |
| Password field | Hidden input with real-time strength analysis |
| Strength bar | Color-coded bar (red = weak, green = strong) |
| Crack time | Estimated time to crack your password |
| Shred checkbox | Securely delete original after encryption |
| Activity log | Live log of all actions in the app |
| Report button | Generate HTML report of all actions |

---

## 📊 Sample CLI Output
```
==================================================
      File Encryption Tool v2.0
      AES-256 | Secure Shredder
==================================================

[*] Encrypting: secret.txt
[+] Encrypted: secret.txt.enc
[~] Original shredded: secret.txt

[*] Done!
```

---

## 🔧 How It Works
```
Password + Random Salt
        │
        ▼
   PBKDF2HMAC (100,000 iterations)
        │
        ▼
   AES-256-GCM Key
        │
        ▼
   Encrypt File Data
        │
        ▼
   Salt + Nonce + Encrypted Data → .enc file
```

---

## 🔒 Security Details

| Feature | Detail |
|---------|--------|
| Algorithm | AES-256-GCM |
| Key Derivation | PBKDF2HMAC + SHA256 |
| Iterations | 100,000 |
| Salt | 16 bytes random |
| Nonce | 12 bytes random |
| Shredder | 3-pass random overwrite |
| Password Analysis | zxcvbn (used by Dropbox) |

---

## 🛡️ Disclaimer

This tool is for **educational purposes** and **personal use only**.
Do not use to encrypt files you do not own or have permission to encrypt.

---

## 👨‍💻 Author

**Tamil Pagalavan E**
B.E. Computer Science Engineering (Cyber Security)
2nd Year | Aspiring Security Engineer

[![GitHub](https://img.shields.io/badge/GitHub-pagalavan22-181717?logo=github)](https://github.com/pagalavan22)