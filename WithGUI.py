import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageSteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("500x400")
        self.root.configure(bg="#222")
        
        self.image_path = ""
        self.create_main_menu()
    
    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Choose an Option", fg="white", bg="#222", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.root, text="Encrypt", command=self.show_encrypt_menu, bg="green", fg="white").pack(pady=5)
        tk.Button(self.root, text="Decrypt", command=self.show_decrypt_menu, bg="blue", fg="white").pack(pady=5)
    
    def show_encrypt_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Encryption", fg="white", bg="#222", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.root, text="Select Image", command=self.load_image, bg="#444", fg="white").pack(pady=5)
        self.file_label = tk.Label(self.root, text="", fg="white", bg="#222")
        self.file_label.pack()
        tk.Label(self.root, text="Enter Message:", fg="white", bg="#222").pack()
        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(pady=5)
        tk.Label(self.root, text="Enter Passcode:", fg="white", bg="#222").pack()
        self.passcode_entry = tk.Entry(self.root, width=20, show="*")
        self.passcode_entry.pack(pady=5)
        tk.Button(self.root, text="Encrypt", command=self.encrypt, bg="green", fg="white").pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg="red", fg="white").pack(pady=5)
    
    def show_decrypt_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Decryption", fg="white", bg="#222", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.root, text="Select Encrypted Image", command=self.load_image, bg="#444", fg="white").pack(pady=5)
        self.file_label = tk.Label(self.root, text="", fg="white", bg="#222")
        self.file_label.pack()
        tk.Label(self.root, text="Enter Passcode:", fg="white", bg="#222").pack()
        self.passcode_entry = tk.Entry(self.root, width=20, show="*")
        self.passcode_entry.pack(pady=5)
        tk.Button(self.root, text="Decrypt", command=self.decrypt, bg="blue", fg="white").pack(pady=5)
        
        
        tk.Label(self.root, text="Decrypted Message:", fg="white", bg="#222").pack()
        self.decrypted_message_text = tk.Text(self.root, height=4, width=40, wrap=tk.WORD)
        self.decrypted_message_text.pack(pady=5)
        self.decrypted_message_text.config(state=tk.DISABLED)
        
        tk.Button(self.root, text="Back", command=self.create_main_menu, bg="red", fg="white").pack(pady=5)
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if self.image_path:
            self.file_label.config(text=f"Selected: {os.path.basename(self.image_path)}")
    
    def encrypt(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image.")
            return
        message = self.message_entry.get().strip()
        password = self.passcode_entry.get().strip()
        if not message or not password:
            messagebox.showerror("Error", "Message and passcode cannot be empty.")
            return
        img = cv2.imread(self.image_path)
        height, width, _ = img.shape
        secret_data = f"{password}|{message}~"
        index = 0
        for row in range(height):
            for col in range(width):
                if index < len(secret_data):
                    img[row, col, 0] = ord(secret_data[index])
                    index += 1
                else:
                    break
        encrypted_path = "encryptedImage.png"
        cv2.imwrite(encrypted_path, img)
        messagebox.showinfo("Success", f"Encryption complete! Image saved as {encrypted_path}")
        os.system(f"start {encrypted_path}")
    
    def decrypt(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image.")
            return
        img = cv2.imread(self.image_path)
        height, width, _ = img.shape
        hidden_data = ""
        for row in range(height):
            for col in range(width):
                char = chr(img[row, col, 0])
                if char == "~":
                    break
                hidden_data += char
            else:
                continue
            break  
        
        hidden_data = hidden_data.strip()
        
        if "|" in hidden_data:
            stored_pass, message = hidden_data.split("|", 1)
        else:
            messagebox.showerror("Error", "Decryption failed: No valid data found!")
            return
        entered_pass = self.passcode_entry.get().strip()
        if entered_pass != stored_pass:
            messagebox.showerror("Error", "Incorrect passcode! Access Denied.")
            return
        
        
        self.decrypted_message_text.config(state=tk.NORMAL)
        self.decrypted_message_text.delete(1.0, tk.END)
        self.decrypted_message_text.insert(tk.END, message.strip())
        self.decrypted_message_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSteganographyApp(root)
    root.mainloop()
