from tkinter import *
from PIL import Image,ImageTk ##pip install pillow
class ImageBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Browser")

        # List to store image paths
        self.image_paths = []

        # Create a listbox to display image names
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.show_image)

        # Create a canvas to display images
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load images from a directory
        self.load_images("path/to/directory")  # Replace with your image directory path

    def load_images(self, directory):
        # Clear the listbox and canvas
        self.listbox.delete(0, tk.END)
        self.canvas.delete("all")

        # Get all image file paths in the directory
        for filename in os.listdir(directory):
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".gif")):
                self.image_paths.append(os.path.join(directory, filename))
                self.listbox.insert(tk.END, filename)

    def show_image(self, event):
        # Get the selected image index from the listbox
        selection = self.listbox.curselection()
        if selection:
            index = int(selection[0])

            # Load the selected image
            image_path = self.image_paths[index]
            image = Image.open(image_path)
            image = image.resize((500, 500))  # Adjust the size as needed
            photo = ImageTk.PhotoImage(image)

            # Clear the canvas and display the image
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.image = photo
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Add a new Employee')
        self.root.wm_iconbitmap('images/icons.ico')
        self.root.geometry("1250x675+0+0")
        self.root.maxsize(1250, 675)
        self.root.minsize(1250,675)
        self.bg = ImageTk.PhotoImage(file='138728.jpg')
        bg = Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
        self.left = ImageTk.PhotoImage(file='images/sideimage.png')
        left=Label(self.root,image=self.left).place(x = 80,y = 100,width=400,height=500)

        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y = 100,width=700,height=500)

        title = Label(frame1,text='Add New Employee',font=("Verdana",20,"bold"),bg="white",fg='green').place(x=50,y=30)
        lblFirstName = Label(frame1,text='First Name :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=80)
        lblLastName = Label(frame1,text='Last Name :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=110)
        lblEmail = Label(frame1,text='Email :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=140)
        lblPassword = Label(frame1,text='Password :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=170)
        lblPhoneNumber = Label(frame1,text='Phone Number :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=200)
        lblDateOfBirth = Label(frame1,text='Date of Birth :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=230)
        lblDoorNum = Label(frame1,text='Door No :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=260)
        lblStreet = Label(frame1,text='Street :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=290)
        lblArea = Label(frame1,text='Area :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=320)
        lblCity = Label(frame1,text='City :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=350)
        lblState = Label(frame1,text='State :',font=("Verdana",10,"bold"),bg="white",fg='green').place(x=50,y=380)
        txtFirstName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtLastName = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtEmail = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtPassword = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtPhoneNumber = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtDateOfBirth = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtDoorNum = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtStreet = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtArea = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtCity = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtState = Entry(frame1,font=("Verdana",10,"bold"),bg="white",fg='black')
        txtFirstName.place(x=170,y=80) 
        txtLastName.place(x=170,y=110)
        txtEmail.place(x=170,y=140)
        txtPassword.place(x=170,y=170)
        txtPhoneNumber.place(x=170,y=200)
        txtDateOfBirth.place(x=170,y=230)
        txtDoorNum.place(x=170,y=260)
        txtStreet.place(x=170,y=290)
        txtArea.place(x=170,y=320)
        txtCity.place(x=170,y=350)
        txtState.place(x=170,y=380)


    
root=Tk()

obj = Register(root)
root.mainloop()