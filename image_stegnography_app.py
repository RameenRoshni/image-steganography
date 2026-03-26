import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox

# Functions
def load_cover():
    global cover_path
    cover_path = filedialog.askopenfilename()
    messagebox.showinfo("Selected", "Cover Image Selected")

def load_secret():
    global secret_path
    secret_path = filedialog.askopenfilename()
    messagebox.showinfo("Selected", "Secret Image Selected")

def encode_image():
    try:
        cover = cv2.imread(cover_path)
        secret = cv2.imread(secret_path)

        secret = cv2.resize(secret, (cover.shape[1], cover.shape[0]))
        encoded = (cover & 254) | (secret >> 7)

        cv2.imwrite("encoded.png", encoded)
        messagebox.showinfo("Success", "Image encoded and saved as encoded.png")
    except:
        messagebox.showerror("Error", "Please select both images")

def decode_image():
    try:
        encoded = cv2.imread("encoded.png")
        decoded = np.zeros_like(encoded)

        for i in range(encoded.shape[0]):
            for j in range(encoded.shape[1]):
                for k in range(3):
                    decoded[i,j,k] = (encoded[i,j,k] & 1) * 255

        cv2.imwrite("decoded.png", decoded)
        messagebox.showinfo("Success", "Decoded image saved as decoded.png")
    except:
        messagebox.showerror("Error", "No encoded image found")

# GUI Window
# GUI Setup
root = Tk()
root.title("Steganography App")
root.geometry("700x600")
root.config(bg="#2c3e50")

# Title
Label(root, text="Image Steganography Tool",
      font=("Arial", 16, "bold"),
      fg="white", bg="#2c3e50").pack(pady=10)

# Image Frame (TOP)
frame = Frame(root, bg="#2c3e50")
frame.pack(pady=10)

cover_label = Label(frame, text="Cover", bg="white", width=20, height=10)
cover_label.grid(row=0, column=0, padx=10)

secret_label = Label(frame, text="Secret", bg="white", width=20, height=10)
secret_label.grid(row=0, column=1, padx=10)

output_label = Label(frame, text="Output", bg="white", width=20, height=10)
output_label.grid(row=0, column=2, padx=10)

# BUTTON FRAME (IMPORTANT FIX)
btn_frame = Frame(root, bg="#2c3e50")
btn_frame.pack(pady=30)

Button(btn_frame, text="Upload Cover Image", command=load_cover, width=20).grid(row=0, column=0, padx=10, pady=5)
Button(btn_frame, text="Upload Secret Image", command=load_secret, width=20).grid(row=0, column=1, padx=10, pady=5)

Button(btn_frame, text="Encode", command=encode_image,
       bg="#27ae60", fg="white", width=20).grid(row=1, column=0, pady=10)

Button(btn_frame, text="Decode", command=decode_image,
       bg="#e67e22", fg="white", width=20).grid(row=1, column=1, pady=10)

root.mainloop()
