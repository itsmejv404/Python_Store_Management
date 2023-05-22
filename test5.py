import tkinter as tk

def hide_window():
    root.withdraw()

root = tk.Tk()
root.title("Main Window")

hide_button = tk.Button(root, text="Hide Window", command=hide_window)
hide_button.pack()

root.mainloop()