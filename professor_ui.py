

from students import student_finder

from operations import end_session_display


# ---------------------------------
# FUNCTIONS:

def professor_login():

    """
    Asks the user for student id and returns an object of Student class if student is found
    """

    current_student = ""

    while current_student.isdigit() == False or student_finder(int(current_student)) == False:
        current_student = input("\nStudent ID: ")

        if current_student.isdigit() == False:
            print("Error: Invalid Student ID")
        elif student_finder(int(current_student)) == False:
            print("Error: Student Does Not Exist")
        else:
            return student_finder(int(current_student))
        

def prof_options_display():

    """
    Displays the menu options to the user and returns the chosen option
    """

    option = ""
    acceptable_options = ["1", "2", "3"]

    while option not in acceptable_options:
        option = input("\nChoose an option (1,2 OR 3): \n1: Student Information \n2: Submit Grades \n3: Logout \n \n")

        if option not in acceptable_options:
            print("Invalid Option")
    
    return option


def add_grades_display(current_student):

    """
    Asks the user to input the course code and the percentage grade achieved by the student in that course in order to add it to the student's course database
    """

    c_code = ""
    grade = ""
    exit = "X"

    while current_student.student_course_finder(c_code) == False and c_code != exit:
        c_code = input(" \nPlease enter the course code or enter X to return to options menu: ")

        if current_student.student_course_finder(c_code) == False and c_code != exit:
            print("Course Not Found")
    
    if c_code != exit:
    
        while grade.isdigit() == False or not (0 <= int(grade) <= 100):
            grade = input("Please enter the percentage grade (Do not include the percentage sign): ")

            if grade.isdigit() == False or not (0 <= int(grade) <= 100):
                print("Invalid Grade")

        return [int(current_student.student_course_finder(c_code)), int(grade)]
    
    else:
        return False


# ---------------------------------
# UI:
        
if __name__ == "__main__":

    end_session = False
    current_student = professor_login()

    while end_session == False:
            chosen_option = prof_options_display()

            if chosen_option == "1":
                print(current_student)
                end_session = end_session_display()

            elif chosen_option == "2":

                adding_grades = add_grades_display(current_student)

                if adding_grades != False:

                    c_code_index = adding_grades[0]
                    perc_grade = adding_grades[1]

                    current_student.add_grade(c_code_index, perc_grade)
                    print("Grade succesfully added!")

                    end_session = end_session_display()
                
                else:
                    end_session = False

            else:
                end_session = True


# ---------------------------------
# TESTING:

# Checking if the grades succesfully got added:

# for courses in student_finder(77305712).student_course_db:
#     print(f"{courses.course_code}, {courses.percentage_grade}, {courses.letter_grade}")