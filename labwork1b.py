def students():
    count = int(input("Enter the number of students "))
    return count
def infor_student(num_students):
    print("\n Enter information of students ")
    students_list = []
    
    for i in range (num_students):
        print(f"\n---Student {i+1}---")
        s_so = input("ID :")
        s_ten = input("Name: ")
        s_dob = input("Birth: ")
         
        student ={
            "id": s_so,
            "name": s_ten,
            "birth": s_dob,
             
         }
        students_list.append(student)
    return students_list
def list_students(student_list):
    print("\n--- LIST OF STUDENTS ---")

    for student in student_list:
        print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Birth: {student['birth']}"
        )
def courses():
    c_count = int(input("Enter the number of courses"))
    return c_count
def infor_courses(num_courses):
    print("\n Enter information of courses")
    courses_list =[]
    for i in range(num_courses):
        print(f"\n Course {i+1} :")
        id_course = input("ID :")
        name_course = input("Name: ")
        
        inforcourses ={
            "ID": id_course,
            "Name": name_course,
        }
        courses_list.append(inforcourses)
    return courses_list
def input_marks(student_list, courses_list, marks):
    course_id = input("Enter the ID course: ")

    course_found = False

    for course in courses_list:
        if course["ID"] == course_id:
            course_found = True
            break

    if course_found == False:
        print("Course is not found")
        return

    print(f"\nInputting marks for course {course_id}")

    for student in student_list:
        score = float(input(f"Enter the score for {student['name']}: "))

        student_id = student["id"]

        if student_id not in marks:
            marks[student_id] = {}

        marks[student_id][course_id] = score
def main():
    students_list = []
    courses_list = []
    marks = {}

    # Input students
    num_students = students()
    students_list = infor_student(num_students)

    # Input courses
    num_courses = courses()
    courses_list = infor_courses(num_courses)

    # Input marks
    input_marks(students_list, courses_list, marks)

    # List students
    list_students(students_list)


main()
    
    
        
        
    
    
    
    
    
        
        
