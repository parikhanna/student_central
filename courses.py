

# ---------------------------------
# CLASSES:

class Course():
     
    """
    A class used to represent a Course

    ----------------
    Attributes:

    name: str
        name of the course
        
    course_code: str
        special code assigend to the course

    pre_requisistes: str
        codes of courses that are pre-requisites for the course
    
    co_requisistes: str
        codes of courses that are co-requisites for the course

    general_seats: int
        number of general seats remaining in the course

    restricted_seats: int
        number of restricted seats remaining in the course

    course_credits: int
        amount of credits received upon completion of the course 

    course_faculty: str
        faculty that offers the course

    course_specialization: list
        list of specializations for which the restricted seats are reserved 

    """
      
    def __init__(self, name, course_code, pre_requisites, co_requisites, general_seats, restricted_seats, course_credits, course_faculty, course_specialization):
           
        self.name = name
        self.course_code = course_code
        self.pre_requisites = pre_requisites
        self.co_requisites = co_requisites
        self.general_seats = general_seats
        self.restricted_seats = restricted_seats
        self.course_credits = course_credits
        self.course_faculty = course_faculty
        self.course_specialization = course_specialization
           

    def __str__(self):
        return "Course name: {} \nCredits: {} \nPrerequisites: {} \nCorequisites: {} \nGeneral seats: {} \nRestricted seats: {} \nCourse specialization: {}".format(self.name, self.course_credits, self.pre_requisites, self.co_requisites, self.general_seats, self.restricted_seats, self.course_specialization)
    

    def res_seats_check(self):
        """ 
        Checks if there are any restricted seats available in the course
        """
        return self.restricted_seats > 0
    

    def gen_seats_check(self):
        """
        Checks if there are any general seats available in the course
        """
        return self.general_seats > 0
    

    def special_reg(self):
        """
        Registers a student into the course and decreases the number of restricted seats left
        """
        self.restricted_seats -= 1
    

    def general_reg(self):
        """
        Registers a student into the course and decreases the number of general seats left
        """
        self.general_seats -= 1


class StudentCourse(Course):

    """
    A subclass of Course class with additional course information specific to a student

    An instance is only created when a student successfully registers in the course

    --------------
    Additional Attributes:

    term: str
        term the student took the course in
    year: int
        year the student took the course in
    percentage_grade = int
        percentage grade the student got in the course
    letter_grade = string
        letter grade the student got in the course
        
    """

    def __init__(self, name, course_code, pre_requisites, co_requisites, general_seats, restricted_seats, course_credits, course_faculty, course_specialization, term, year, percentage_grade, letter_grade):

        Course.__init__(self, name, course_code, pre_requisites, co_requisites, general_seats, restricted_seats, course_credits, course_faculty, course_specialization)
        
        self.term = term
        self.year = year
        self.percentage_grade = percentage_grade
        self.letter_grade = letter_grade

        print("Course Successfully Registered")


    def completed(self):
        """
        Returns true if the student has successfully passed the course
        """
        return self.percentage_grade != "" and self.letter_grade != "F"
    

    def registered(self):
        """
        Returns true if the student is registered in the course for the current or an upcoming term
        """
        return self.letter_grade == ""
    

    def attempted(self):
        """
        Returns true is the student has ever attempted the course (includes failed and withdrawn courses ; doesn't include registered courses)
        """
        return self.letter_grade != "" 
    

    def display_grade(self):
        print(f"Course: {self.course_code} \nPercentage Grade: {self.percentage_grade} \nLetter Grade: {self.letter_grade} \nCredits: {self.course_credits} \n")


    def display_timetable(self):
        print(f"Course: {self.course_code} Credits: {self.course_credits} \n")
 

# ---------------------------------
# DATABASE:

ubc_courses = []
"""
Stores all objects of Course class 
"""


# ---------------------------------
# FUNCTIONS:

def create_course(name, course_code, pre_requisites, co_requisites, general_seats, restricted_seats, course_credits, course_faculty, course_specialization):

    """
    Returns an object of the Course class with the given attributes and adds the course to the ubc courses database
    """

    course = Course(name, course_code, pre_requisites, co_requisites, general_seats, restricted_seats, course_credits, course_faculty, course_specialization)
    ubc_courses.append(course)
    return course


