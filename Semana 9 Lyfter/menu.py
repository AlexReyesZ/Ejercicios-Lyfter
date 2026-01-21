from actions import add_student, print_all_students, get_top_3_students, calculate_general_average
from data import export_to_csv, import_from_csv




def start_menu():
    students=[]

    while True:
        print('\n===== MENU ======')
        print('1. Add students')
        print('2. View all students')
        print('3. View top 3 students')
        print('4. View general average')
        print('5. Export students to CSV')
        print('6. Import students from CSV')
        print('7. Exit')

        option=input('Choose an option: ')


        if option == '1':
            add_student(students)

        elif option == '2':
            print_all_students(students)

        elif option == '3':
            get_top_3_students(students)
        
        elif option == '4':
            calculate_general_average(students)

        elif option == '5':
            export_to_csv(students)

        elif option == '6':
            students = import_from_csv()

        elif option == '7':
            print('Goodbye!')
            break

        else:
            print('Invalid option. Try again.')