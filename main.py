from tkinter import *
from PIL import Image, ImageTk
from cryptography.fernet import Fernet


# SCREEN
screen = Tk()
screen.config(background="#EAEDED", pady=30, padx=30)
screen.minsize(width=300, height=500)
screen.title("My Crypto Note Programming")

# ICON
iconPhoto = PhotoImage(file="secretIcon.png")
screen.iconphoto(False, iconPhoto)

# PHOTO
picture = Image.open("secret.png")
resizePic = picture.resize((100, 100))
photo = ImageTk.PhotoImage(resizePic)
labelImage = Label(screen, image=photo)
labelImage.pack()

# TITLE
titleLabel = Label(text="Enter Your Title", pady=5)
titleLabel.pack()
titleEntry = Entry()
titleEntry.pack()
exox = Label(text="")
exox.pack()

# SECRET
secretLabel = Label(text="Enter Your Secret")
secretLabel.pack()
secretText = Text(width=25, height=6)
secretText.pack()
exoxo = Label(text="")
exoxo.pack()

# MASTER KEY
masterLabel = Label(text="Enter Master Key")
masterLabel.pack()
masterEntry = Entry()
masterEntry.pack()
exoxox = Label(text="")
exoxox.pack()

# RESULT Label
resultLabel = Label()
resultLabel.pack()


def saveButton():
    key = masterEntry.get()
    plaintext = secretText.get("1.0", END)

    fernet = Fernet(key)
    cipher_text = fernet.encrypt(plaintext.encode())

    resultLabel.config(text=f"{cipher_text.decode()}")
    print(resultLabel)

# BUTTONS
saveButton = Button(text="Save & Encrypt", pady=5, background="#229954",command=saveButton)
saveButton.pack()

decButton = Button(text="Decrypt", pady=5, background="#B03A2E")
decButton.pack()

# CRYPTOGRAPHY






screen.mainloop()