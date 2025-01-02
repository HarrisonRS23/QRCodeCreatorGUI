import tkinter as tk
import qrcode
from tkinter import PhotoImage

# Define a global variable for the image reference
image_reference = None
qr_image = None

def create_qr_code():
    global image_reference  # Declare the global variable
    print("Creating QR code")
    # Access entry variable and save as URL
    url = url_entry.get()
    # Check to see if user input a URL
    if url != "":
        # Create qrcode
        img = qrcode.make(url)
        # Save qrcode as image
        img.save("image.png")

        # Clear home window in order to switch to show qr code
        for widget in root.winfo_children():
            widget.destroy()

        # Show the qr code image
        image_reference = PhotoImage(file="image.png")  # Keep a reference
        image_label = tk.Label(root, image=image_reference)
        image_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Add a "Back" button to return to the home page
        back_button = tk.Button(root, text="Back", command=create_home_page)
        back_button.grid(row=1, column=1, pady=10)

    else:
        print("Empty URL")  # Add a message box here if needed


def create_home_page():
    global qr_image  # Declare the global variable

    for widget in root.winfo_children():
        widget.destroy()  # Clear the current screen
    
    # App title
    title_label = tk.Label(root, text="QR Code Generator", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=1, columnspan=3, pady=10)

    # Prompt text
    word = tk.Label(root, text="Enter the URL to generate a QR Code:")
    word.grid(row=1, column=1, columnspan=2, sticky="w", padx=10)

    # Text entry field
    entry1 = tk.Entry(root, textvariable=url_entry, width=40)
    entry1.grid(row=1, column=3, padx=10)

    # Create QR code button
    button = tk.Button(root, text="Create QR CODE", width=20, command=create_qr_code)
    button.grid(row=2, column=1, columnspan=3, pady=20)

# Create main window
root = tk.Tk()
root.title('QR Code Generator')

# Create url entry variable that will be accessed later
url_entry = tk.StringVar()

# Create home page and start main loop (show window)
create_home_page()
root.mainloop()