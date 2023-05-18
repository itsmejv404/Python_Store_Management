import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
        
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2,LoginScreen):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(LoginScreen))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(LoginScreen))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lblUsername = ttk.Label(self,text = "Username").grid(row = 1, column = 0, padx = 10, pady = 10)
        txtUsername = ttk.Entry(self, text ="Username")
        txtUsername.grid(row = 1, column = 1, padx = 10, pady = 10)
        lblUsername = ttk.Label(self,text = "Password").grid(row = 2, column = 0, padx = 10, pady = 10)
        txtPassword = ttk.Entry(self, text ="Password")
        txtPassword.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        btnSubmit = ttk.Button(self, text ="Login",
                            command = loginCheck(txtUsername.get(),txtPassword.get(),controller))
        btnSubmit.grid(row = 3, column = 1, padx = 10, pady = 10)
  
def loginCheck(a,b,controller):
    print(a)
    print(b)
    controller.show_frame(Page2)
# Driver Code
app = tkinterApp()
app.title('Store Mangement')
app.mainloop()