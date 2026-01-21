import csv
import os


file_name= 'Students.csv'


def export_to_csv(students):
    if not students:
        print('No students to export')
        return
    
    with open(file_name, mode='w', newline='') as file:
        writer=csv.DictWriter(
            file,
            fieldnames=[
                'name',
                'section',
                'spanish',
                'english',
                'socials',
                'science'
            ]
        )
        writer.writeheader()
        writer.writerows(students)
    print('students exported succesfully')


def import_from_csv():
    if not os.path.exists(file_name):
        print("No exported file found.")
        return []

    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file)
        students = []

        for row in reader:
            students.append({
                "name": row["name"],
                "section": row["section"],
                "spanish": float(row["spanish"]),
                "english": float(row["english"]),
                "socials": float(row["socials"]),
                "science": float(row["science"])
            })

    print("Students imported successfully.")
    return students
