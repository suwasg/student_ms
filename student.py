from tkinter import * 
from PIL import Image, ImageTk 
import os
import mysql.connector # mysql-connector-python
from tkinter import ttk, messagebox, filedialog
import database_operations as db_ops
from dotenv import load_dotenv
import cv2

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variables
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')


class Student:
    def __init__(self, root):
        self.root=root 

        # geometry
        root.geometry("1400x750+0+0")
        # self.root.geometry("1400x750+0+0")
        # title
        root.title("STUDENT MANAGEMENT SYSTEM")

        # variables
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        # first image
        img=Image.open(r"images\std1.png")
        # img=Image.open("images/std1.png")
        img=img.resize((450, 160), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,command=self.open_image, image=self.photoimg, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=450, height=160)
        # second image
        img_2=Image.open(r"images\std2.png")
        # img=Image.open("images/std1.png")
        img_2=img_2.resize((450, 160), Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,command=self.open_image2, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=450, y=0, width=450, height=160)
        # third image
        img_3=Image.open(r"images\std3.png")
        # img=Image.open("images/std1.png")
        img_3=img_3.resize((450, 160), Image.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,command=self.open_image3, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=900, y=0, width=450, height=160)

        # bg_image
        img_4=Image.open(r"images\college1.png")
        # img=Image.open("images/std1.png")
        img_4=img_4.resize((1450, 710), Image.LANCZOS)
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
        img_5=img_5.resize((535, 120), Image.LANCZOS)
        # img_5=img_5.resize((535, 120), Image.ANTIALIAS) previous PIL version.
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
        dept_combo=ttk.Combobox(std_label_info_frame,textvariable=self.var_dept ,font=("times new roman", 12, 'bold') , width=15, state='readonly')
        dept_combo['value']=("Select Department", "Computer", "IT", "Civil","Mechanic", "Electric")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=4, sticky=W) # sticky=West

        # courses
        course_label=Label(std_label_info_frame, text="Courses", font=("times new roman", 12, 'bold'), bg="white", fg="black" )
        course_label.grid(row=0, column=2, padx=2, sticky=W)

        # combobox
        course_combo=ttk.Combobox(std_label_info_frame, textvariable=self.var_course, font=("halvetica", 12, 'bold') , width=15, state='readonly')
        course_combo['value']=("Select Course", "FE", "BE", "SE","TE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=4, sticky=W) # sticky=West

        # year
        current_year=Label(std_label_info_frame, text="Current Year", font=("arial", 12, 'bold'), bg="white", fg="black" )
        current_year.grid(row=1, column=0, padx=2, sticky=W)

        # combobox
        current_year_combo=ttk.Combobox(std_label_info_frame,textvariable=self.var_year, font=("times new roman", 12, 'bold') , width=15, state='readonly')
        current_year_combo['value']=("Select Year", "2020-2021", "2021-2022", "2022-2023","2023-2024", "2024-2025")
        current_year_combo.current(0)
        current_year_combo.grid(row=1, column=1, padx=2, pady=4, sticky=W) # sticky=West


        # semester
        semester_label=Label(std_label_info_frame, text="Semester", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        semester_label.grid(row=1, column=2, padx=2, sticky=W)

        # combobox
        semester_combo=ttk.Combobox(std_label_info_frame, textvariable=self.var_semester, font=("poppins", 12, 'bold') , width=15, state='readonly')
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
        id_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_std_id,font=("times new roman", 12, 'bold'), width=15 )
        id_entry.grid(row=0, column=1, sticky=W, padx=2)

        # name label
        name_label=Label(std_label_class_frame, text="Student Name", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        name_label.grid(row=0, column=2,pady=4, padx=2, sticky=W)

        # name entry field
        name_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_std_name,font=("times new roman", 12, 'bold'), width=15 )
        name_entry.grid(row=0, column=3, sticky=W,pady=4, padx=2)

        # section
        sec_label=Label(std_label_class_frame, text="Section", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        sec_label.grid(row=1, column=0, padx=2,pady=4, sticky=W)

        sec_combo=ttk.Combobox(std_label_class_frame,textvariable=self.var_div, state="readonly",font=("poppins", 12, 'bold'), width=15)
        sec_combo['value']=("Select Section", "A", "B", "C")
        sec_combo.current(0)
        sec_combo.grid(row=1, column=1, sticky=W, padx=2,pady=4)


        # roll
        roll_label=Label(std_label_class_frame, text="Roll No", font=("arial", 12, 'bold'), bg="white", fg="black" )
        roll_label.grid(row=1, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        roll_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_roll,font=("arial", 12, 'bold'), width=15 )
        roll_entry.grid(row=1, column=3, sticky=W, padx=2, pady=4)


        # gender
        gender_label=Label(std_label_class_frame, text="Gender", font=("poppins", 12, 'bold'), bg="white", fg="black" )
        gender_label.grid(row=2, column=0, padx=2,pady=4, sticky=W)

        gender_combo=ttk.Combobox(std_label_class_frame,textvariable=self.var_gender, state="readonly",font=("poppins", 12, 'bold'), width=15)
        gender_combo['value']=("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, sticky=W, padx=2,pady=4)
        

        # dob
        dob_label=Label(std_label_class_frame, text="DOB", font=("arial", 12, 'bold'), bg="white", fg="black" )
        dob_label.grid(row=2, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        dob_entry=ttk.Entry(std_label_class_frame,textvariable=self.var_dob , font=("arial", 12, 'bold'), width=15 )
        dob_entry.grid(row=2, column=3, sticky=W, padx=2, pady=4)

        # email
        email_label=Label(std_label_class_frame, text="Email", font=("arial", 12, 'bold'), bg="white", fg="black" )
        email_label.grid(row=3, column=0, padx=2,pady=4, sticky=W)

        # name entry field
        email_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_email, font=("arial", 12, 'bold'), width=15 )
        email_entry.grid(row=3, column=1, sticky=W, padx=2, pady=4)

        # phone
        phone_label=Label(std_label_class_frame, text="Phone", font=("arial", 12, 'bold'), bg="white", fg="black" )
        phone_label.grid(row=3, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        phone_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_phone,font=("arial", 12, 'bold'), width=15 )
        phone_entry.grid(row=3, column=3, sticky=W, padx=2, pady=4)

        # address
        address_label=Label(std_label_class_frame, text="Address", font=("arial", 12, 'bold'), bg="white", fg="black" )
        address_label.grid(row=4, column=0, padx=2,pady=4, sticky=W)

        # name entry field
        address_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_address,font=("arial", 12, 'bold'), width=15 )
        address_entry.grid(row=4, column=1, sticky=W, padx=2, pady=4)

        # teacher
        teacher_label=Label(std_label_class_frame, text="Teacher", font=("arial", 12, 'bold'), bg="white", fg="black" )
        teacher_label.grid(row=4, column=2, padx=2,pady=4, sticky=W)

        # name entry field
        teacher_entry=ttk.Entry(std_label_class_frame, textvariable=self.var_teacher, font=("arial", 12, 'bold'), width=15 )
        teacher_entry.grid(row=4, column=3, sticky=W, padx=2, pady=4)



        # button frame
        btn_frame=Frame(left_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=400, width=650, height=38)

        
        btn_add=Button(btn_frame, text="Save", command=self.add_data,font=("times new roman", 12, 'bold'), width=13, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=4, )
        
        btn_update=Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=0, column=1, padx=4, )

        btn_delete=Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 12, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=0, column=2, padx=4, )

        btn_reset=Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, 'bold'), width=13, bg='blue', fg='white')
        btn_reset.grid(row=0, column=3, padx=4, )







        # right frame
        right_frame=LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Student Information", font=("times new roman", 12, 'bold'))
        right_frame.place(x=585, y=10, width=610, height=470)


        # img_6
        img_6=Image.open(r"images\std2.png")
        img_6=img_6.resize((600, 170), Image.LANCZOS)
        # img_5=img_5.resize((535, 120), Image.ANTIALIAS) previous PIL version.
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img=Label(right_frame, image=self.photoimg_6, bd=2, relief=RIDGE)
        my_img.place(x=0, y=0, width=600, height=170)

        # search frame
        search_frame=LabelFrame(right_frame, bd=4, relief=RIDGE, padx=2, pady=4, fg="red",bg='white',  text="Search Student Information", font=("times new roman", 12, 'bold'))
        search_frame.place(x=0, y=170, width=600, height=60)

        # search label
        search_by_label=Label(search_frame, text="search by: ", font=("arial", 12, 'bold'), bg="black", fg="white" )
        search_by_label.grid(row=0, column=0, padx=5, sticky=W)

        # search text combobox
        self.var_search_combo = StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search_combo, font=("halvetica", 12, 'bold') , width=13, state='readonly')
        search_combo['value']=("Select Options",'name', "roll",'section', "phone", "student_id", 'dept', 'course', 'semester', 'teacher', 'address', 'dob', 'email', 'gender')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, sticky=W) # sticky=West

        # text search/ entry field
        self.var_search = StringVar()
        search_entry=ttk.Entry(search_frame, textvariable=self.var_search,font=("arial", 12, 'bold'), width=13 )
        search_entry.grid(row=0, column=2, sticky=W, padx=4)

        # search button
        btn_search=Button(search_frame, command=self.search_data, text="Search",font=("times new roman", 12, 'bold'), width=10, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=2, )

        btn_showall=Button(search_frame,command=self.fetch_data, text="Show All",font=("times new roman", 12, 'bold'), width=10, bg='blue', fg='white')
        btn_showall.grid(row=0, column=4, padx=2, )

        # --------------------Student Table and Scroll bar-----------------
        table_frame=Frame(right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=235, width=600, height=200) # frame bhanda bahira januparda place use, bhitra grid.

        # scrollbar
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        # treeview
        self.student_table=ttk.Treeview(table_frame, columns=('id',"dept", 'course', 'year', 'sem', 'name', 'div', 'roll', 'gender', 'dob', 'email', 'phone','address', 'teacher'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # config scrollbar with table
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # 
        self.student_table.heading('id', text='StudentId')
        self.student_table.heading('dept', text='Department')
        self.student_table.heading('course', text='Course')
        self.student_table.heading('year', text='Year')
        self.student_table.heading('sem', text='Semester')
        self.student_table.heading('name', text='Student Name')
        self.student_table.heading('div', text='Class Div')
        self.student_table.heading('roll', text='Roll No')
        self.student_table.heading('gender', text='Gender')
        self.student_table.heading('dob', text='DOB')
        self.student_table.heading('email', text='Email')
        self.student_table.heading('phone', text='Phone No')
        self.student_table.heading('address', text='Address')
        self.student_table.heading('teacher', text='Teacher Name')

        self.student_table['show']='headings' # removes the first empty heading.

        # heading width set
        self.student_table.column("id", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
    

    def add_data(self):
        # db_ops.add_data(self)
        if (self.var_dept.get()=='' or self.var_email.get()=='' or self.var_std_id.get()=='' or self.var_address.get()=='' or self.var_std_name.get()=='' or self.var_semester.get()=='' or self.var_roll.get()=='' or self.var_gender.get()=='' or self.var_div.get()=='' or self.var_phone.get()=='' or self.var_teacher.get()=='' or self.var_dob.get()=='' or self.var_course.get()=='' or self.var_year.get()=='' ):
            messagebox.showerror("Error", "All Fields are required.")
        else:
            try:
                conn = mysql.connector.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    password=db_password,
                    database=db_name
                    )

                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (   self.var_std_id.get(),
                    self.var_dept.get(), 
                    self.var_course.get(), 
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student has been added.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}.", parent=self.root)
    
    def fetch_data(self):
        conn = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password,
                database=db_name
             )
        my_cursor=conn.cursor()
        my_cursor.execute('SELECT * FROM students')
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

      # get cursor
    def get_cursor(self, event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content['values']

        self.var_std_id.set(data[0])
        self.var_dept.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
    
    # update data
    def update_data(self):
        if (self.var_dept.get()=='' or self.var_email.get()=='' or self.var_std_id.get()=='' or self.var_address.get()=='' or self.var_std_name.get()=='' or self.var_semester.get()=='' or self.var_roll.get()=='' or self.var_gender.get()=='' or self.var_div.get()=='' or self.var_phone.get()=='' or self.var_teacher.get()=='' or self.var_dob.get()=='' or self.var_course.get()=='' or self.var_year.get()=='' ):
            messagebox.showerror("Error", "All Fields are required.")
        else:
            try:
                update=messagebox.askyesno("Update", "Are You Sure Update this Student Data?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(
                        host=db_host,
                        port=db_port,
                        user=db_user,
                        password=db_password,
                        database=db_name
                    )
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE students SET dept=%s, course=%s, year=%s, semester=%s, name=%s, section=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s  WHERE student_id=%s", (
                        self.var_dept.get(), 
                        self.var_course.get(), 
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_std_id.get()

                    )
                    )
                else:
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Student data has been successfully updated.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}.", parent=self.root) 
    
    # delete data 
    def delete_data(self):
        if (self.var_dept.get()=='' or self.var_email.get()=='' or self.var_std_id.get()=='' or self.var_address.get()=='' or self.var_std_name.get()=='' or self.var_semester.get()=='' or self.var_roll.get()=='' or self.var_gender.get()=='' or self.var_div.get()=='' or self.var_phone.get()=='' or self.var_teacher.get()=='' or self.var_dob.get()=='' or self.var_course.get()=='' or self.var_year.get()=='' ):
            messagebox.showerror("Error", "All Fields are required.", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete", "Are you sure delete this student data? ", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(
                        host=db_host,
                        port=db_port,
                        user=db_user,
                        password=db_password,
                        database=db_name
                    )
                    my_cursor=conn.cursor()
                    # my_cursor.execute("")
                    sql="DELETE FROM students WHERE student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursor.execute(sql, value)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Delete", "Student has been deleted.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}.", parent=self.root) 

    # reset data
    def reset_data(self):
        self.var_std_id.set("")
        self.var_dept.set('Select Department')
        self.var_course.set('Select Course')
        self.var_year.set('Select Year')
        self.var_semester.set('Select Semester')
        self.var_std_name.set("")
        self.var_div.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
    
    # search data
    def search_data(self):
        if self.var_search_combo.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please Select Option.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host=db_host,
                    port=db_port,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                my_cursor = conn.cursor()

                # List of valid columns to prevent SQL injection
                valid_columns = ["student_id",'section', "name", "roll", "dept", "course", "year", "semester", "gender", "dob", "email", "phone", "address", "teacher"]

                column_name = str(self.var_search_combo.get())
                search_value = str(self.var_search.get())

                if column_name not in valid_columns:
                    messagebox.showerror("Error", "Invalid search column", parent=self.root)
                else:
                    # Parameterized query to prevent SQL injection
                    query = f"SELECT * FROM students WHERE {column_name} = %s"
                    my_cursor.execute(query, (search_value,))
                    data = my_cursor.fetchall()

                    if len(data) != 0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("", END, values=i)
                    else:
                        messagebox.showinfo("Info", "No record found", parent=self.root)

                conn.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}.", parent=self.root)
            finally:
            # Ensure the connection is closed even if an error occurs
                if conn.is_connected():
                    conn.close()

    def open_image(self):
        try:
            # Open file dialog to select an image
            flnm = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open Images",
                filetypes=(('JPG File', "*.jpg"), ("PNG File", "*.png"), ("JPEG File", "*.jpeg"), ("All Files", "*.*"))
            )

            # Check if a file was selected
            if flnm:
                # Open and resize the selected image
                img_b = Image.open(flnm)
                img_browse = img_b.resize((450, 160), Image.LANCZOS)

                # Convert the image to PhotoImage for tkinter
                self.photoimg_browse = ImageTk.PhotoImage(img_browse)

                # Update the button image (ensure btn_1 is properly initialized)
                if self.btn_1 is not None:
                    self.btn_1.config(image=self.photoimg_browse)
                else:
                    messagebox.showerror("Error", "Button not initialized.", parent=self.root)
            else:
                messagebox.showinfo("Info", "No file selected.", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {str(e)}", parent=self.root)

    def open_image2(self):
        try:
            # Open file dialog to select an image
            flnm2 = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open Images",
                filetypes=(('JPG File', "*.jpg"), ("PNG File", "*.png"), ("JPEG File", "*.jpeg"), ("All Files", "*.*"))
            )

            # Check if a file was selected
            if flnm2:
                # Open and resize the selected image
                img_b2 = Image.open(flnm2)
                img_browse2 = img_b2.resize((450, 160), Image.LANCZOS)

                # Convert the image to PhotoImage for tkinter
                self.photoimg_browse2 = ImageTk.PhotoImage(img_browse2)

                # Update the button image (ensure btn_1 is properly initialized)
                self.btn_2.config(image=self.photoimg_browse2)
              
            else:
                messagebox.showinfo("Info", "No file selected.", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {str(e)}", parent=self.root)

    def open_image3(self):
        try:
            # Open file dialog to select an image
            flnm3 = filedialog.askopenfilename(
                initialdir=os.getcwd(),
                title="Open Images",
                filetypes=(('JPG File', "*.jpg"), ("PNG File", "*.png"), ("JPEG File", "*.jpeg"), ("All Files", "*.*"))
            )

            # Check if a file was selected
            if flnm3:
                # Open and resize the selected image
                img_b3 = Image.open(flnm3)
                img_browse3 = img_b3.resize((450, 160), Image.LANCZOS)

                # Convert the image to PhotoImage for tkinter
                self.photoimg_browse3 = ImageTk.PhotoImage(img_browse3)

                # Update the button image (ensure btn_1 is properly initialized)
                if self.btn_3 is not None:
                    self.btn_3.config(image=self.photoimg_browse3)
                else:
                    messagebox.showerror("Error", "Button not initialized.", parent=self.root)
            else:
                messagebox.showinfo("Info", "No file selected.", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {str(e)}", parent=self.root)
 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()