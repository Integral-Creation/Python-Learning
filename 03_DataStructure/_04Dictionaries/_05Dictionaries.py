student_grades = {}

number_students = int(input('Enter Total no of students: '))

for i in range(number_students):
    student_name = input('Enter Student name: ')
    grade = int(input('Enter Student grade: '))

    student_grades[student_name] = grade

sum = 0
count = 0

for key in student_grades:
    sum += student_grades[key]
    count+=1

avg = sum / count

print(f"Average of class: {avg:.2f}")

"""
Output:
    Enter Total no of students: 3
    Enter Student name: Harold
    Enter Student grade: 88
    Enter Student name: Alice
    Enter Student grade: 89
    Enter Student name: Elina
    Enter Student grade: 90
    Average of class: 89.00
"""