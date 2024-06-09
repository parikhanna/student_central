

from operations import calculate_credits

from datetime import datetime


class Student():
      
    """
    A class used to represent a Student

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

    student_course_db: list of objects of StudentCourse class
        a database list consisting of all the courses student has taken (including failed and withdrawn courses) and/or is registered in

    registered_courses = list of objects of StudentCourse class
        list of courses that student is currently registered in but has not finished yet

    attempted_courses = list of objects of StudentCourse class
        list of courses student has attempted (including failed and withdrawn courses)

    completed_courses = list of objects of StudentCourse class
        list of courses student has successfully completed (passed)
    
    """

    def __init__(self, name, student_id, address, program, faculty, specialization, standing, student_course_db):
          
        self.name = name
        self.student_id = student_id
        self.address = address
        self.program = program
        self.faculty = faculty
        self.specialization = specialization
        self.standing = standing
        self.student_course_db = student_course_db
        self.registered_courses = list(filter((lambda x: x.registered()),student_course_db))
        self.attempted_courses = list(filter((lambda x: x.attempted()),student_course_db))
        self.completed_courses = list(filter((lambda x: x.completed()),student_course_db))
        self.completed_faculty_courses = list(filter((lambda x: x.course_faculty == self.faculty),self.completed_courses))
        self.completed_specialization_courses = list(filter((lambda x: self.specialization in x.course_specialization),self.completed_courses))


    def __str__(self):
        return "Student name: {} \nStudent ID: {} \nProgram: {} \nFaculty: {} \nSpecialization: {} \nStanding: {}".format(self.name, self.student_id, self.program, self.faculty, self.specialization, self.standing)
    

    def term_courses(self, term, year):
        """
        Returns a list of courses taken by the student in the given term and year
        """
        term_course_list = list(filter((lambda x: x.year == year and x.term == term),self.student_course_db))
        return term_course_list
    

    def completed_courses_code(self) :
        return list(map((lambda x: x.course_code),self.completed_courses))


    def register(self, student_course):
        """
        Adds the given course code to student's course database
        """
        self.student_course_db.append(student_course)


    def unenroll_without_w(self, student_course):
        """
        Removes the given course code from student's course database
        """
        self.student_course_db.remove(student_course)
    

    def unenroll_with_w(self, student_course_index):
        """
        Adds a withdrawn grade ("W") to the given course in the student's course database
        """
        self.student_course_db[student_course_index].letter_grade == "W" 

    
    def student_course_finder(self, c_code):

        """
        Looks for the given course in the student's course database and returns an object of StudentCourse class if course is found, else return False
        """

        current_course = False
        
        for courses in self.student_course_db:
            if courses.course_code == c_code:
                current_course = courses
                break
        
        return current_course


    def add_grade(self, student_course_index, perc_grade):
        """
        Adds the given percentage grade and a letter grade to the given course in student's course databse 
        """

        letter_grade = give_letter_grade(perc_grade)

        self.student_course_db[student_course_index].percentage_grade = perc_grade
        self.student_course_db[student_course_index].letter_grade = letter_grade


    def calculate_term_avg(self,term_course_list):
        """
        Calculates weighted avg for the courses taken in the given term
        """

        course_credits_list = list(map((lambda x: x.course_credit),term_course_list))
        course_perc_list = list(map((lambda x: x.perc_grade),term_course_list))
        combined_list = list(zip(course_credits_list, course_perc_list))

        total_credits = sum(course_credits_list)

        average = 0

        for credits, perc_grade in combined_list:
            average += (credits * 100 / total_credits) * perc_grade

        return average
    

    def display_grades(self, term_course_list):
        """
        Displays the percentage grade, letter grade, and credits achieved for each course taken by the student        
        """

        for courses in term_course_list:
            courses.display_grade()


    def display_timetable(self, term_course_list):
        """
        Displays the student's timetable for the given term        
        """
        for courses in term_course_list:
            courses.display_timetable()

    

    def reg_start_date(self):

        """
        Returns the fall, winter and summer registration start dates for the student
        """

        student_standing = self.standing

        current_date = datetime.now()
        current_year = current_date.year
        w_and_f_reg_start_date = 0
        s1_and_s2_reg_start_date = 0


        if student_standing == 1:
            w_and_f_reg_start_date = datetime(current_year, 6, 24)
            s1_and_s2_reg_start_date = datetime(current_year, 2, 29)
        elif student_standing == 2:
            w_and_f_reg_start_date = datetime(current_year, 7, 8)
            s1_and_s2_reg_start_date = datetime(current_year, 2, 28)
        elif student_standing == 3:
            w_and_f_reg_start_date = datetime(current_year, 7, 2)
            s1_and_s2_reg_start_date = datetime(current_year, 2, 27)
        else:
            w_and_f_reg_start_date = datetime(current_year, 6, 10)
            s1_and_s2_reg_start_date = datetime(current_year, 2, 26)

        return (w_and_f_reg_start_date, s1_and_s2_reg_start_date)


    def open_terms(self):

        """
        Returns a list of terms that registration is open for
        """

        open_terms = []

        current_date = datetime.now()
        current_year = current_date.year

        reg_start_date = self.reg_start_date()

        w_and_f_reg_start_date = reg_start_date[0]
        s1_and_s2_reg_start_date = reg_start_date[1]
        f_reg_end_date = datetime(current_year, 9, 16, 23, 59, 59)
        w_reg_end_date = datetime(current_year, 1, 17, 23, 59, 59)
        s1_reg_end_date = datetime(current_year, 6, 7, 23, 59, 59)
        s2_reg_end_date = datetime(current_year, 7, 5, 23, 59, 59)
            

        
        if w_and_f_reg_start_date <= current_date:

            if current_date <= f_reg_end_date:
                open_terms.append("{} Winter Term 1".format(current_year))
            
            if current_date <= w_reg_end_date:
                open_terms.append("{} Winter Term 2".format(current_year))

        if s1_and_s2_reg_start_date <= current_date:
            
            if current_date <= s1_reg_end_date:
                open_terms.append("{} Summer Term 1".format(current_year))
                
            if current_date <= s2_reg_end_date:
                open_terms.append("{} Summer Term 2".format(current_year))

        
        return open_terms


    def change_standing(self, standing_year):
        self.standing = standing_year

    
    ## SCIENCE STUDENT SPECIFIC METHODS:
    ## (IDEALLY IT WOULD MAKE SENSE TO HAVE SUB CLASSES FOR STUDENTS FROM DIFFERENT FACULTIES AS DIFFERENT KINDS OF OPERATIONS ARE NEEDED.)


    def communication_req(self, completed_courses_code):
        """
        Returns True if student has met the communication requirements (taken SCIE113 and three other courses from the provided list)
        """

        communication_courses = ["WRDS150", "ENGL100", "ENGL110", "ENGL111", "SCIE300", "CHEM300", "APSC176", "LFS176", "FRST150", "ASTU100", "ASTU101"] 
        communication_courses_counter = len(list(filter((lambda x: x in communication_courses), completed_courses_code)))
        
        req_met = (communication_courses_counter == 3) and ("SCIE113" in completed_courses_code)

        return req_met
    

    def lab_req(self, completed_courses_code):
        """
        Returns True if student has met the lab requirements (taken one of the courses from the provided list)
        """
        
        lab_courses = ["ASTR101", "ASTR102", "BIOL140", "CHEM111", "CHEM115", "CHEM121", "CHEM123", "CHEM135", "EOSC111", "PHYS101", "PHYS107", "PHYS109", "PHYS119", "PHYS159", "SCIE001"]
        
        for courses in lab_courses:
            if courses in completed_courses_code:
                return True
        return False


    def breadth_req(self):

        """
        Returns true if the student has taken courses in 6 out of the 7 science breadth categories
        """

        counter = 0 

        for course in self.completed_courses:

            c_specialization = course.course_specialization

            if "MATH" in c_specialization or "CHEM" in c_specialization or "PHYS" in c_specialization or "LSCI" in c_specialization or "STAT" in c_specialization or "CPSC" in c_specialization or "EOSC" in c_specialization:
                counter += 1

        if counter >= 6:
            return True
        else:
            return False
        
    
    def specialization_avg(self): 

        """
        Calculates avg of 3/5 of credits for the second-year named courses in the student's specialization (rounded up to nearest whole course)
        """

        credit_counter = 0 
        course_counter = 0 
        grade_calculator = 0 

        y2_specialization_courses = list(filter((lambda x: x.course_code[4] == "2", self.completed_specialization_courses)))
        y2_specialization_courses.sort(key = lambda x: x.percentage_grade, reverse = True)

        req_credits = 3 / 5 * (sum(list(map(lambda x: x.course_credits, y2_specialization_courses))))

        for courses in y2_specialization_courses:
                
            if credit_counter < req_credits:
                grade_calculator += courses.percentage_grade
                course_counter += 1
                credit_counter += courses.course_credits

        average = grade_calculator / course_counter

        return average

        
    def sci_y4_req(self):

        """
        Returns True if the student meets requirements for promotion to year 4 in the Faculty of Science

        Requirements:
        - 72 or more credits
        - 50 or more science credits
        - Must meet Lab requirements
        - Must meet communication requirements
        - Must meet breadth requirements 
        - Requirements must be met within 108 attempted credits. 
        """

        completed_courses_code = self.completed_courses_code()

        return calculate_credits(self.completed_courses) >= 72 and calculate_credits(self.completed_faculty_courses) >= 50 and calculate_credits(self.attempted_courses) <= 180 and self.lab_req(completed_courses_code) and self.communication_req(completed_courses_code) and self.breadth_req()


    def sci_y3_req(self):

        """
        Returns True if the student meets requirements for promotion to year 3 in the Faculty of Science

        Requirements:
        - 48 or more credits 
        - An avg of at least 60% in 3/5 of credits for the second-year named courses in the student's specialization
        - Requirements must be met within 78 attempted credits after admission to first year
        """

        return calculate_credits(self.completed_courses) >= 48 and calculate_credits(self.completed_faculty_courses) >= 15 and calculate_credits(self.attempted_courses) <= 78 and self.specialization_avg >= 60


    def sci_y2_req(self):

        """
        Returns True if the student meets requirements for promotion to year 2 in the Faculty of Science

        Requirements:
        - 24 or more credits
        - 15 science credits 
        - Requirements must be met within 48 attempted credits after admission to first year
        """

        return calculate_credits(self.completed_courses) >= 24 and calculate_credits(self.completed_faculty_courses) >= 15 and calculate_credits(self.attempted_courses) <= 48
    

    def change_science_standing(self):

        """
        Changes a Science student's year standing if requirements are met
        """

        if self.standing < 4 and self.sci_y4_req():
            self.change_standing(4)

        elif self.standing < 3 and self.sci_y3_req():
            self.change_standing(3)

        elif self.standing < 2 and self.sci_y2_req():
            self.change_standing(2)
        
        else:
            print("Error: Student not eligible for promotion")


