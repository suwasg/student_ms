
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



if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
