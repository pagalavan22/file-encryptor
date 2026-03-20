import os
import argparse
from colorama import init, Fore
from modules.crypto import encrypt_file, decrypt_file
from modules.shredder import shred_file

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "      File Encryption Tool v2.0")
    print(Fore.CYAN + "      AES-256 | Secure Shredder")
    print(Fore.CYAN + "=" * 50)

def encrypt_folder(folder, password, shred):
    """Encrypt all files in a folder."""
    encrypted = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".enc"):
                continue
            filepath = os.path.join(root, file)
            print(Fore.CYAN + f"\n[*] Encrypting: {filepath}")
            output = encrypt_file(filepath, password)
            if output:
                print(Fore.GREEN + f"[+] Done: {output}")
                encrypted.append(output)
                if shred:
                    if shred_file(filepath):
                        print(Fore.YELLOW + f"[~] Shredded: {filepath}")
            else:
                print(Fore.RED + f"[!] Failed: {filepath}")
    return encrypted

def main():
    parser = argparse.ArgumentParser(
        description="File Encryption Tool v2.0 - AES-256"
    )
    parser.add_argument("-e", "--encrypt",
                        help="File or folder to encrypt")
    parser.add_argument("-d", "--decrypt",
                        help="File to decrypt (.enc)")
    parser.add_argument("-p", "--password",
                        required=True,
                        help="Password for encryption/decryption")
    parser.add_argument("-s", "--shred",
                        action="store_true",
                        help="Securely shred original file after encryption")

    args = parser.parse_args()
    print_banner()

    if args.encrypt:
        # Check if it's a folder
        if os.path.isdir(args.encrypt):
            print(Fore.CYAN + f"\n[*] Encrypting folder: {args.encrypt}")
            results = encrypt_folder(args.encrypt, args.password, args.shred)
            print(Fore.GREEN + f"\n[+] Encrypted {len(results)} file(s)!")

        # Single file
        elif os.path.isfile(args.encrypt):
            print(Fore.CYAN + f"\n[*] Encrypting: {args.encrypt}")
            output = encrypt_file(args.encrypt, args.password)
            if output:
                print(Fore.GREEN + f"[+] Encrypted: {output}")
                if args.shred:
                    if shred_file(args.encrypt):
                        print(Fore.YELLOW + f"[~] Original shredded: {args.encrypt}")
            else:
                print(Fore.RED + "[!] Encryption failed.")
        else:
            print(Fore.RED + f"[!] Not found: {args.encrypt}")

    elif args.decrypt:
        if not os.path.exists(args.decrypt):
            print(Fore.RED + f"[!] File not found: {args.decrypt}")
            return
        print(Fore.CYAN + f"\n[*] Decrypting: {args.decrypt}")
        output = decrypt_file(args.decrypt, args.password)
        if output:
            print(Fore.GREEN + f"[+] Decrypted: {output}")
        else:
            print(Fore.RED + "[!] Decryption failed — wrong password?")

    else:
        print(Fore.RED + "\n[!] Use -e to encrypt or -d to decrypt")
        print(Fore.WHITE + "    Encrypt file  : python encryptor.py -e secret.txt -p pass")
        print(Fore.WHITE + "    Decrypt file  : python encryptor.py -d secret.txt.enc -p pass")
        print(Fore.WHITE + "    Encrypt folder: python encryptor.py -e myfolder -p pass")
        print(Fore.WHITE + "    Shred original: python encryptor.py -e secret.txt -p pass -s")

    print(Fore.CYAN + "\n[*] Done!\n")

if __name__ == "__main__":
    main()