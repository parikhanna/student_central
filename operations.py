

from courses import course_finder

from datetime import datetime

def end_session_display():

    """
    Asks user if they would like to end the session and returns a boolean value.
    """

    end_session = ""
    acceptable_options = ["Y", "N"]

    while end_session not in acceptable_options:
        end_session = input("End Session (Y or N)? ")

        if end_session not in acceptable_options:
            print("Error: Invalid Option")
    
    if end_session == "Y":
        return True
    else:
        return False


def course_code_display():

    """
    Asks the user for the course code they would like ti register or unenroll and returns an object of Course class associated with the given course code.
    """

    c_code = ""

    while course_finder(c_code) == False:
        c_code = input("Enter the course code: ")

        if course_finder(c_code) == False:
            print("Error: Invalid Course Code")
    
    return course_finder(c_code)


def specialization_check(current_student, current_course):

    """
    Checks if the student can be alotted a restricted seat for the given course.
    """

    return current_student.specialization in current_course.course_specialization
     

def prerequisites_check(current_student, current_course):

    """
    Checks if the student fulfills the pre-requisites for the given course.
    """

    status = True

    for courses in current_course.pre_requisites:
            if courses not in current_student.completed_courses:
                status = False
    
    return status


def corequisites_check(current_student, current_course):

    """
    Checks if the student fulfills the co-requisites for the given course. If not, prints a message telling the student what co-requisites they must enroll in.
    """
     
    combined_list = current_student.registered_courses + current_student.completed_courses
    missing_courses = []

    for courses in current_course.co_requisites:
        if courses not in combined_list:
            missing_courses.append(courses)
    
    if missing_courses != []:
        print(f"Please ensure to register in the following co_requisites - {missing_courses}")


def course_reg(current_student, current_course):

    """
    Registers the student in the given course if seats are available and all requirements are met.
    """

    if current_course.course_code in current_student.registered_courses:
        print("Student already registered in the course.")

    elif not current_course.res_seats_check() and not current_course.gen_seats_check():
        print("No seats available in the course.") 

    elif not prerequisites_check(current_student, current_course):
        print("You do not meet the prerequisites for this course.")
            
    else:
            
        if specialization_check(current_student, current_course) and current_course.res_seats_check(): 
            current_student.reg(current_course.course_code)
            current_course.special_reg()
            print("Course succesfully registered!")
            corequisites_check(current_student, current_course)
            
        elif current_course.gen_seats_check():
            current_student.reg(current_course.course_code)
            current_course.general_reg()
            print("Course succesfully registered!")
            corequisites_check(current_student, current_course)

        else:
            print("Only restricted seats available in the course.")


def course_unenroll(current_student, current_course):

    """
    Unenrolls the student from the given course.
    """
    
    if current_course.course_code not in current_student.registered_courses:
        print("The student is not currently enrolled in the course.")
    
    else:
        current_student.unenroll(current_course.course_code)  
        print("Course Succesfully Dropped!")


def total_credits(current_student):

    """
    Calculates the total credits earned by the given student (failed courses are not included).
    """

    credit_counter = 0 

    for course in current_student.completed_courses:
        credit_counter += course_finder(course).course_credits
    
    return credit_counter


def science_credits(current_student):

    """
    Calculates total science credits earned by the given student (failed courses are not included).
    """

    credit_counter = 0 

    for course in current_student.completed_courses:
        if course_finder(course).course_faculty == "Science":
            credit_counter += course_finder(course).course_credits
    
    return credit_counter


def attempted_credits(current_student):

    """
    Calculates total attempted credits by the given student (failed courses are included).
    """

    credit_counter = 0 

    for course, perc, letter in current_student.grades:
        credit_counter += course_finder(course).course_credits
    
    return credit_counter


