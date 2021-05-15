# importing necessary modules
import pyperclip
import pyshorteners
from tkinter import *


# Creating a simple GUI
root = Tk()
root.geometry("600x500")
root.title("URL Shortener")
root.configure(bg="#990000")

# Strings to store URLs
url = StringVar()
url_address = StringVar()

# Function that shortens the URL 
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

# Function used to copy URL to user's clipboard
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


# Calling the GUI and setting up the form
Label(root, text="My URL Shortener", font="poppins").pack(pady=20)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text='Copy URL', command=copyurl).pack(pady=5)
root.mainloop() 