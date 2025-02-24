from main.students import Student

class TestStudent:

    def setup_method(self, method):

        self.test_student = Student(name = "Pari Khanna", student_id = 77305712, address = "Abbotsford, B.C.", program = "B.SC", faculty = "Science", specialization = "CPSC", standing = 2, completed_courses = [], grades = [], registered_courses = [])

    def test_reg(self):
        
        self.test_student.reg("CPSC210")
        assert len(self.test_student.get_registered_courses()) == 1
        assert self.test_student.get_registered_courses() == ["CPSC210"]

    def test_unenroll(self):
        self.test_student.reg("CPSC210")
        self.test_student.reg("CPSC121")
        self.test_student.unenroll("CPSC210")
        assert len(self.test_student.get_registered_courses()) == 1
        assert self.test_student.get_registered_courses() == ["CPSC121"]

    def test_add_grade(self):
        self.test_student.add_grade("CPSC210", 90, "A+")
        assert len(self.test_student.get_grades()) == 1
        assert self.test_student.get_grades() == [("CPSC210", 90, "A+")]
    
    def test_add_completed_course(self):
        self.test_student.add_completed_course("CPSC121")
        assert len(self.test_student.get_completed_courses()) == 1
        assert self.test_student.get_completed_courses() == ["CPSC121"]


        

        

