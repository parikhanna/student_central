

from students import student_finder

from students import id_pass

import operations


def student_login():

    """
    Asks the user for student id and password and returns an object of Student class if student is found.
    """

    current_student = ""
    password = ""

    while current_student.isdigit() == False or student_finder(int(current_student)) == False or id_pass[current_student] != password:
        current_student = input("Student ID: ")
        password = input("Password: ")

        if current_student.isdigit() == False or student_finder(int(current_student)) == False or id_pass[current_student] != password:
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
        option = input("Choose an option (1,2,3 OR 4): \n1: Personal Information \n2: Courses \n3: Grades \n4: Logout \n")

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
        course_option = input("Choose an option (1,2,3 Or 4): \n1: Course Info \n2: Register \n3: Unenroll \n4: Home \n")

        if course_option not in acceptable_options:
            print("Invalid Option")
    
    return course_option




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
                    current_course = operations.course_code_display()
                    operations.course_reg(current_student, current_course)

                elif course_option == "3":
                    current_course = operations.course_code_display()
                    operations.course_unenroll(current_student, current_course)

                else:
                    course_end_session = True
                    end_session = False

        elif chosen_option == "3":
            current_student.display_grades()
            end_session = operations.end_session_display()

        else:
            end_session = True


