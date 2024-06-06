

from courses import course_finder


class Student():
      
    """
    A class used to represent a Student.

    ---------------
    Attributes:
      
    name: str
        name of the student
    
    student_id: int
        student id of the student

    address: str
        student's mailing address
    
    program: str
        program the student is currently enrolled in

    faculty: str
        faculty the student is currently enrolled in

    specialization: str
        specialization the student is currently enrolled in

    standing: int
        student's year standing

    completed_courses: list
        a list of codes of courses the student has taken and passed so far

    grades: list of tuples
        a list of tuples, each containing course_code, percentage grade, and letter grade (F if below 50%)

    registered_courses: list
        a list of codes of courses the student is currently registered in
    
    """
      
    def __init__(self, name, student_id, address, program, faculty, specialization, standing, completed_courses, grades, registered_courses):
          
        self.name = name
        self.student_id = student_id
        self.address = address
        self.program = program
        self.faculty = faculty
        self.specialization = specialization
        self.standing = standing
        self.completed_courses = completed_courses
        self.grades = grades
        self.registered_courses = registered_courses

    def __str__(self):
        return "Student name: {} \nStudent ID: {} \nProgram: {} \nFaculty: {} \nSpecialization: {} \nStanding: {}".format(self.name, self.student_id, self.program, self.faculty, self.specialization, self.standing)
    
    def reg(self, c_code):
        """
        Adds the given course code to student's registered courses list
        """
        self.registered_courses.append(c_code)

    def unenroll(self, c_code):
        """
        Removes the given course code from student's registered courses list
        """
        self.registered_courses.remove(c_code)
    
    def add_grade(self, c_code, perc_grade, letter_grade):
        """
        Adds a new tuple the student's grades list
        """
        self.grades.append((c_code, perc_grade, letter_grade))
    
    def add_completed_course(self, c_code):
        """
        Adds the given course to student's completed courses list
        """
        self.completed_courses.append(c_code)

    def display_grades(self):
        """
        Displays the percentage and letter grade achieved in all courses by the student
        """
        for course, perc_grade, letter_grade in self.grades:
            print(f"{course}: {perc_grade} ({letter_grade})")

    def change_standing(self, year):
        self.standing = year


ubc_students = []
"""
Stores all objects of Student class 
"""

id_pass = {"77305712": "Teddy@2023"}
"""
Stores all student IDs and passwords
"""

def create_student(name, student_id, address, program, faculty, specialization, standing, completed_courses, grades, registered_courses):
     
    """
    returns an object of the Student class with the given attributes and adds the student to the ubc students database
    """

    student = Student(name, student_id, address, program, faculty, specialization, standing, completed_courses, grades, registered_courses)
    ubc_students.append(student)
    return student


def student_finder(std_id):

    """
    if the given student id exists, returns an object of Student class, otherwise returns False
    """

    current_student = False

    for students in ubc_students:
        if students.student_id == std_id:
            current_student = students
            break
    
    return current_student


def assign_grade(current_student, c_code, perc_grade):
    
    letter_grade = ""
    
    if 90 <= perc_grade <= 100:
        letter_grade = "A+"
    
    elif 85 <= perc_grade <= 89:
        letter_grade = "A"

    elif 80 <= perc_grade <= 84:
        letter_grade = "A-"

    elif 76 <= perc_grade <= 79:
        letter_grade = "B+"

    elif 72 <= perc_grade <= 75:
        letter_grade = "B"

    elif 71 <= perc_grade <= 68:
        letter_grade = "B-"

    elif 64 <= perc_grade <= 67:
        letter_grade = "C+"

    elif 60 <= perc_grade <= 63:
        letter_grade = "C"

    elif 55 <= perc_grade <= 59:
        letter_grade = "C-"
    
    elif 50 <= perc_grade <= 54:
        letter_grade = "D"
    
    else:
        letter_grade = "F"
    
    current_student.add_grade(c_code, perc_grade, letter_grade)


pari_courses = ["MATH100", "PHYS131", "SCIE113", "COMR100", "ECON102", "MATH101", "CPSC110", "ECON101"]
pari_grades = [("MATH100", 82, "A-"), ("PHYS131", 99, "A+"), ("SCIE113", 91, "A+"), ("COMR100", 94, "A+"), ("ECON102", 94, "A+"), ("MATH101", 91, "A+"), ("CPSC110", 96, "A+"), ("ECON101", 91, "A+"), ("ECON321", 49, "F")]
create_student("Pari Khanna", 77305712, "Abbotsford, B.C.", "B.SC", "Science", "CPSC", 2, pari_courses, pari_grades, ["CPSC121"])

keshav_courses = pari_courses + ["CPSC210", "CPSC213", "CPSC221", "STAT200", "MATH200", "DSCI100", "WRDS150", "LING100"]
keshav_grades = pari_grades + [("CPSC210", 80, "A-"), ("CPSC213", 75, "B"), ("CPSC221", 40, "F"), ("STAT200", 90, "A+"), ("MATH200", 65, "C+"), ("DSCI100", 95, "A+"), ("WRDS150", 99, "A+"), ("LING100", 97, "A+")] 
create_student("Keshav Dubay", 23706032, "Vancouver, B.C.", "B.SC", "Science", "CPSC", 2, keshav_courses, keshav_grades, [])

myra_courses = pari_courses + keshav_courses + ["CHEM121", "ENGL110", "BIOL111", "ASTR102", "SCIE300"]
myra_grades = pari_grades + keshav_grades + [("CHEM121", 90, "A+"), ("ENGL110", 90, "A+"), ("BIOL111", 90, "A+"), ("ASTR102", 90, "A+"), ("SCIE300", 90, "A+")]
create_student("Myra", 11223344, "Vancouver, B.C.", "B.SC", "Science", "CPSC", 3, myra_courses, myra_grades, [] )