def create_student_course (current_course, current_student, term, year, percentage_grade = "", letter_grade = ""):

    """
    Returns an object of the StudentCourse class with the given attributes nd adds it to the given student's course database
        percentage_grade and letter_grade are set to "" by default
    """

    course = StudentCourse(current_course.name, current_course.course_code, current_course.pre_requisites, current_course.co_requisites, current_course.general_seats, current_course.restricted_seats, current_course.course_credits, current_course.course_faculty, current_course.course_specialization, term, year, percentage_grade, letter_grade)
    current_student.register(course)
    return course


def course_finder(c_code):

    """
    If the given course code exists, returns an object of Code class, otherwise returns False
    """

    current_course = False

    for courses in ubc_courses:
        if courses.course_code == c_code:
            current_course = courses
            break
    
    return current_course


# ---------------------------------
# TESTING:

# Creating courses and adding them to the UBC course db:

create_course("Systematic Program Design", "CPSC110", [], [], 100, 30, 4, "Science", ["CPSC", "BUCS"])
create_course("Software Construction", "CPSC210", ["MATH100"], ["CPSC121"], 100, 100, 4, "Science", ["BUCS", "CPSC"])
create_course("Differential Calculus", "MATH100", [], [], 500, 0, 3, "Science", ["MATH"])
create_course("Integral Calculus", "MATH101", ["MATH100"], ["STAT100"], 500, 0, 3, "Science", ["MATH"])
create_course("Introduction to Microeconomics", "ECON101", [], [], 0, 0, 3, "Arts", ["ECON", "BUCS"])
create_course("Introduction to Macroeconomics", "ECON102", [], [], 0, 10, 3, "Arts", ["ECON", "BUCS"])
create_course("Discrete Mathematics", "CPSC121", ["CPSC110, MATH100"], ["MATH101"], 100, 100, 4, "Science", ["CPSC", "MATH", "BUCS", "STAT"])
create_course("Energy and Waves", "PHYS131", [], [], 100, 0, 3, "Science", ["PHYS"])
create_course("First Year Seminar in Science", "SCIE113", [], [], 200, 100, 3, "Science", [])
create_course("Introduction to Business", "COMR100", [], [], 300, 0, 3, "Sauder", [])
create_course("This is a random course", "PREQ100", ["POLI100", "APSC100", "ARTS200"], [], 100, 200, 4, "Arts", [])
create_course("International Economics", "ECON321", ["ECON101", "ECON102", "MATH101"], [], 0, 0, 4, "Arts", ["ECON"])
create_course("Introduction to Computer System", "CPSC213", ["CPSC110", "CPSC121", "MATH100", "MATH101"], ["CPSC210"], 200, 30, 4, "Science", ["CPSC", "BUCS"])
create_course("Basic Algorithms and Data Structures", "CPSC221", ["CPSC110", "CPSC121", "MATH100", "MATH101"], ["CPSC210"], 200, 30, 4, "Science", ["CPSC", "BUCS"])
create_course("Elementary Statistics for Application", "STAT200", ["MATH100", "MATH101"], [], 100, 20, 3, "Science", ["STAT", "MATH", "CPSC", "BUCS"])
create_course("Calculus 3", "MATH200", ["MATH100", "MATH101"], [], 200, 30, 3, "Science", ["MATH", "STAT"])
create_course("Introduction to Data Science", "DSCI100", [], [], 100, 0, 3, "Science", ["STAT"])
create_course("Writing Studies", "WRDS150", [], [], 300, 0, 3, "Science", [])
create_course("Introduction to Linguistics", "LING100", [], [], 500, 0, 3, "Arts", [])
create_course("Structural Chemistry", "CHEM121", [], ["MATH100"], 300, 0, 3, "Science", ["CHEM"])
create_course("Approaches to Literature and Culture", "ENGL110", [], [], 300, 100, 3, "Arts", ["LITS"])
create_course("Introduction to Biology", "BIOL111", [], [], 300, 0, 3, "Science", ["LSCI"])
create_course("Introduction to Stars and Galaxies", "ASTR102", [], [], 300, 0, 3, "Science", ["EOSC"])
create_course("Communicating Science", "SCIE300", ["SCIE113"], [], 300, 0, 3, "Science", [])