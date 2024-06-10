

import students

from students import student_finder

from courses import create_student_course

import operations

from datetime import datetime


def student_login():

    """
    Asks the user for student id and password and returns an object of Student class if student is found.
    """

    current_student = ""
    password = ""

    while current_student.isdigit() == False or student_finder(int(current_student)) == False or students.id_pass[current_student] != password:
        current_student = input("Student ID: ")
        password = input("Password: ")

        if current_student.isdigit() == False or student_finder(int(current_student)) == False or students.id_pass[current_student] != password:
            print("Error: Invalid Student ID or Password")
        else:
            return student_finder(int(current_student))
        

def std_options_display():

    """
    Displays the menu options to the user and returns the chosen option.
    """

    option = ""
    acceptable_options = ["1", "2", "3", "4"]

    while option not in acceptable_options:
        option = input("Choose an option [1,2,3,4]: \n1: Personal Information \n2: Courses \n3: Grades \n4: Logout \n")

        if option not in acceptable_options:
            print("Invalid Option")
    
    return option


def courses_display():

    """
    Displays course menu options to the user and returns the option chosen.
    """

    course_option = ""
    acceptable_options = ["1", "2", "3", "4"]

    while course_option not in acceptable_options:
        course_option = input("Choose an option [1,2,3,4]: \n1: Course Info \n2: Register \n3: Unenroll \n4: Home \n")

        if course_option not in acceptable_options:
            print("Invalid Option")
    
    return course_option


def term_display(current_student):

    """
    Asks users what term they would like to register for and returns the chosen term.
    """

    term_option = ""

    open_terms = operations.open_terms(current_student)

    options_list = list(range(1, (len(open_terms) + 1)))


    while term_option.isdigit() == False or int(term_option) not in options_list:

        print("Choosen an option {}:".format(options_list))

        for index,term in enumerate(open_terms):
            print("{}. {}".format((index + 1),term))

        term_option = input("")

        if term_option.isdigit() == False or int(term_option) not in options_list:
            print("Invalid Option")

    return open_terms[(int(term_option) - 1)]


def withdraw_without_w_deadline(student_course):

    course_term = student_course.term
    course_year = student_course.year
    deadline = 0

    if course_term == "Fall":
        deadline = datetime(course_year, 9, 16, 23, 59, 59)
    elif course_term == "Winter":
        deadline = datetime(course_year, 1, 17, 23, 59, 59)
    elif course_term == "Summer Term 1":
        deadline = datetime(course_year, 5, 17, 23, 59, 59)
    else:
        deadline = datetime(course_year, 7, 8, 23, 59, 59)
    
    return deadline


def withdraw_with_w_deadline(student_course):

    course_term = student_course.term
    course_year = student_course.year
    deadline = 0

    if course_term == "Fall":
        deadline = datetime(course_year, 10, 25, 23, 59, 59)
    elif course_term == "Winter":
        deadline = datetime(course_year, 3, 7, 23, 59, 59)
    elif course_term == "Summer Term 1":
        deadline = datetime(course_year, 6, 7, 23, 59, 59)
    else:
        deadline = datetime(course_year, 7, 26, 23, 59, 59)
    
    return deadline


def withdraw_confirmation_display():

    """
    Asks users to confirm that they would like to unenroll. 
    Returns True if confirmed, False otherwise
    """

    confirmation = ""
    accepted_values = ["Y", "N"]

    while confirmation not in accepted_values:

        confirmation = input("Would you like to unenroll? Enter Y to confirm or enter N to exit. \n")

        if confirmation not in accepted_values:
            print("Please enter a valid option [Y or N]")
    
    if confirmation == "Y":
        return True
    else:
        return False


def unenroll_course_display(current_student, c_code):

    """
    Handles student unenrollment from a course by checking registration status and deadline adherence, and processes unenrollment with or without a 'W' standing accordingly
    """
    
    student_course = current_student.student_course_finder(c_code)
    registered_courses_codes = current_student.registered_courses_codes()
    
    if c_code not in registered_courses_codes:
        print(f"Student Not Registered in {c_code}")
    
    elif datetime.now() > withdraw_with_w_deadline(student_course):
        print("Error: The deadline to drop this course has passed.")
        
    else:

        w_standing = False

        if datetime.now() > withdraw_without_w_deadline(student_course):
            print("The deadline to withdraw from the course without W standing has passed.")
            w_standing = True
        
        confirmation = withdraw_confirmation_display()
        if confirmation:
            if w_standing:
                current_student.unenroll_with_w(student_course)
                print("Course Succesfully Dropped")
            else:
                current_student.unenroll_without_w(student_course)
                print("Course Succesfully Dropped")

        else:
            course_end_session = True
            end_session = False


if __name__ == "__main__":

    end_session = False
    course_end_session = False
    current_student = student_login()
        
    while end_session == False:
        chosen_option = std_options_display()

        if chosen_option == "1":
            print(current_student)
            end_session = operations.end_session_display()

        elif chosen_option == "2":

            course_end_session = False

            while course_end_session == False:
                course_option = courses_display()

                if course_option == "1":
                    current_course = operations.course_code_display()
                    print(current_course) 

                elif course_option == "2":
                    chosen_term = term_display(current_student).split()
                    term = chosen_term[1:]
                    year = int(chosen_term[0])
                    current_course = operations.course_code_display()
                    create_student_course(current_course, current_student, term, year)

                elif course_option == "3":
                    current_course = operations.course_code_display()
                    unenroll_course_display(current_student, current_course.course_code)

                else:
                    course_end_session = True
                    end_session = False

        elif chosen_option == "3":
            current_student.display_grades()
            end_session = operations.end_session_display()

        else:
            end_session = True


