
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1400x750+0+0")

        self.bg = ImageTk.PhotoImage(file=r'C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\college1.png')
        self.lbl_bg = Label(self.root, image=self.bg)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = Frame(self.root, bg='yellow')
        self.frame.place(x=500, y=150, width=340, height=450)


        img1= Image.open(r"images\loginIcon.png")
        img1=img1.resize((100,100), Image.LANCZOS)
        self.photo_img1= ImageTk.PhotoImage(img1)
        self.lbl_img1 = Label(image=self.photo_img1, bg="yellow", borderwidth=0)
        self.lbl_img1.place(x=620, y=155, width=100, height=100)

        get_started = Label(self.frame, text="Welcome", font=("times new roman", 25, "bold"), fg="black", bg="yellow")
        get_started.place(x=100, y=105)

                # labels
        user_name = Label(self.frame, text='User Name',font=("times new roman", 15, "bold"), fg="black", bg="yellow")
        user_name.place(x=70, y=150)

        self.txt_user = ttk.Entry(self.frame, font=("times new roman", 15, "bold"))
        self.txt_user.place(x=40, y=180, width=270)

        password = Label(self.frame, text='Password',font=("times new roman", 15, "bold"), fg="black", bg="yellow")
        password.place(x=70, y=210)

        self.txt_pass = ttk.Entry(self.frame, font=("times new roman", 15, "bold"), ) # show="*"
        self.txt_pass.place(x=40, y=240, width=270)

        # Icon Images
        img2= Image.open(r"C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\loginIcon.png")
        img2=img2.resize((25,25), Image.LANCZOS)
        self.photo_img2= ImageTk.PhotoImage(img2)
        self.lbl_img2 = Label(image=self.photo_img2, bg="yellow", borderwidth=0)
        self.lbl_img2.place(x=540, y=300, width=25, height=25)

        img3= Image.open(r"C:\Users\Acer\Desktop\projects_2024\tkinter\login\images\pass.png")
        img3=img3.resize((25,25), Image.LANCZOS)
        self.photo_img3= ImageTk.PhotoImage(img3)
        self.lbl_img3 = Label(image=self.photo_img3, bg="yellow", borderwidth=0)
        self.lbl_img3.place(x=540, y=360, width=25, height=25)

        login_btn = Button(self.frame, text="Login",command=self.login, font=("times new roman", 15 , "bold"),fg='white', bg='blue', bd=3, relief=RIDGE, activeforeground="white", activebackground="blue")
        login_btn.place(x=110, y=300, width=120)

    def login(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required.")
        elif self.txt_user.get() == "admin" and self.txt_pass.get() == "admin@789":
            messagebox.showinfo("Login Success", "Welcome to Student Management System.")
        else:
            messagebox.showerror("Error", "Invalid username and password.")

if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
