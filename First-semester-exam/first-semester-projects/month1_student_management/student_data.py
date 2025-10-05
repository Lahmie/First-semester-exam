students = []

def add_student(name, age, grade):
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))
    try:
        if not isinstance(name, str) or not name.strip():
            print("Invalid name. Name must be a non-empty string.")
            return students
        
        if not isinstance(age, int):
            age = int(age)
        if age < 0:
            print("Invalid age. Age must be a positive number.")
            return students
            
        if not isinstance(grade, (int, float)):
            grade = float(grade)
        if grade < 0 or grade > 100:
            print("Invalid grade. Grade must be between 0 and 100.")
            return students
            
        student = {"name": name.strip(), "age": age, "grade": grade}
        students.append(student)
        print(f"Successfully added student: {name}")
        return students
        
    except ValueError:
        print("Invalid input. Age must be an integer and grade must be a number.")
        return students

def view_students(students):
    """
    TODO: Loop through the students list and print each student's info.
    """
    if not students:
        print("No students found.")
        return []
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    return students

def get_average_grade(students):
    """
    TODO: Return the average grade of all students.
    """
    if not students:
        return 0
    total_grade = sum(student['grade'] for student in students)
    average_grade = total_grade / len(students)
    return average_grade