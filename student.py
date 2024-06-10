from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk 

class Student:
    def __init__(self, root):
        self.root=root 

        # geometry
        root.geometry("1400x750+0+0")
        # self.root.geometry("1400x750+0+0")
        # title
        root.title("STUDENT MANAGEMENT SYSTEM")

        # first image
        img=Image.open(r"images\std1.png")
        # img=Image.open("images/std1.png")
        img=img.resize((450, 160), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=450, height=160)
        # second image
        img_2=Image.open(r"images\std2.png")
        # img=Image.open("images/std1.png")
        img_2=img_2.resize((450, 160), Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=450, y=0, width=450, height=160)
        # third image
        img_3=Image.open(r"images\std3.png")
        # img=Image.open("images/std1.png")
        img_3=img_3.resize((450, 160), Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=900, y=0, width=450, height=160)

        # bg_image
        img_4=Image.open(r"images\college1.png")
        # img=Image.open("images/std1.png")
        img_4=img_4.resize((1450, 710), Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_label=Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_label.place(x=0, y=160, width=1450, height=710)
        # label title
        label_title=Label(bg_label, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), fg="blue", bg="yellow", pady=5)
        label_title.place(x=0, y=0, width=1450, height=50)
        

        # manage frame
        manage_frame=Frame(bg_label, bd=2, relief=RIDGE, bg='white')
        manage_frame.place(x=25, y=55, width=1220, height=500)


        # left frame
        left_frame=LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Student Information", font=("times new roman", 12, 'bold'))
        left_frame.place(x=25, y=10, width=550, height=470)

        # img_5
        img_5=Image.open(r"images\std4.png")
        img_5=img_5.resize((535, 120), Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(left_frame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=535, height=110)

        # current course label frame information
        std_label_info_frame=LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Current Course Information", font=("times new roman", 12, 'bold'))
        std_label_info_frame.place(x=0, y=110, width=535, height=90)

        # department
        # labels
        dept_label=Label(std_label_info_frame, text="Department", font=("times new roman", 12, 'bold'), bg="white", fg="black" )
        dept_label.grid(row=0, column=0, padx=2, sticky=W)

        # combobox
        dept_combo=ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold') , width=15, state='readonly')
        dept_combo['value']=("Select Department", "Computer", "IT", "Civil","Mechanic", "Electric")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=4, sticky=W) # sticky=West

        # courses
        course_label=Label(std_label_info_frame, text="Courses", font=("times new roman", 12, 'bold'), bg="white", fg="black" )
        course_label.grid(row=0, column=2, padx=2, sticky=W)

        # combobox
        course_combo=ttk.Combobox(std_label_info_frame, font=("halvetica", 12, 'bold') , width=15, state='readonly')
        course_combo['value']=("Select Course", "FE", "BE", "SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=4, sticky=W) # sticky=West

        # year
        current_year=Label(std_label_info_frame, text="Current Year", font=("arial", 12, 'bold'), bg="white", fg="black" )
        current_year.grid(row=1, column=0, padx=2, sticky=W)

        # combobox
        current_year_combo=ttk.Combobox(std_label_info_frame, font=("times new roman", 12, 'bold') , width=15, state='readonly')
        current_year_combo['value']=("Select Year", "2020-2021", "2021-2022", "2022-2023","2023-2024", "2024-2025")
        current_year_combo.current(0)
        current_year_combo.grid(row=1, column=1, padx=2, pady=4, sticky=W) # sticky=West


        # semester
        semester_label=Label(std_label_info_frame, text="Semester", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        semester_label.grid(row=1, column=2, padx=2, sticky=W)

        # combobox
        semester_combo=ttk.Combobox(std_label_info_frame, font=("poppins", 12, 'bold') , width=15, state='readonly')
        semester_combo['value']=("Select Semester", "Semester-1", "Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=4, sticky=W) # sticky=West

        # student class label information
        std_label_class_frame=LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Class Course Information", font=("times new roman", 12, 'bold'))
        std_label_class_frame.place(x=0, y=200, width=535, height=200)

        # id label
        id_label=Label(std_label_class_frame, text="Student Id", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        id_label.grid(row=0, column=0,pady=4, padx=2, sticky=W)

        # id entry field
        id_entry=ttk.Entry(std_label_class_frame,font=("times new roman", 12, 'bold'), width=15 )
        id_entry.grid(row=0, column=1, sticky=W, padx=2)

        # name label
        name_label=Label(std_label_class_frame, text="Student Name", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        name_label.grid(row=0, column=2,pady=4, padx=2, sticky=W)

        # name entry field
        name_entry=ttk.Entry(std_label_class_frame,font=("times new roman", 12, 'bold'), width=15 )
        name_entry.grid(row=0, column=3, sticky=W,pady=4, padx=2)

        # section
        sec_label=Label(std_label_class_frame, text="Section", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        sec_label.grid(row=1, column=0, padx=2,pady=4, sticky=W)

        sec_combo=ttk.Combobox(std_label_class_frame, state="readonly",font=("poppins", 12, 'bold'), width=15)
        sec_combo['value']=("Select Section", "A", "B", "C")
        sec_combo.current(0)
        sec_combo.grid(row=1, column=1, sticky=W, padx=2,pady=4)


        # roll
        roll_label=Label(std_label_class_frame, text="Roll No", font=("arial", 12, 'bold'), bg="white", fg="black" )
        roll_label.grid(row=1, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        roll_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        roll_entry.grid(row=1, column=3, sticky=W, padx=2, pady=4)


        # gender
        gender_label=Label(std_label_class_frame, text="Gender", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        gender_label.grid(row=2, column=0, padx=2,pady=4, sticky=W)

        gender_combo=ttk.Combobox(std_label_class_frame, state="readonly",font=("poppins", 12, 'bold'), width=15)
        gender_combo['value']=("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, sticky=W, padx=2,pady=4)
        

        # dob
        dob_label=Label(std_label_class_frame, text="DOB", font=("arial", 12, 'bold'), bg="white", fg="black" )
        dob_label.grid(row=2, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        dob_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        dob_entry.grid(row=2, column=3, sticky=W, padx=2, pady=4)

        # email
        email_label=Label(std_label_class_frame, text="Email", font=("arial", 12, 'bold'), bg="white", fg="black" )
        email_label.grid(row=3, column=0, padx=2,pady=4, sticky=W)

        # name entry field
        email_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        email_entry.grid(row=3, column=1, sticky=W, padx=2, pady=4)

        # phone
        phone_label=Label(std_label_class_frame, text="Phone", font=("arial", 12, 'bold'), bg="white", fg="black" )
        phone_label.grid(row=3, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        phone_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        phone_entry.grid(row=3, column=3, sticky=W, padx=2, pady=4)

        # address
        address_label=Label(std_label_class_frame, text="Address", font=("arial", 12, 'bold'), bg="white", fg="black" )
        address_label.grid(row=4, column=0, padx=2,pady=4, sticky=W)

        # name entry field
        address_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        address_entry.grid(row=4, column=1, sticky=W, padx=2, pady=4)

        # teacher
        teacher_label=Label(std_label_class_frame, text="Teacher", font=("arial", 12, 'bold'), bg="white", fg="black" )
        teacher_label.grid(row=4, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        teacher_entry=ttk.Entry(std_label_class_frame,font=("arial", 12, 'bold'), width=15 )
        teacher_entry.grid(row=4, column=3, sticky=W, padx=2, pady=4)





        # right frame
        right_frame=LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Student Information", font=("times new roman", 12, 'bold'))
        right_frame.place(x=585, y=10, width=610, height=470)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()