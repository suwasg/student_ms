from login import LoginWindow # import the LoginWindow class from login.py
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()