def specialization_avg(current_student):

    """
    Calculates avg of 3/5 of credits for the second-year named courses in the student's specialization (rounded up to nearest whole course)
    """

    std_specialization = current_student.specialization

    attempted_courses_list = current_student.grades

    credit_counter = 0 
    course_counter = 0 
    grade_calculator = 0 

    
    y2_specialization_courses = list(filter((lambda x: x[0][4] == "2" and std_specialization in course_finder(x[0]).course_specialization), attempted_courses_list))
    y2_specialization_courses.sort(key = lambda x: x[1], reverse = True)
    print(y2_specialization_courses)

    req_credits = 3 / 5 * (sum(list(map(lambda x: course_finder(x[0]).course_credits, y2_specialization_courses))))


    for course,perc,letter in y2_specialization_courses:
            
        if credit_counter < req_credits:
            grade_calculator += perc
            course_counter += 1
            credit_counter += course_finder(course).course_credits

    average = grade_calculator / course_counter

    return average


def lab_req(current_student):

    """
    Returns True if the student has met the lab requirements (taken one of the given lab courses).
    """

    lab_courses = ["ASTR101", "ASTR102", "BIOL140", "CHEM111", "CHEM115", "CHEM121", "CHEM123", "CHEM135", "EOSC111", "PHYS101", "PHYS107", "PHYS109", "PHYS119", "PHYS159", "SCIE001"]

    for course in current_student.completed_courses:
        if course in lab_courses:
            return True
        
    return False


def communication_req(current_student):

    """
    Returns True if student has met the communication requirements (taken SCIE113 and three other courses from the provided list).
    """

    course_counter = 0
    communication_courses = ["WRDS150", "ENGL100", "ENGL110", "ENGL111", "SCIE300", "CHEM300", "APSC176", "LFS176", "FRST150", "ASTU100", "ASTU101"] 

    for course in current_student.completed_courses:
        if course in communication_courses:
            course_counter += 1
    
    req_met = (course_counter == 3) and ("SCIE113" in current_student.completed_courses)

    return req_met


def breadth_req(current_student):

    """
    Returns true if the given student has taken courses in 6 out of the 7 science breadth categories.
    """

    math = False
    chemistry = False
    physics = False
    life_science = False
    statistics = False
    computer_science = False
    earth_planetary_science = False
    counter = 0 

    for course in current_student.completed_courses:

        c_specialization = course_finder(course).course_specialization

        if "MATH" in c_specialization:
            math = True
            counter += 1
        elif "CHEM" in c_specialization:
            chemistry = True
            counter += 1
        elif "PHYS" in c_specialization:
            physics = True
            counter += 1
        elif "LSCI" in c_specialization:
            life_science = True
            counter += 1
        elif "STAT" in c_specialization:
            statistics = True
            counter += 1
        elif "CPSC" in c_specialization:
            computer_science = True
            counter += 1
        elif "EOSC" in c_specialization:
            earth_planetary_science = True
            counter += 1

    if counter >= 6:
        return True
    else:
        return False


def sci_y4_req(current_student):

    """
    Returns True if the given student meets requirements for promotion to year 4 in the Faculty of Science.

    Requirements:
    - 72 or more credits
    - 50 or more science credits
    - Must meet Lab requirements
    - Must meet communication requirements
    - Must meet breadth requirements 
    - Requirements must be met within 108 attempted credits. 
    """

    return total_credits(current_student) >= 72 and science_credits(current_student) >= 50 and attempted_credits(current_student) <= 180 and lab_req(current_student) and communication_req(current_student) and breadth_req(current_student)


def sci_y3_req(current_student):

    """
    Returns True if the given student meets requirements for promotion to year 3 in the Faculty of Science.

    Requirements:
    - 48 or more credits 
    - An avg of at least 60% in 3/5 of credits for the second-year named courses in the student's specialization
    - Requirements must be met within 78 attempted credits after admission to first year.
    """

    return total_credits(current_student) >= 48 and science_credits(current_student) >= 15 and attempted_credits(current_student) <= 78 and specialization_avg(current_student) >= 60


def sci_y2_req(current_student):

    """
    Returns True if the given student meets requirements for promotion to year 2 in the Faculty of Science.

    Requirements:
    - 24 or more credits
    - 15 science credits 
    - Requirements must be met within 48 attempted credits after admission to first year.
    """

    return total_credits(current_student)>= 24 and science_credits(current_student) >= 15 and attempted_credits(current_student) <= 48


