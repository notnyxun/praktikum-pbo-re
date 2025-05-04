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


class UserManager:
    """Class untuk mengelola data user"""
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
        else:
            self.users = {}
    
    def save_users(self):
        """Simpan user ke file"""
        with open(self.filepath, 'w') as file:
            json.dump(self.users, file)
    
    def register_user(self, username, password):
        """Registrasi user baru"""
        if username in self.users:
            return False
        
        user = User(username, password)
        self.users[username] = user.to_dict()
        self.save_users()
        return True
    
    def validate_login(self, username, password):
        """Validasi login user"""
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False


class BaseWindow:
    """Class dasar untuk window"""
    def __init__(self, master=None, title="Window", icon=None):
        self.master = tk.Toplevel(master) if master else tk.Tk()
        self.master.title(title)
        self.master.resizable(False, False)
        
        # Set icon jika ada
        if icon:
            self.master.iconbitmap(icon)
        
        # Center window
        self.center_window(400, 200)
        
    def center_window(self, width, height):
        """Posisikan window di tengah layar"""
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        self.master.geometry(f"{width}x{height}+{x}+{y}")
    
    def show(self):
        """Tampilkan window"""
        self.master.mainloop()
        
    def close(self):
        """Tutup window"""
        self.master.destroy()


class NotificationWindow(BaseWindow):
    """Class untuk window notifikasi"""
    def __init__(self, master=None, title="Notification", message=""):
        super().__init__(master, title)
        
        # Frame utama
        frame = tk.Frame(self.master, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Icon info
        self.info_icon = tk.Label(frame, text="i", font=("Arial", 16, "bold"), 
                                  fg="white", bg="#0078D7", width=2, height=1)
        self.info_icon.grid(row=0, column=0, padx=(0, 10))
        
        # Pesan
        self.message_label = tk.Label(frame, text=message, font=("Arial", 10))
        self.message_label.grid(row=0, column=1, sticky="w")
        
        # Tombol OK
        self.ok_button = tk.Button(frame, text="OK", width=10, command=self.close)
        self.ok_button.grid(row=1, column=0, columnspan=2, pady=(20, 0))
        
        # Posisikan elemen di tengah
        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)
        
        self.master.protocol("WM_DELETE_WINDOW", self.close)


class LoginWindow(BaseWindow):
    """Class untuk window login"""
    def __init__(self, user_manager):
        super().__init__(title="Login")
        self.user_manager = user_manager
        
        # Frame utama
        frame = tk.Frame(self.master, padx=20, pady=20)
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
        login_button.grid(row=2, column=0, columnspan=2, pady=(20, 10))
        
        # Tombol Register
        register_button = tk.Button(frame, text="Register", width=10, command=self.open_register)
        register_button.grid(row=3, column=0, columnspan=2)
        
        # Bind enter key ke login
        self.master.bind('<Return>', lambda event: self.login())
    
    def login(self):
        """Proses login user"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
            return
        
        if self.user_manager.validate_login(username, password):
            # Login sukses
            self.master.withdraw()  # Sembunyikan window login
            notification = NotificationWindow(self.master, "Login Successful", f"Welcome, {username}!")
            notification.master.protocol("WM_DELETE_WINDOW", lambda: self.close_app(notification))
        else:
            messagebox.showerror("Login Failed", "Username atau password salah!")
    
    def close_app(self, notification_window):
        """Tutup aplikasi setelah notifikasi ditutup"""
        notification_window.close()
        self.close()
    
    def open_register(self):
        """Buka window register"""
        self.master.withdraw()  # Sembunyikan window login
        register_window = RegisterWindow(self.master, self.user_manager)
        register_window.master.protocol("WM_DELETE_WINDOW", lambda: self.show_login(register_window))
    
    def show_login(self, register_window):
        """Tampilkan kembali window login saat register ditutup"""
        register_window.close()
        self.master.deiconify()  # Tampilkan kembali window login


class RegisterWindow(BaseWindow):
    """Class untuk window register"""
    def __init__(self, master, user_manager):
        super().__init__(master, "Register")
        self.user_manager = user_manager
        self.login_window = master
        
        # Frame utama
        frame = tk.Frame(self.master, padx=20, pady=20)
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
        
        # Tombol Register
        register_button = tk.Button(frame, text="Register", width=10, command=self.register)
        register_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))
        
        # Bind enter key ke register
        self.master.bind('<Return>', lambda event: self.register())
    
    def register(self):
        """Proses registrasi user"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
            return
        
        if self.user_manager.register_user(username, password):
            # Register sukses
            self.master.withdraw()  # Sembunyikan window register
            notification = NotificationWindow(self.master, "Registration Successful", "You have successfully registered")
            notification.master.protocol("WM_DELETE_WINDOW", lambda: self.back_to_login(notification))
        else:
            messagebox.showerror("Registration Failed", "Username sudah digunakan!")
    
    def back_to_login(self, notification_window):
        """Kembali ke window login setelah registrasi sukses"""
        notification_window.close()
        self.close()
        self.login_window.deiconify()  # Tampilkan kembali window login


def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    user_manager = UserManager()
    app = LoginWindow(user_manager)
    app.show()


if __name__ == "__main__":
    main()