import csv  

def read_students(file_name):
    students = []
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                students.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return students

def search_students(students, search_type, search_value):
    results = []
    for student in students:
        if search_type.lower() == 'matric' and student['Matric no'].strip() == search_value.strip():
            results.append(student)
        elif search_type.lower() == 'name' and search_value.strip().lower() in student['name'].strip().lower():
            results.append(student)
    return results

def display_student(student):
    print(f"Matric No: {student['Matric no']}")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"CGPA: {student['CGPA']}")
    print("-" * 30)

def main():
    file_name = 'students.txt'
    students = read_students(file_name)
    
    if not students:
        print("No student records found.")
        return
    
    print("Welcome to Student Search System!")
    print("You can search by 'matric' (for matric number) or 'name' (for student name).")
    
    while True:
        search_type = input("Enter search type (matric/name) or 'exit' to quit: ").strip()
        if search_type.lower() == 'exit':
            break
        search_value = input(f"Enter the {search_type} to search for: ").strip()
        
        results = search_students(students, search_type, search_value)
        
        if results:
            print(f"Found {len(results)} matching student(s):")
            for student in results:
                display_student(student)
        else:
            print("No matching students found.")

if __name__ == "__main__":
    main()