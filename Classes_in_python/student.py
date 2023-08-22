class Student:
    def __init__(self, student_id, first_name, last_name, age):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.courses = []

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
    def display_info(self):
        print("Student id :", self.student_id)
        print("first_name :", self.first_name)
        print("Last_name :", self.last_name)
        print("Age :", self.age)
        print("Courses :", self.courses)

def main():
    student_naji = Student("L1f21bscs0272", "Syed", "Najiullah", 20)
    student_naji.add_course("OOP")
    student_naji.add_course("OOP")
    student_naji.add_course("DSA")
    student_naji.add_course("DATA BASE")
    student_naji.add_course("Assembly")
    student_naji.display_info()


    student_safi = Student("L1f21bscs1122", "Syed", "Safiullah", 21)
    student_safi.add_course("OOP")
    student_safi.add_course("DSA")
    student_safi.add_course("DATA BASE")
    student_safi.add_course("Assembly")
    student_safi.display_info()

if __name__ == "__main__":
    main()