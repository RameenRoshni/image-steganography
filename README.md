# Image Steganography Application

A GUI-based Image Steganography application developed using Python. This tool allows users to hide and extract images using the Least Significant Bit (LSB) technique.

## Features

- User-friendly GUI (Tkinter)
- Upload images at runtime
- Encode (hide) secret image inside cover image
- Decode hidden image from encoded image
- Image preview panels
- Modern dark-themed interface

## Technologies Used

- Python
- OpenCV
- NumPy
- Tkinter
- PIL (Pillow)

## How to Run

1. Clone the repository:

git clone https://github.com/RameenRoshni/image-steganography.git


2. Navigate to folder:

cd image-steganography


3. Run the application:

python steganography_app_gui.py

## Working Principle

This application uses the **Least Significant Bit (LSB)** technique:

- During encoding:
  - The least significant bits of the cover image are replaced with bits from the secret image.
  
- During decoding:
  - These bits are extracted to reconstruct the hidden image.


## Author

Rameen Roshni

## GitHub Link

https://github.com/RameenRoshni/image-steganography
