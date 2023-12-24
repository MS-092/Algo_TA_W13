class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []
        self.selected_course = None  # Property to track the selected course

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)
        self.selected_course = course

    def display_student_info(self):
        course_list = "\n".join([f"{c.code}: {c.title}" for c in self.courses_enrolled])
        return f"Student ID: {self.student_id}\nName: {self.name}\nCourses Enrolled:\n{course_list}\nSelected Course: {self.selected_course.title if self.selected_course else 'None'}"