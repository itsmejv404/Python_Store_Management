import tkinter as tk
from tkinter import ttk
import mysql.connector

# Create a function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pystoremanagement"
        )
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)
        return None

# Create a function to execute SQL queries
def execute_query(query):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor
    except mysql.connector.Error as error:
        print("Error executing query:", error)
    return None

# Create a function to insert a new record
def insert_record():
    name = name_entry.get()
    age = age_entry.get()
    query = f"INSERT INTO students (name, age) VALUES ('{name}', {age})"
    execute_query(query)
    display_records()

# Create a function to update a record
def update_record():
    selected_item = records_list.selection()
    if selected_item:
        name = name_entry.get()
        age = age_entry.get()
        record_id = records_list.item(selected_item)['text']
        query = f"UPDATE students SET name='{name}', age={age} WHERE id={record_id}"
        execute_query(query)
        display_records()

# Create a function to delete a record
def delete_record():
    selected_item = records_list.selection()
    if selected_item:
        record_id = records_list.item(selected_item)['text']
        query = f"DELETE FROM students WHERE id={record_id}"
        execute_query(query)
        display_records()

# Create a function to display records in the ListView
def display_records():
    records_list.delete(*records_list.get_children())
    query = "SELECT * FROM students"
    cursor = execute_query(query)
    if cursor:
        for row in cursor:
            records_list.insert("", "end", text=row[0], values=(row[1], row[2]))

# Create the main window
window = tk.Tk()
window.title("Student Records")

# Create the input fields and buttons
name_label = ttk.Label(window, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(window)
name_entry.grid(row=0, column=1)

age_label = ttk.Label(window, text="Age:")
age_label.grid(row=1, column=0, sticky=tk.W)
age_entry = ttk.Entry(window)
age_entry.grid(row=1, column=1)

insert_button = ttk.Button(window, text="Insert", command=insert_record)
insert_button.grid(row=2, column=0)

update_button = ttk.Button(window, text="Update", command=update_record)
update_button.grid(row=2, column=1)

delete_button = ttk.Button(window, text="Delete", command=delete_record)
delete_button.grid(row=2, column=2)

# Create the ListView to display records
columns = ("Name", "Age")
records_list = ttk.Treeview(window, columns=columns, show="headings")
records_list.heading("Name", text="Name")
records_list.heading("Age", text="Age")
records_list.grid(row=3, column=0, columnspan=3)

# Display the initial records
display_records()

# Start the Tkinter event loop
window.mainloop()
