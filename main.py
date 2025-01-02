import tkinter as tk
import qrcode
from tkinter import PhotoImage

# Define a global variable for the image reference
image_reference = None

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
        image_label.pack()

        # Add a "Back" button to return to the home page
        back_button = tk.Button(root, text="Back", command=create_home_page)
        back_button.pack()

    else:
        # TODO: Announce to user they need to add a URL 
        print("Empty URL")


def create_home_page():
    for widget in root.winfo_children():
        widget.destroy()  # Clear the current screen

    word = tk.Label(root, text='Enter the URL to generate a QR Code:')
    word.pack()

    # Text entry used to hold url user wants to convert
    entry1 = tk.Entry(root, textvariable=url_entry)
    entry1.pack()

    # Create QR code button launches the function
    button = tk.Button(root, text='Create QR CODE', width=25, command=create_qr_code)
    button.pack()

# Create main window
root = tk.Tk()
root.title('QR Code Generator')
# Create url entry variable that will be accessed later
url_entry = tk.StringVar()

# Create home page and start main loop (show window)
create_home_page()
root.mainloop()