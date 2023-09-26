class student:
   def __init__(self, name, roll_number, cgpa):
       self. name=name 
       self.roll_number=roll_number 
       self. cgpa=cgpa 
def sort_students(student_list):
    sorted_students=sorted(student_list,key=lambda student:student.cgpa,  reverse=True)
 
    return sorted_students 
#Example usage:
students=[
    student("arvin","A122",1.2), 
    student("archi","A123",1.3), 
    student("mahi","A124",1.4), 
    student("maaji","A125",1.5), 
]
sorted_students=sort_students(students)
#print the sorted
for student in sorted_students:
    print("Name:{}, Roll Number:{})CGPA:{}".format(student.name,student.roll_number,student.cgpa))