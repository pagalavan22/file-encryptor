# 🔐 File Encryption Tool

A powerful AES-256 file encryption tool built in Python.
Encrypt any file or entire folders with a password. Includes a secure file shredder.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Version](https://img.shields.io/badge/Version-2.0-orange)
![Encryption](https://img.shields.io/badge/Encryption-AES--256-red)

---

## 🚀 Features

- **AES-256 Encryption** — Military-grade encryption used by banks and governments
- **Password-based** — Derive secure key using PBKDF2 with 100,000 iterations
- **File Encryption** — Encrypt any file type (.txt, .pdf, .jpg, .docx etc.)
- **Folder Encryption** — Encrypt all files in a folder with one command
- **Secure Shredder** — Overwrite original file 3 times before deleting
- **Wrong Password Rejection** — Decryption fails safely with wrong password
- **Colored CLI Output** — Clean, color-coded terminal output

---

## 📋 Requirements
```
Python 3.x
pip install cryptography colorama
```

---

## 📁 Project Structure
```
file-encryptor/
├── encryptor.py        ← Main entry point
├── modules/
│   ├── crypto.py       ← AES-256 encryption/decryption
│   └── shredder.py     ← Secure file shredder
└── output/             ← Output files saved here
```

---

## ⚡ Usage

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

## 📊 Sample Output
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