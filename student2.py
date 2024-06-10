from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Load and resize images
        self.images = [
            ImageTk.PhotoImage(Image.open("images/std1.png").resize((450, 160), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("images/std2.png").resize((450, 160), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("images/std3.png").resize((450, 160), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("images/college1.png").resize((1450, 710), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("images/std4.png").resize((535, 120), Image.LANCZOS)),
            ImageTk.PhotoImage(Image.open("images/std2.png").resize((600, 170), Image.LANCZOS))
        ]

        # Top image buttons
        for i in range(3):
            Button(self.root, image=self.images[i], cursor="hand2").place(x=i*450, y=0, width=450, height=160)

        # Background image
        bg_label = Label(self.root, image=self.images[3], bd=2, relief=RIDGE)
        bg_label.place(x=0, y=160, width=1450, height=710)

        # Title label
        Label(bg_label, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), fg="blue", bg="yellow", pady=5).place(x=0, y=0, width=1450, height=50)

        # Manage frame
        manage_frame = Frame(bg_label, bd=2, relief=RIDGE, bg='white')
        manage_frame.place(x=25, y=55, width=1220, height=500)

        # Left frame
        left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red", bg='white', text="Student Information", font=("times new roman", 12, 'bold'))
        left_frame.place(x=25, y=10, width=550, height=470)

        # Image in left frame
        Label(left_frame, image=self.images[4], bd=2, relief=RIDGE).place(x=0, y=0, width=535, height=110)

        # Current course information
        std_label_info_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red", bg='white', text="Current Course Information", font=("times new roman", 12, 'bold'))
        std_label_info_frame.place(x=0, y=110, width=535, height=90)

        # Department combobox
        Label(std_label_info_frame, text="Department", font=("times new roman", 12, 'bold'), bg="white", fg="black").grid(row=0, column=0, padx=2, sticky=W)
        dept_combo = ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold'), width=15, state='readonly')
        dept_combo['values'] = ("Select Department", "Computer", "IT", "Civil", "Mechanic", "Electric")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=4, sticky=W)

        # Course combobox
        Label(std_label_info_frame, text="Courses", font=("times new roman", 12, 'bold'), bg="white", fg="black").grid(row=0, column=2, padx=2, sticky=W)
        course_combo = ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold'), width=15, state='readonly')
        course_combo['values'] = ("Select Course", "FE", "BE", "SE", "TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=4, sticky=W)

        # Year combobox
        Label(std_label_info_frame, text="Current Year", font=("times new roman", 12, 'bold'), bg="white", fg="black").grid(row=1, column=0, padx=2, sticky=W)
        current_year_combo = ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold'), width=15, state='readonly')
        current_year_combo['values'] = ("Select Year", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")
        current_year_combo.current(0)
        current_year_combo.grid(row=1, column=1, padx=2, pady=4, sticky=W)

        # Semester combobox
        Label(std_label_info_frame, text="Semester", font=("times new roman", 12, 'bold'), bg="white", fg="black").grid(row=1, column=2, padx=2, sticky=W)
        semester_combo = ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold'), width=15, state='readonly')
        semester_combo['values'] = ("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=4, sticky=W)

        # Student class information
        std_label_class_frame = LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red", bg='white', text="Class Course Information", font=("times new roman", 12, 'bold'))
        std_label_class_frame.place(x=0, y=200, width=535, height=200)

        # Student class entries
        entries = [
            ("Student Id", "poppins"),
            ("Student Name", "poppins"),
            ("Section", "poppins"),
            ("Roll No", "arial"),
            ("Gender", "poppins"),
            ("DOB", "arial"),
            ("Email", "arial"),
            ("Phone", "arial"),
            ("Address", "arial"),
            ("Teacher", "arial")
        ]
        combo_values = {
            "Section": ("Select Section", "A", "B", "C"),
            "Gender": ("Select Gender", "Male", "Female", "Others")
        }

        for idx, (label_text, font_family) in enumerate(entries):
            label = Label(std_label_class_frame, text=label_text, font=(font_family, 12, 'bold'), bg="white", fg="black")
            label.grid(row=idx // 2, column=(idx % 2) * 2, padx=2, pady=4, sticky=W)
            if label_text in combo_values:
                entry = ttk.Combobox(std_label_class_frame, font=(font_family, 12, 'bold'), width=15, state='readonly')
                entry['values'] = combo_values[label_text]
                entry.current(0)
            else:
                entry = ttk.Entry(std_label_class_frame, font=(font_family, 12, 'bold'), width=15)
            entry.grid(row=idx // 2, column=(idx % 2) * 2 + 1, padx=2, pady=4, sticky=W)

        # Buttons in left frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=400, width=650, height=38)
        btn_texts = ["Save", "Update", "Delete", "Reset"]
        for idx, text in enumerate(btn_texts):
            Button(btn_frame, text=text, font=("times new roman", 12, 'bold'), width=13, bg='blue', fg='white').grid(row=0, column=idx, padx=4)

        # Right frame
        right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red", bg='white', text="Student Information", font=("times new roman", 12, 'bold'))
        right_frame.place(x=585, y=10, width=610, height=470)
        Label(right_frame, image=self.images[5], bd=2, relief=RIDGE).place(x=0, y=0, width=600, height=170)

        # Search frame
        search_frame = LabelFrame(right_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red", bg='white', text="Search Student Information", font=("times new roman", 12, 'bold'))
        search_frame.place(x=0, y=170, width=600, height=70)

        # Search frame entries
        Label(search_frame, text="Search By:", font=("times new roman", 12, 'bold'), bg="yellow", fg="red").grid(row=0, column=0, padx=2, pady=4, sticky=W)
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, 'bold'), width=15, state='readonly')
        search_combo['values'] = ("Select Option", "Roll No", "Phone", "Student Id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=4, pady=4, sticky=W)
        ttk.Entry(search_frame, font=("times new roman", 12, 'bold'), width=18).grid(row=0, column=2, padx=2, pady=4, sticky=W)
        Button(search_frame, text="Search", font=("times new roman", 12, 'bold'), width=10, bg='blue', fg='white').grid(row=0, column=3, padx=2)
        Button(search_frame, text="Show All", font=("times new roman", 12, 'bold'), width=10, bg='blue', fg='white').grid(row=0, column=4, padx=2)

        # Student data table frame
        table_frame = Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=245, width=600, height=200)

        # Student data table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dept", "course", "year", "sem", "id", "name", "sec", "roll", "gender", "dob", "email", "phone", "address", "teacher"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for col in self.student_table["column"]:
            self.student_table.heading(col, text=col.capitalize())
            self.student_table.column(col, width=100)
        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
