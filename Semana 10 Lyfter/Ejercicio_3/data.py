import csv
import os
from student import Student

file_name = 'Students.csv'

def export_to_csv(students):
    if not students:
        print('No students to export')
        return
    
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['name', 'section', 'spanish', 'english', 'socials', 'science']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for student in students:
            # Convertimos el OBJETO a DICCIONARIO para el CSV
            writer.writerow(student.to_dict())
            
    print('Students exported successfully')

def import_from_csv():
    if not os.path.exists(file_name):
        print("No exported file found.")
        return []

    students = []
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertimos cada fila (diccionario) en un OBJETO Student
            new_student = Student(
                row["name"], 
                row["section"], 
                row["spanish"], 
                row["english"], 
                row["socials"], 
                row["science"]
            )
            students.append(new_student)

    print("Students imported successfully.")
    return students