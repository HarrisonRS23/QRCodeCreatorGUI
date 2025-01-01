import tkinter as tk
import qrcode
from tkinter import PhotoImage


# after clicking button change screens then user can click back and image will show qr code in another screen


def create_qr_code():
    print("Creating QR code")
    url = url_entry.get()
    if url != "": 
        # create qrcode
        img = qrcode.make(url)
        # save qrcode as image
        type(img)  # qrcode.image.pil.PilImage
        img.save("qrcode/image.png")



    else:
        print("Empty URL")


root = tk.Tk()
root.title('QR code generator')

word = tk.Label(root, text='Enter in the QR Code!')
word.pack()

url_entry = tk.StringVar()
entry1 = tk.Entry(root, textvariable=url_entry)
entry1.pack()

button = tk.Button(root, text='Create QR CODE', width=25, command=create_qr_code)
button.pack()

root.mainloop()

