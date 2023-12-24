import tkinter as tk
from tkinter import messagebox
from course import Course
from student import Student


class UniversitySystem:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    # Functions to ensure that students and courses are properly initialized
    def enroll_student_in_course(self, student_id, course_code):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.code == course_code), None)

        # Conditions for student ID/Name into enrolling into course, etc.
        if student and course:
            if student not in course.enrolled_students:
                if course.enroll_student(student):
                    messagebox.showinfo("Success", f"Enrolled {student.name} in {course.title}")
                else:
                    messagebox.showwarning("Warning", f"Course {course.title} is full!")
            else:
                messagebox.showinfo("Info", f"{student.name} is already enrolled in {course.title}")
        else:
            messagebox.showerror("Error", "Student or Course not found!")

    def add_new_student(self):
        student_id = tk.simpledialog.askstring("New Student", "Enter Student ID:")
        name = tk.simpledialog.askstring("New Student", "Enter Name:")

        if student_id and name:
            # Check for any duplicate student ID or name
            duplicate_id = any(s.student_id == student_id for s in self.students)
            duplicate_name = any(s.name == name for s in self.students)

            if duplicate_id and duplicate_name:
                messagebox.showwarning("Warning", f"Student ID '{student_id}' and Name '{name}' already exist!")
            elif duplicate_id:
                messagebox.showwarning("Warning", f"Student ID '{student_id}' already exists!")
            elif duplicate_name:
                messagebox.showwarning("Warning", f"Student Name '{name}' already exists!")
            else:
                new_student = Student(student_id, name)
                self.add_student(new_student)
                messagebox.showinfo("Success", f"Added new student: {name} ({student_id})")


    # Showcase details and information
    def display_course_details(self, course_code):
        course = next((c for c in self.courses if c.code == course_code), None)
        if course:
            messagebox.showinfo("Course Details", course.display_course_details())
        else:
            messagebox.showerror("Error", "Course not found!")

    def display_student_info(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            messagebox.showinfo("Student Info", student.display_student_info())
        else:
            messagebox.showerror("Error", "Student not found!")

    # Preparing pre-data about the students and courses
    def initialize_data(self):
        # Course(Code of the course, Title of the course, maximum capacity of the class)
        c1 = Course("CSCI101", "Introduction to Programming", 10)
        c2 = Course("MATH201", "Calculus I", 15)
        c3 = Course("PHY101", "Physics I", 10)
        c4 = Course("ENG102", "English Composition", 15)
        c5 = Course("CHEM201", "Chemistry I", 5)

        # Showing list of courses in GUI
        self.add_course(c1)
        self.add_course(c2)
        self.add_course(c3)
        self.add_course(c4)
        self.add_course(c5)

        # Student(Student ID, Student Name)
        s1 = Student("1001", "John Doe")
        s2 = Student("1002", "Jane Smith")
        s3 = Student("1003", "Bob Johnson")
        s4 = Student("1004", "Alice Lee")
        s5 = Student("1005", "Charlie Brown")
        s6 = Student("1006", "Eva Miller")
        s7 = Student("1007", "David Wang")
        s8 = Student("1008", "Grace Chen")
        s9 = Student("1009", "Michael Brown")
        s10 = Student("1010", "Emily Davis")
        s11 = Student("1011", "Ryan Wilson")
        s12 = Student("1012", "Sophia Miller")
        s13 = Student("1013", "Daniel Garcia")
        s14 = Student("1014", "Mia Thompson")
        s15 = Student("1015", "Owen Johnson")
        s16 = Student("1016", "Ava Harris")

        # Showing list of students in GUI
        self.add_student(s1)
        self.add_student(s2)
        self.add_student(s3)
        self.add_student(s4)
        self.add_student(s5)
        self.add_student(s6)
        self.add_student(s7)
        self.add_student(s8)
        self.add_student(s9)
        self.add_student(s10)
        self.add_student(s11)
        self.add_student(s12)
        self.add_student(s13)
        self.add_student(s14)
        self.add_student(s15)
        self.add_student(s16)

        # Enrolling students that are already in the system into specific courses
        
        # Programming (Max: 10)
        c1.enroll_student(s1)
        c1.enroll_student(s2)
        c1.enroll_student(s3)
        c1.enroll_student(s7)
        c1.enroll_student(s9)
        c1.enroll_student(s10)
        c1.enroll_student(s14)

        # Calculus (Max: 15)
        c2.enroll_student(s2)
        c2.enroll_student(s4)
        c2.enroll_student(s6)
        c2.enroll_student(s10)
        c2.enroll_student(s12)
        c2.enroll_student(s15)
        c2.enroll_student(s16)

        # Physics (Max: 10)
        c3.enroll_student(s1)
        c3.enroll_student(s3)
        c3.enroll_student(s5)
        c3.enroll_student(s8)
        c3.enroll_student(s11)
        c3.enroll_student(s13)
        c3.enroll_student(s16)

        # English (Max: 15)
        c4.enroll_student(s4)
        c4.enroll_student(s6)
        c4.enroll_student(s8)
        c4.enroll_student(s13)
        c4.enroll_student(s14)
        c4.enroll_student(s15)

        # Chemistry (Max: 5) - This course is used as an example, as the course that's already full
        c5.enroll_student(s5)
        c5.enroll_student(s7)
        c5.enroll_student(s9)
        c5.enroll_student(s11)
        c5.enroll_student(s12)