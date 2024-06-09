

from courses import course_finder, create_student_course


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
     

def prerequisites_check(current_student, current_course, term, year):

    """
    Returns True if student meets prerequisites for course, else returns False.
    """

    status = True
    terms_to_check = []

    for courses in current_course.pre_requisites:

        student_course = current_student.student_course_finder(courses)

        if student_course != False:

            if term == "Fall":
                terms_to_check = [("S1", year), ("S2", year)]
            elif term == "Winter":
                terms_to_check = [("S1", year), ("S2", year), ("Fall", (year + 1))]
            elif term == "S1":
                terms_to_check = [("Winter", year)]
            else:
                terms_to_check = [("Winter", year), ("S1", year)]


            if student_course.completed() or (student_course.registered() and (student_course.term, student_course.year) in terms_to_check):
                pass 

            return False

        return False
    
    return status
    

def corequisites_check(current_student, current_course, term, year):

    """
    Checks if the student fulfills the co-requisites for the given course. If not, prints a message telling the student what co-requisites they must enroll in.
    """

    missing_courses = []
    terms_to_check = []

    for courses in current_course.co_requisites:

        student_course = current_student.student_course_finder(courses)

        if student_course != False:

            if term == "Fall":
                terms_to_check = [("S1", year), ("S2", year), (term, year)]
            elif term == "Winter":
                terms_to_check = [("S1", year), ("S2", year), ("Fall", (year + 1)), (term, year)]
            elif term == "S1":
                terms_to_check = [("Winter", year), (term, year)]
            else:
                terms_to_check = [("Winter", year), ("S1", year), (term, year)]


            if student_course.completed() or (student_course.registered() and (student_course.term, student_course.year) in terms_to_check):
                pass 

            missing_courses.append(courses)

        missing_courses.append(courses)
    
    if missing_courses != []:
        print(f"Must enrol in the following co-requisites: {missing_courses}")
    else:
        return True
    

def course_reg(current_student, current_course, term, year):

    """
    Registers student in course for specified term and year by creating a StudentCourse object in the student's database, if seats are available and requirements are met.
    """

    student_course = current_student.student_course_finder(current_course.course_code)

    if student_course != False and student_course.term == term and student_course.year == year:
        print("Student already registered in the course.")

    elif not current_course.res_seats_check() and not current_course.gen_seats_check():
        print("No seats available in the course.") 

    elif not prerequisites_check(current_student, current_course, term, year): 
        print("You do not meet the prerequisites for this course.")
            
    else:
            
        if specialization_check(current_student, current_course) and current_course.res_seats_check(): 
            create_student_course(current_course, current_student, term, year)
            current_course.special_reg()
            print("Course succesfully registered!")
            corequisites_check(current_student, current_course, term, year)
            
        elif current_course.gen_seats_check():
            create_student_course(current_course, current_student, term, year)
            current_course.general_reg()
            print("Course succesfully registered!")
            corequisites_check(current_student, current_course, term, year)

        else:
            print("Only restricted seats available in the course.")


def calculate_credits(list):
    """
    Calculates total credits from the provided course list
    """
    return sum(list(map((lambda x: x.course_credit),list)))




# TESTING:

# from students import student_finder

# print(total_credits(student_finder(77305712)))
# print(science_credits(student_finder(77305712)))
# print(attempted_credits(student_finder(77305712)))
# print(sci_y2_req(student_finder(77305712)))

# print(total_credits(student_finder(23706032)))
# print(science_credits(student_finder(23706032)))
# print(attempted_credits(student_finder(23706032)))
# print(specialization_avg(student_finder(23706032)))
# print(sci_y3_req(student_finder(23706032)))

# print(lab_req(student_finder(23706032)))
# print(communication_req(student_finder(77305712)))
# print(breadth_req(student_finder(77305712)))

# print(lab_req(student_finder(11223344)))
# print(communication_req(student_finder(11223344)))
# print(breadth_req(student_finder(11223344)))
# print(total_credits(student_finder(11223344)))
# print(attempted_credits(student_finder(11223344)))
# print(science_credits(student_finder(11223344)))
# print(sci_y4_req(student_finder(11223344)))

# change_year_standing(student_finder(77305712))
# change_year_standing(student_finder(23706032))
# change_year_standing(student_finder(11223344))

# print(student_finder(77305712))
# print(student_finder(23706032))
# print(student_finder(11223344))

# print(open_terms(student_finder(77305712)))
# print(open_terms(student_finder(23706032)))
# print(open_terms(student_finder(11223344)))