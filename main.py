from login import LoginWindow # import the LoginWindow class from login.py
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root, redirect_to_main=True)
    root.mainloop()
