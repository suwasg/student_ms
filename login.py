from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import json
# Import StudentManagementSystem class from the student.py file
try:
    from student import StudentManagementSystem
except ImportError:
    StudentManagementSystem = None
class LoginWindow:
    def __init__(self, root, redirect_to_main=False):
        # Set the root window and its properties
        self.root = root
        self.root.title("Login")
        self.root.geometry("1400x750+0+0")

        self.redirect_to_main = redirect_to_main

        # Load and display background image
        self.bg = ImageTk.PhotoImage(file=r'C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\college1.png')
        self.lbl_bg = Label(self.root, image=self.bg)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for the login section
        self.frame = Frame(self.root, bg='yellow')
        self.frame.place(x=500, y=180, width=340, height=350)

        # Load and display login icon image
        img1= Image.open(r"images\loginIcon.png")
        img1=img1.resize((100,100), Image.LANCZOS)
        self.photo_img1= ImageTk.PhotoImage(img1)
        self.lbl_img1 = Label(image=self.photo_img1, bg="yellow", borderwidth=0)
        self.lbl_img1.place(x=620, y=185, width=100, height=100)
        
        # Label for "Welcome" text
        get_started = Label(self.frame, text="Welcome", font=("times new roman", 25, "bold"), fg="black", bg="yellow")
        get_started.place(x=100, y=105)

        # user label
        user_name = Label(self.frame, text='User Name',font=("times new roman", 15, "bold"), fg="black", bg="yellow")
        user_name.place(x=70, y=150)

        self.txt_user = ttk.Entry(self.frame, font=("times new roman", 15, "bold"))
        self.txt_user.place(x=40, y=180, width=270)

        # password label
        password = Label(self.frame, text='Password',font=("times new roman", 15, "bold"), fg="black", bg="yellow")
        password.place(x=70, y=210)

        self.txt_pass = ttk.Entry(self.frame, font=("times new roman", 15, "bold"), ) # show="*"
        self.txt_pass.place(x=40, y=240, width=270)

        # Icon Images
        img2= Image.open(r"C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\loginIcon.png")
        img2=img2.resize((25,25), Image.LANCZOS)
        self.photo_img2= ImageTk.PhotoImage(img2)
        self.lbl_img2 = Label(image=self.photo_img2, bg="yellow", borderwidth=0)
        self.lbl_img2.place(x=540, y=330, width=25, height=25)

        img3= Image.open(r"C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\pass.png")
        img3=img3.resize((25,25), Image.LANCZOS)
        self.photo_img3= ImageTk.PhotoImage(img3)
        self.lbl_img3 = Label(image=self.photo_img3, bg="yellow", borderwidth=0)
        self.lbl_img3.place(x=540, y=390, width=25, height=25)

        # login button
        login_btn = Button(self.frame, text="Login",command=self.login, font=("times new roman", 15 , "bold"),fg='white', bg='blue', bd=3, relief=RIDGE, activeforeground="white", activebackground="blue")
        login_btn.place(x=110, y=300, width=120)

    # login function
    def login(self):
        "Login Functionality"
        # Load credentials from json file:
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)
        
        username = self.txt_user.get()
        password = self.txt_pass.get()

         # Check if the credentials are valid
        user = next((user for user in credentials['users'] if user['username'] == username and user['password'] == password), None)

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required.")
        elif user and user['role'] == 1:
            if self.redirect_to_main:
                messagebox.showinfo("Login Success", "Welcome to Student Management System.")
                self.open_student_management_system()
            
        elif user:
            messagebox.showinfo("Access Denied", "You do not have the required permissions to access this system.")
        else:
            messagebox.showerror("Error", "Invalid username and password.")
    
    def open_student_management_system(self):
        "open the student management system"
        if StudentManagementSystem is None:
            messagebox.showerror("Error", "Student management system module is not available.")
            return
        # Destroy all widgets in the frame and root
        self.lbl_bg.destroy()
        self.frame.destroy()
        self.lbl_img1.destroy()
        self.lbl_img2.destroy()
        self.lbl_img3.destroy()

        # Initialize the Student Management System in the same root window
        self.app = StudentManagementSystem(self.root)

if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
