#Question 1
'''
class Premium:
    def __init__(self):
        self.__vehicle_cost = None
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__premium_amount = None

    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_type(self,vehicle_type):
        if vehicle_type ==  "Two-Wheeler" or vehicle_type == "Four-Wheeler":
            self.__vehicle_type = vehicle_type
        else:
            print("Invalid Vehicle Details") 

    def calculate_premium(self):
        if self.__vehicle_type == "Two-Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.02
        if self.__vehicle_type == "Four-Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.06
        else:
            print("Invalid Details to calculate Premium")

    def display(self):
        print(f"Vehicle Cost: {self.__vehicle_cost}")
        print(f"Vehicle ID: {self.__vehicle_id}")
        print(f"Vehicle Type: {self.__vehicle_type}")
        print(f"Premium Amount: {self.__premium_amount}")
v = Premium()
v.set_vehicle_id(int(input("Enter Vehicle ID ")))
v.set_vehicle_cost(int(input("Enter  Vehicle Cost ")))
v.set_vehicle_type(input("Enter Vehicle Type "))
v.calculate_premium()
v.display()  
'''
#Question 2
'''
import sys
course = {1001:25575.0,1002:15500.0}
class Student:
    def __init__(self):
        self.__student_id = None
        self.__student_marks = None
        self.__student_age = None
        self.__student_courseid = None
        self.__student_fees = None
    #Setter for student
    def set_id(self, id):
        self.__student_id = id
    def set_marks(self, marks):
        self.__student_marks = marks
    def set_age(self, age):
        self.__student_age = age
    
    #Getter for student
    def get_id(self):
        return self.__student_id
    def get_age(self):
        return self.__student_age
    def get_marks(self):
        return self.__student_marks
    def get_course_id(self):
        return self.__student_courseid
    def get_student_fees(self):
        return self.__student_fees 
    
    def validate_age(self):
        if self.__student_age > 20:
            return True
        else:
            return False
    def validate_marks(self):
        if self.__student_marks >= 0 and self.__student_marks <= 100:
            return True
        else:
            return False
        
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__student_marks >= 65:
                return True
        else:
            return False
    
    def choose_course(self, course_id):
        if self.check_qualification():
            print("<----****----Congratulations you are qualified for this course----****---->")
            if course_id in course.keys():
                self.__student_courseid = course_id
                if self.__student_marks > 85:
                    
                    self.__student_fees= course[course_id] *0.75
                else:
                    self.__student_fees= course[course_id]
            else:
                print("Invalid course id")
        else:
            print("Not allowed to choose course")
            sys.exit(1)
    
s = Student()
s.set_age(int(input("Enter Age ")))
s.set_id(int(input("Enter ID ")))
s.set_marks(int(input("Enter Marks ")))
s.validate_age()
s.validate_marks()
s.check_qualification()
s.choose_course(int(input("Choose Course (1001 or 1002) ")))
print("Student Id:",s.get_id())
print("Age: ",s.get_age())
print("Marks: ",s.get_marks())
print("Fees: ",s.get_student_fees())
print("Course id: ",s.get_course_id())    
'''


