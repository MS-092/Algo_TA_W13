import tkinter as tk
from system import UniversitySystem

class UniversityGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("University Course Registration System")
        self.system = UniversitySystem()
        self.system.initialize_data()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Courses").grid(row=0, column=0, columnspan=2)
        tk.Label(self.master, text="Students").grid(row=0, column=3, columnspan=2)

        self.courses_listbox = tk.Listbox(self.master, height=10, width=40)
        self.students_listbox = tk.Listbox(self.master, height=10, width=40)

        # Showcase list for possible courses and already registered students
        for course in self.system.courses:
            self.courses_listbox.insert(tk.END, f"{course.code}: {course.title}")

        for student in self.system.students:
            self.students_listbox.insert(tk.END, f"{student.name} ({student.student_id})")

        self.courses_listbox.grid(row=1, column=0, columnspan=2)
        self.students_listbox.grid(row=1, column=3, columnspan=2)

        tk.Label(self.master, text="Student ID:").grid(row=2, column=0)
        tk.Label(self.master, text="Course Code:").grid(row=3, column=0)

        self.student_id_entry = tk.Entry(self.master)
        self.course_code_entry = tk.Entry(self.master)

        self.student_id_entry.grid(row=2, column=1)
        self.course_code_entry.grid(row=3, column=1)

        tk.Button(self.master, text="Enroll", command=self.enroll_student).grid(row=4, column=0, columnspan=2)
        tk.Button(self.master, text="Display Course Details", command=self.display_course_details).grid(row=5, column=0, columnspan=2)
        tk.Button(self.master, text="Display Student Info", command=self.display_student_info).grid(row=6, column=0, columnspan=2)
        tk.Button(self.master, text="Add New Student", command=self.add_new_student).grid(row=7, column=0, columnspan=2)

    def enroll_student(self):
        student_id = self.student_id_entry.get()
        course_code = self.course_code_entry.get()
        self.system.enroll_student_in_course(student_id, course_code)
        self.update_lists()

    def display_course_details(self):
        course_code = self.course_code_entry.get()
        self.system.display_course_details(course_code)

    def display_student_info(self):
        student_id = self.student_id_entry.get()
        self.system.display_student_info(student_id)

    def add_new_student(self):
        self.system.add_new_student()
        self.update_lists()

    def update_lists(self):
        self.courses_listbox.delete(0, tk.END)
        self.students_listbox.delete(0, tk.END)

        for course in self.system.courses:
            self.courses_listbox.insert(tk.END, f"{course.code}: {course.title}")

        for student in self.system.students:
            self.students_listbox.insert(tk.END, f"{student.name} ({student.student_id})")