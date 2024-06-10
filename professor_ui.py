

from students import student_finder

from courses import course_finder

from operations import end_session_display


def professor_login():

    """
    Asks the user for student id and returns an object of Student class if student is found.
    """

    current_student = ""

    while current_student.isdigit() == False or student_finder(int(current_student)) == False:
        current_student = input("Student ID: ")

        if current_student.isdigit() == False:
            print("Error: Invalid Student ID")
        elif student_finder(int(current_student)) == False:
            print("Error: Student Does Not Exist")
        else:
            return student_finder(int(current_student))
        

def prof_options_display():

    """
    Displays the menu options to the user and returns the chosen option.
    """

    option = ""
    acceptable_options = ["1", "2", "3"]

    while option not in acceptable_options:
        option = input("Choose an option (1,2 OR 3): \n1: Student Information \n2: Submit Grades \n3: Logout \n")

        if option not in acceptable_options:
            print("Invalid Option")
    
    return option


def add_grades_display():

    """
    Asks the user to input the course code and the percentage grade achieved by the student in that course in order to add it to the student's course database.
    """

    course = ""
    percentage_grade = ""

    while course_finder(c_code) == False:
        c_code = input("Please enter the course code: ")

        if course_finder(c_code) == False:
            print("Invalid Course Code")
    
    while course_grade.isdigit() == False or not (0 <= int(course_grade) <= 100):
        course_grade = input("Please enter the percentage grade (Do not include the percentage sign): ")

        if course_grade.isdigit() == False or not (0 <= int(course_grade) <= 100):
            print("Invalid Grade")

    return [c_code, int(course_grade)]



        
if __name__ == "__main__":

    end_session = False
    current_student = professor_login()

    while end_session == False:
            chosen_option = prof_options_display()

            if chosen_option == "1":
                print(current_student)
                end_session = end_session_display()

            elif chosen_option == "2":

                adding_grades = add_grades_display()

                c_code = adding_grades[0]
                perc_grade = adding_grades[1]

                current_student.adde_grade(c_code, perc_grade)
                print("Grade succesfully added!")

                end_session = end_session_display()

            else:
                end_session = True


# TESTING:

# print(student_finder(77305712).completed_courses)
# print(student_finder(77305712).registered_courses)
# print(student_finder(77305712).grades)