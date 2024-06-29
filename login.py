
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

        get_started = Label(self.frame, text="Welcome! Get Started.", font=("times new roman", 20, "bold"), fg="black", bg="yellow")
        get_started.place(x=125, y=105)


if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
