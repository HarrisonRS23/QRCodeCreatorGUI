import tkinter as tk
import qrcode
from tkinter import PhotoImage
import time

# Define a global variable for the image reference
image_reference = None

def create_qr_code():
    global image_reference  # Declare the global variable
    print("Creating QR code")
    url = url_entry.get()
    if url != "": 
        # create qrcode
        img = qrcode.make(url)
        # save qrcode as image
        img.save("image.png")

        for widget in root.winfo_children():
            widget.destroy()

        time.sleep(1)
        # show the image
        
        image_reference = PhotoImage(file="image.png")  # Keep a reference
        image_label = tk.Label(root, image=image_reference)
        image_label.pack()

        # Add a "Back" button to return to the home page
        back_button = tk.Button(root, text="Back", command=create_home_page)
        back_button.pack()

    else:
        print("Empty URL")

def create_home_page():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the current screen

    word = tk.Label(root, text='Enter the URL to generate a QR Code:')
    word.pack()

    entry1 = tk.Entry(root, textvariable=url_entry)
    entry1.pack()

    button = tk.Button(root, text='Create QR CODE', width=25, command=create_qr_code)
    button.pack()


root = tk.Tk()
root.title('QR Code Generator')

url_entry = tk.StringVar()

create_home_page()
root.mainloop()