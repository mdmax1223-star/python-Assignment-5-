# Task 1: Create a Dictionary of Student Marks

# Creating the dictionary of students and their marks
students_marks = {
    'John': 85,
    'Alice': 92,
    'Bob': 78,
    'David': 90,
    'Emma': 88
}

# Asking user to input a student's name
student_name = input("Enter the student's name to retrieve their marks: ")

# Checking if the student exists in the dictionary
if student_name in students_marks:
    print(f"The marks for {student_name} are: {students_marks[student_name]}")
else:
    print(f"Sorry, the student '{student_name}' does not exist in the records.")
