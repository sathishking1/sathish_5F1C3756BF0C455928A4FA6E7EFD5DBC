class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_student(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

students = [
    student("Amith", "02", 9.8),
    student("Monesh", "10", 8.5),
    student("Parvesh", "15", 7.5),
    student("Rajasekar", "18", 7.4),
]
sorted_students = sort_student(students)
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                      student.roll_number,
                                                      student.cgpa))