
icon_image = Image.open("138728.jpg")
icon_image = icon_image.resize((32, 32))
icon_photo = ImageTk.PhotoImage(icon_image)
button = ttk.Button(window, text="Click Me", image=icon_photo, compound=tk.LEFT, command=button_clicked)
button.pack()