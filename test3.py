import tkinter as tk
from tkinter import ttk

def on_combobox_change(event):
    # Retrieve the selected value from the combobox
    selected_value = combobox.get()
    # Perform actions based on the selected value
    print("Selected value:", selected_value)

root = tk.Tk()

# Create a Combobox widget
combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

# Bind the ComboboxSelected event to the combobox
combobox.bind("<<ComboboxSelected>>", on_combobox_change)

root.mainloop()
