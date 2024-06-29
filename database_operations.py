import mysql.connector
from dotenv import load_dotenv
import os
from tkinter import messagebox

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variables
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

def add_data(student):
    if (student.var_dept.get() == '' or 
        student.var_email.get() == '' or 
        student.var_std_id.get() == '' or 
        student.var_address.get() == '' or 
        student.var_std_name.get() == '' or 
        student.var_semester.get() == '' or 
        student.var_roll.get() == '' or 
        student.var_gender.get() == '' or 
        student.var_div.get() == '' or 
        student.var_phone.get() == '' or 
        student.var_teacher.get() == '' or 
        student.var_dob.get() == '' or 
        student.var_course.get() == '' or 
        student.var_year.get() == ''):
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

            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                student.var_std_id.get(),
                student.var_dept.get(), 
                student.var_course.get(), 
                student.var_year.get(),
                student.var_semester.get(),
                student.var_std_name.get(),
                student.var_div.get(),
                student.var_roll.get(),
                student.var_gender.get(),
                student.var_dob.get(),
                student.var_email.get(),
                student.var_phone.get(),
                student.var_address.get(),
                student.var_teacher.get()
            ))
            conn.commit()
            student.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student has been added.", parent=student.root)
        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}.", parent=student.root)

def fetch_data(student):
    # Implement the fetch_data function
    pass

def reset_data(student):
    # Implement the reset_data function
    pass

def update_data(student):
    # Implement the update_data function
    pass

def delete_data(student):
    # Implement the delete_data function
    pass

def search_data(student):
    # Implement the search_data function
    pass
