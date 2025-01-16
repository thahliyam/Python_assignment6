# Question 1: Build a program to manage a university's course catalog.You want to define a base class
# Course that has the following properties: course_code: a string representing the course code
# (e.g., "CS101") course_name: a string representing the course name (e.g., "Introduction to Computer Science")
# credit_hours: an integer representing the credit hours for the course (e.g., 3) You also want to
# define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.
# CoreCourse should have an additional property required_for_major which is a boolean representing
# whether the course is required for a particular major. ElectiveCourse should have an additional property
# elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display(self):
        print(f"{self.course_code}: {self.course_name} ({self.credit_hours} Credit Hours)")
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display(self):
        super().display()
        status = "Required" if self.required_for_major else "Not Required"
        print(f"- Core Course ({status} for Major)")

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display(self):
        super().display()
        print(f"- Elective Course (Type: {self.elective_type})")

core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("ENG201", "Creative Writing", 2, "Liberal Arts")

core_course.display()
print()
elective_course.display()

from Assignment6 import Employee
emp = Employee("Alice", 50000)
emp.get_name()
emp.get_salary()