def change_science_standing(current_student):

    """
    Changes a Science student's year standing if requirements are met. 
    """

    if current_student.standing < 4 and sci_y4_req(current_student):
        current_student.change_standing(4)

    elif current_student.standing < 3 and sci_y3_req(current_student):
        current_student.change_standing(3)

    elif current_student.standing < 2 and sci_y2_req(current_student):
        current_student.change_standing(2)
    
    else:
        print("Error: Student not eligible for promotion")
    

def change_year_standing(current_student):

    """
    Changes the given student's year standing based on their faculty if requirements are met.
    """

    faculty = current_student.faculty

    if faculty == "Science":
        change_science_standing(current_student)


def open_terms(current_student):

    """
    Returns a list of terms that registration is open for.
    """

    student_standing = current_student.standing

    open_terms = []

    current_date = datetime.now()
    current_year = current_date.year

    w_term_reg_start_date = 0
    s_term_reg_start_date = 0
    w_term1_reg_end_date = datetime(current_year, 9, 16, 23, 59, 59)
    w_term2_reg_end_date = datetime(current_year, 1, 17, 23, 59, 59)
    s_term1_reg_end_date = datetime(current_year, 6, 7, 23, 59, 59)
    s_term2_reg_end_date = datetime(current_year, 7, 5, 23, 59, 59)
        

    if student_standing == 1:
        w_term_reg_start_date = datetime(current_year, 6, 24)
        s_term_reg_start_date = datetime(current_year, 2, 29)
    elif student_standing == 2:
        w_term_reg_start_date = datetime(current_year, 7, 8)
        s_term_reg_start_date = datetime(current_year, 2, 28)
    elif student_standing == 3:
        w_term_reg_start_date = datetime(current_year, 7, 2)
        s_term_reg_start_date = datetime(current_year, 2, 27)
    else:
        w_term_reg_start_date = datetime(current_year, 6, 10)
        s_term_reg_start_date = datetime(current_year, 2, 26)


    if w_term_reg_start_date <= current_date:

        if current_date <= w_term1_reg_end_date:
            open_terms.append("{} Winter Term 1".format(current_year))
        
        if current_date <= w_term2_reg_end_date:
            open_terms.append("{} Winter Term 2".format(current_year))

    if s_term_reg_start_date <= current_date:
        
        if current_date <= s_term1_reg_end_date:
            open_terms.append("{} Summer Term 1".format(current_year))
            
        if current_date <= s_term2_reg_end_date:
            open_terms.append("{} Summer Term 2".format(current_year))

    
    return open_terms




# TESTING:

from students import student_finder

print(total_credits(student_finder(77305712)))
print(science_credits(student_finder(77305712)))
print(attempted_credits(student_finder(77305712)))
print(sci_y2_req(student_finder(77305712)))

print(total_credits(student_finder(23706032)))
print(science_credits(student_finder(23706032)))
print(attempted_credits(student_finder(23706032)))
print(specialization_avg(student_finder(23706032)))
print(sci_y3_req(student_finder(23706032)))

print(lab_req(student_finder(23706032)))
print(communication_req(student_finder(77305712)))
print(breadth_req(student_finder(77305712)))

print(lab_req(student_finder(11223344)))
print(communication_req(student_finder(11223344)))
print(breadth_req(student_finder(11223344)))
print(total_credits(student_finder(11223344)))
print(attempted_credits(student_finder(11223344)))
print(science_credits(student_finder(11223344)))
print(sci_y4_req(student_finder(11223344)))

change_year_standing(student_finder(77305712))
change_year_standing(student_finder(23706032))
change_year_standing(student_finder(11223344))

print(student_finder(77305712))
print(student_finder(23706032))
print(student_finder(11223344))

print(open_terms(student_finder(77305712)))
print(open_terms(student_finder(23706032)))
print(open_terms(student_finder(11223344)))


