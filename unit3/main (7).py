class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the student list based on CGPA in descending order
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Input
students = [
    Student("Azhagumari", "8017", 7.9),
    Student("Kathir", "8015", 6.7),
    Student("karthi", "8018", 8.5),
    Student("Prakash", "8016", 7.0),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
