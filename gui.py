import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
import subprocess
from datetime import datetime
from modules.crypto import encrypt_file, decrypt_file
from modules.shredder import shred_file
from modules.password_checker import check_password
from modules.report import generate_report

actions = []

class EncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption Tool v3.0")
        self.root.geometry("600x580")
        self.root.configure(bg="#0d1117")
        self.root.resizable(False, False)
        self.build_ui()

    def build_ui(self):
        # Title
        tk.Label(self.root, text="File Encryption Tool",
                 font=("Segoe UI", 18, "bold"),
                 bg="#0d1117", fg="#58a6ff").pack(pady=16)

        tk.Label(self.root, text="AES-256 | Secure Shredder | v3.0",
                 font=("Segoe UI", 10),
                 bg="#0d1117", fg="#888").pack()

        # File selection
        frame1 = tk.Frame(self.root, bg="#161b22",
                          highlightbackground="#30363d",
                          highlightthickness=1)
        frame1.pack(fill="x", padx=20, pady=16)

        tk.Label(frame1, text="Selected File",
                 font=("Segoe UI", 10),
                 bg="#161b22", fg="#888").pack(anchor="w", padx=12, pady=(10,0))

        frow = tk.Frame(frame1, bg="#161b22")
        frow.pack(fill="x", padx=12, pady=8)

        self.file_var = tk.StringVar(value="No file selected")
        tk.Label(frow, textvariable=self.file_var,
                 font=("Segoe UI", 10),
                 bg="#161b22", fg="#c9d1d9",
                 width=45, anchor="w").pack(side="left")

        tk.Button(frow, text="Browse",
                  font=("Segoe UI", 9),
                  bg="#21262d", fg="#58a6ff",
                  relief="flat", cursor="hand2",
                  command=self.browse_file).pack(side="right")

        # Password
        frame2 = tk.Frame(self.root, bg="#161b22",
                          highlightbackground="#30363d",
                          highlightthickness=1)
        frame2.pack(fill="x", padx=20, pady=4)

        tk.Label(frame2, text="Password",
                 font=("Segoe UI", 10),
                 bg="#161b22", fg="#888").pack(anchor="w", padx=12, pady=(10,0))

        self.pass_var = tk.StringVar()
        self.pass_var.trace("w", self.on_password_change)

        tk.Entry(frame2, textvariable=self.pass_var,
                 show="*", font=("Segoe UI", 11),
                 bg="#21262d", fg="#c9d1d9",
                 insertbackground="#c9d1d9",
                 relief="flat", width=40).pack(padx=12, pady=8, fill="x")

        # Password strength
        self.strength_label = tk.Label(frame2, text="",
                                        font=("Segoe UI", 9),
                                        bg="#161b22", fg="#888")
        self.strength_label.pack(anchor="w", padx=12)

        self.strength_bar = ttk.Progressbar(frame2, length=560,
                                             mode="determinate",
                                             maximum=4)
        self.strength_bar.pack(padx=12, pady=(4,8), fill="x")

        self.crack_label = tk.Label(frame2, text="",
                                     font=("Segoe UI", 9),
                                     bg="#161b22", fg="#888")
        self.crack_label.pack(anchor="w", padx=12, pady=(0,8))

        # Shred checkbox
        self.shred_var = tk.BooleanVar()
        tk.Checkbutton(self.root,
                       text="Securely shred original file after encryption",
                       variable=self.shred_var,
                       font=("Segoe UI", 10),
                       bg="#0d1117", fg="#c9d1d9",
                       selectcolor="#21262d",
                       activebackground="#0d1117").pack(pady=8)

        # Buttons
        bframe = tk.Frame(self.root, bg="#0d1117")
        bframe.pack(pady=8)

        tk.Button(bframe, text="Encrypt",
                  font=("Segoe UI", 11, "bold"),
                  bg="#238636", fg="white",
                  relief="flat", cursor="hand2",
                  padx=20, pady=8,
                  command=self.encrypt).pack(side="left", padx=8)

        tk.Button(bframe, text="Decrypt",
                  font=("Segoe UI", 11, "bold"),
                  bg="#1f6feb", fg="white",
                  relief="flat", cursor="hand2",
                  padx=20, pady=8,
                  command=self.decrypt).pack(side="left", padx=8)

        tk.Button(bframe, text="Report",
                  font=("Segoe UI", 11, "bold"),
                  bg="#6e40c9", fg="white",
                  relief="flat", cursor="hand2",
                  padx=20, pady=8,
                  command=self.save_report).pack(side="left", padx=8)

        # Status
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(self.root, textvariable=self.status_var,
                 font=("Segoe UI", 10),
                 bg="#0d1117", fg="#888").pack(pady=4)

        # Log
        tk.Label(self.root, text="Activity Log",
                 font=("Segoe UI", 10),
                 bg="#0d1117", fg="#888").pack(anchor="w", padx=20)

        self.log = tk.Text(self.root, height=8,
                           font=("Consolas", 9),
                           bg="#161b22", fg="#c9d1d9",
                           relief="flat", state="disabled",
                           padx=8, pady=8)
        self.log.pack(fill="x", padx=20, pady=4)

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_var.set(path)

    def on_password_change(self, *args):
        pwd = self.pass_var.get()
        if not pwd:
            self.strength_label.config(text="")
            self.crack_label.config(text="")
            self.strength_bar["value"] = 0
            return
        result = check_password(pwd)
        self.strength_bar["value"] = result["score"]
        self.strength_label.config(
            text=f"{result['label']}",
            fg=result["color"]
        )
        self.crack_label.config(
            text=f"Crack time: {result['crack_time']}"
        )

    def log_message(self, msg):
        self.log.config(state="normal")
        self.log.insert("end", msg + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    def encrypt(self):
        filepath = self.file_var.get()
        password = self.pass_var.get()
        if filepath == "No file selected" or not password:
            messagebox.showwarning("Missing Info",
                                   "Please select a file and enter a password!")
            return

        self.status_var.set("Encrypting...")
        self.log_message(f"[*] Encrypting: {os.path.basename(filepath)}")

        def run():
            size   = os.path.getsize(filepath)
            output = encrypt_file(filepath, password)
            if output:
                self.log_message(f"[+] Done: {os.path.basename(output)}")
                actions.append({
                    "file":     os.path.basename(filepath),
                    "action":   "Encrypted",
                    "time":     datetime.now().strftime("%H:%M:%S"),
                    "size":     f"{size} bytes",
                    "shredded": self.shred_var.get()
                })
                if self.shred_var.get():
                    shred_file(filepath)
                    self.log_message(
                        f"[~] Shredded: {os.path.basename(filepath)}")
                self.status_var.set("Encryption complete!")
                messagebox.showinfo("Done!", f"Encrypted:\n{output}")
            else:
                self.log_message("[!] Encryption failed!")
                self.status_var.set("Encryption failed!")

        threading.Thread(target=run, daemon=True).start()

    def decrypt(self):
        filepath = self.file_var.get()
        password = self.pass_var.get()
        if filepath == "No file selected" or not password:
            messagebox.showwarning("Missing Info",
                                   "Please select a file and enter a password!")
            return

        self.status_var.set("Decrypting...")
        self.log_message(f"[*] Decrypting: {os.path.basename(filepath)}")

        def run():
            size   = os.path.getsize(filepath)
            output = decrypt_file(filepath, password)
            if output:
                self.log_message(f"[+] Done: {os.path.basename(output)}")
                actions.append({
                    "file":     os.path.basename(filepath),
                    "action":   "Decrypted",
                    "time":     datetime.now().strftime("%H:%M:%S"),
                    "size":     f"{size} bytes",
                    "shredded": False
                })
                self.status_var.set("Decryption complete!")
                messagebox.showinfo("Done!", f"Decrypted:\n{output}")
            else:
                self.log_message("[!] Decryption failed — wrong password?")
                self.status_var.set("Decryption failed!")

        threading.Thread(target=run, daemon=True).start()

    def save_report(self):
        if not actions:
            messagebox.showinfo("No Actions",
                                "Please encrypt or decrypt a file first!")
            return
        os.makedirs("output", exist_ok=True)
        path = os.path.abspath(
            f"output/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        )
        html = generate_report(actions)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        self.log_message(f"[+] Report saved: {path}")
        messagebox.showinfo("Report Saved!", f"Report saved to:\n{path}")
        subprocess.Popen(["start", path], shell=True)

if __name__ == "__main__":
    root = tk.Tk()
    app  = EncryptorApp(root)
    root.mainloop()