ubc_students = []
"""
Stores all objects of Student class 
"""


id_pass = {"77305712": "Teddy@2023"}
"""
Stores all student IDs and passwords
"""


def create_student(name, student_id, address, program, faculty, specialization, standing, student_course_db):
    """
    returns an object of the Student class with the given attributes and adds the student to the ubc students database
    """

    student = Student(name, student_id, address, program, faculty, specialization, standing, student_course_db)
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


def give_letter_grade(perc_grade):

    """
    Returns the letter grade category the given perc_grade falls under
    """
    
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
    
    return letter_grade




# pari_course = ["MATH100", "PHYS131", "SCIE113", "COMR100", "ECON102", "MATH101", "CPSC110", "ECON101"]
# pari_course_db = [("MATH100", 82, "A-"), ("PHYS131", 99, "A+"), ("SCIE113", 91, "A+"), ("COMR100", 94, "A+"), ("ECON102", 94, "A+"), ("MATH101", 91, "A+"), ("CPSC110", 96, "A+"), ("ECON101", 91, "A+"), ("ECON321", 49, "F")]
# create_student("Pari Khanna", 77305712, "Abbotsford, B.C.", "B.SC", "Science", "CPSC", 2, pari_course_db)

# keshav_courses = pari_courses + ["CPSC210", "CPSC213", "CPSC221", "STAT200", "MATH200", "DSCI100", "WRDS150", "LING100"]
# keshav_grades = pari_grades + [("CPSC210", 80, "A-"), ("CPSC213", 75, "B"), ("CPSC221", 40, "F"), ("STAT200", 90, "A+"), ("MATH200", 65, "C+"), ("DSCI100", 95, "A+"), ("WRDS150", 99, "A+"), ("LING100", 97, "A+")] 
# create_student("Keshav Dubay", 23706032, "Vancouver, B.C.", "B.SC", "Science", "CPSC", 2, keshav_courses, keshav_grades, [])

# myra_courses = pari_courses + keshav_courses + ["CHEM121", "ENGL110", "BIOL111", "ASTR102", "SCIE300"]
# myra_grades = pari_grades + keshav_grades + [("CHEM121", 90, "A+"), ("ENGL110", 90, "A+"), ("BIOL111", 90, "A+"), ("ASTR102", 90, "A+"), ("SCIE300", 90, "A+")]
# create_student("Myra", 11223344, "Vancouver, B.C.", "B.SC", "Science", "CPSC", 3, myra_courses, myra_grades, [] )
