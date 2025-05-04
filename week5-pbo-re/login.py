import tkinter as tk
from tkinter import messagebox
import json
import os

class User:
    """Class untuk merepresentasikan user"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def to_dict(self):
        """Konversi object user ke dictionary"""
        return {
            "username": self.username,
            "password": self.password
        }


class UserAuthentication:
    """Class untuk autentikasi user"""
    def __init__(self, filepath="users.json"):
        self.filepath = filepath
        self.users = {}
        self.load_users()
    
    def load_users(self):
        """Load user dari file"""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    self.users = json.load(file)
            except json.JSONDecodeError:
                self.users = {}
                # Tambahkan user default untuk testing
                self.add_default_users()
        else:
            self.users = {}
            # Tambahkan user default untuk testing
            self.add_default_users()
            self.save_users()
    
    def add_default_users(self):
        """Tambahkan beberapa user default"""
        default_users = {
            "summer": {"username": "summer", "password": "password123"},
            "admin": {"username": "admin", "password": "admin123"}
        }
        self.users.update(default_users)
    
    def save_users(self):
        """Simpan user ke file"""
        with open(self.filepath, 'w') as file:
            json.dump(self.users, file)
    
    def validate_login(self, username, password):
        """Validasi login user"""
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False


class Window:
    """Class dasar untuk window"""
    def __init__(self, title="Window", width=400, height=200):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        
        # Center window
        self.center_window(width, height)
        
    def center_window(self, width, height):
        """Posisikan window di tengah layar"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def show(self):
        """Tampilkan window"""
        self.root.mainloop()
        
    def close(self):
        """Tutup window"""
        self.root.destroy()


class NotificationWindow:
    """Class untuk window notifikasi"""
    def __init__(self, parent, title="Login Successful", message=""):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.resizable(False, False)
        
        # Ukuran dan posisi window
        width, height = 300, 150
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        # Frame utama
        frame = tk.Frame(self.window, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Icon info
        self.info_frame = tk.Frame(frame, bg="#0078D7", width=40, height=40)
        self.info_frame.grid(row=0, column=0, padx=(0, 10))
        
        self.info_icon = tk.Label(self.info_frame, text="i", font=("Arial", 16, "bold"), 
                                 fg="white", bg="#0078D7")
        self.info_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Pesan
        self.message_label = tk.Label(frame, text=message, font=("Arial", 10))
        self.message_label.grid(row=0, column=1, sticky="w")
        
        # Tombol OK
        self.ok_button = tk.Button(frame, text="OK", width=10, command=self.close)
        self.ok_button.grid(row=1, column=0, columnspan=2, pady=(20, 0))
        
        # Set focus pada tombol OK
        self.ok_button.focus_set()
        
        # Posisikan elemen di tengah
        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)
        
        # Bind event ke tombol
        self.window.bind('<Return>', lambda event: self.close())
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        
        # Make this window modal
        self.window.transient(parent)
        self.window.grab_set()
        parent.wait_window(self.window)
    
    def close(self):
        """Tutup window"""
        self.window.destroy()


class LoginApp(Window):
    """Class untuk aplikasi login"""
    def __init__(self):
        super().__init__(title="Login", width=350, height=180)
        self.auth = UserAuthentication()
        self.create_widgets()
    
    def create_widgets(self):
        """Buat widget-widget untuk window login"""
        # Frame utama
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Label Username
        username_label = tk.Label(frame, text="Username:")
        username_label.grid(row=0, column=0, sticky="w", pady=(0, 10))
        
        # Entry Username
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.grid(row=0, column=1, pady=(0, 10), padx=(10, 0))
        
        # Label Password
        password_label = tk.Label(frame, text="Password:")
        password_label.grid(row=1, column=0, sticky="w")
        
        # Entry Password
        self.password_entry = tk.Entry(frame, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=(10, 0))
        
        # Tombol Login
        login_button = tk.Button(frame, text="Login", width=10, command=self.login)
        login_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))
        
        # Set focus pada username entry
        self.username_entry.focus_set()
        
        # Bind enter key ke login
        self.root.bind('<Return>', lambda event: self.login())
    
    def login(self):
        """Proses login user"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
            return
        
        if self.auth.validate_login(username, password):
            # Login sukses
            NotificationWindow(self.root, "Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Username atau password salah!")


def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    app = LoginApp()
    app.show()


if __name__ == "__main__":
    main()