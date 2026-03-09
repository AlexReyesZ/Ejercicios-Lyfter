from student import Student

def get_name():
    return input('Full name: ').strip()

def get_section():
    return input('Section: ').strip()

def get_score(subject):
    while True:
        try:
            score = float(input(f'{subject} score (0-100): '))
            if 0 <= score <= 100:
                return score
            print('Error: score must be between 0 and 100')
        except ValueError:
            print('Error: Please enter a valid number')

def add_student(students):
    print("\n--- Add students ---")
    while True:
        name = get_name()
        section = get_section()
        spanish = get_score('spanish')
        english = get_score('english')
        socials = get_score('socials')
        science = get_score('science')

        # CREACIÓN DEL OBJETO
        new_student = Student(name, section, spanish, english, socials, science)
        students.append(new_student)
        
        if input("Do you want to add another student? (y/n): ").lower() != 'y':
            break

def print_student(student):
    print("-------------------------")
    # ACCESO POR ATRIBUTOS
    print(f"Name: {student.name}")
    print(f"Section: {student.section}")
    print(f"Spanish: {student.spanish}")
    print(f"English: {student.english}")
    print(f"Socials: {student.socials}")
    print(f"Science: {student.science}")
    print(f"Average: {student.get_average():.2f}")

def print_all_students(students):
    if not students:
        print("No students registered.")
        return
    print("\n=== STUDENTS LIST ===")
    for student in students:
        print_student(student)

def get_top_3_students(students):
    if not students:
        print('No students registered')
        return
    
    # Ordenamos usando el método get_average del objeto
    sorted_students = sorted(
        students,
        key=lambda s: s.get_average(),
        reverse=True
    )
    
    print("\n=== TOP 3 STUDENTS ===")
    for student in sorted_students[:3]:
        print("-------------------------")
        print(f"Name: {student.name} | Section: {student.section} | Average: {student.get_average():.2f}")

def calculate_general_average(students):
    if not students:
        print('No students registered')
        return
    
    total = sum(student.get_average() for student in students)
    general_average = total / len(students)
    print(f'\nGeneral average: {general_average:.2f}')