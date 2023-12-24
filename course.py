from tkinter import messagebox

class Course:
    def __init__(self, code, title, max_capacity):
        self.code = code
        self.title = title
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.enrolled_students = []

    def enroll_student(self, student):
        if self.current_capacity < self.max_capacity:
            self.current_capacity += 1
            self.enrolled_students.append(student)
            student.enroll_in_course(self)  # Update the student's selected course
            return True
        # Creating an exception, if the course is already fully enroll
        else:
            messagebox.showwarning("Warning", f"Course {self.title} is full!")
            return False

    def display_course_details(self):
        student_list = "\n".join([f"{s.name} ({s.student_id})" for s in self.enrolled_students])
        return f"Course Code: {self.code}\nTitle: {self.title}\nMax Capacity: {self.max_capacity}\nCurrent Capacity: {self.current_capacity}\nEnrolled Students:\n{student_list}"