from tkinter import Tk, Button, Label
from tkinter import filedialog
from PIL import Image, ImageTk

def pick_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

window = Tk()


window.mainloop()