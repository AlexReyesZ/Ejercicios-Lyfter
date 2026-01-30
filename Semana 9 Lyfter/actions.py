def get_name():
    return input('Full name: ').strip()


def get_section():
    return input('Section: ').strip()


def get_score(subject):

    while True:
        try:
            score= float(input(f'{subject} score (0-100): '))

            if score < 0 or score > 100:
                print('Error: score must be between 0 and 100')
                continue
            return score
        except ValueError:
            print('Error: Please enter a valid number')
    


def create_student(name, section, spanish, english, socials, science):
    return {
        'name': name,
        'section': section,
        'spanish': spanish,
        'english': english,
        'socials': socials,
        'science': science
    }


def add_student(students):
    print("\n--- Add students ---")

    while True:
        name=get_name()
        section=get_section()

        spanish=get_score('spanish')
        english=get_score('english')
        socials=get_score('socials')
        science=get_score('science')

        student=create_student(
            name,
            section,
            spanish,
            english,
            socials,
            science
        )

        students.append(student)
        
        more = input("Do you want to add another student? (y/n): ").lower()
        if more != 'y':
            break

def has_students(students):
    return len(students) > 0


def print_student(student):
    print("-------------------------")
    print(f"Name: {student['name']}")
    print(f"Section: {student['section']}")
    print(f"Spanish: {student['spanish']}")
    print(f"English: {student['english']}")
    print(f"Socials: {student['socials']}")
    print(f"Science: {student['science']}")


def print_all_students(students):
    if not has_students(students):
        print("No students registered.")
        return

    print("\n=== STUDENTS LIST ===")
    for student in students:
        print_student(student)


def calculate_average(student):
    total= (
        student['spanish'] +
        student['english'] +
        student['socials'] +
        student['science']
    )
    return total/4


def get_top_3_students(students):
    if not has_students(students):
        print('No students registered')
        return
    
    sorted_students = sorted(
        students,
        key=calculate_average,
        reverse=True
    )
    print("\n=== TOP 3 STUDENTS ===")

    top = sorted_students[:3]

    for student in top:
        average = calculate_average(student)
        print("-------------------------")
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Average: {average:.2f}")


def calculate_general_average(students):
    if not has_students(students):
        print('No students registered')
        return

    total= 0

    for student in students:
        total+= calculate_average(student)

    general_average = total/ len(students)

    print(f'\nGeneral average:{general_average: .2f}')
