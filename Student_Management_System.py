class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_students(database, name, age, grades):
        student = Student(name, age, grades)
        database[name] = student

    def view_student(database, name):
        if name in database:
            student = database[name]
            print(f'Name: {student.name}')
            print(f'Age: {student.age}')
            print(f'Grades: {"," .join(map(str, student.grades))}')
        else:
            print(f"Student {name} not in database")

    def calculate_statistics(grades):
        import statistics as stats
        mean = stats.mean(grades)
        median = stats.median(grades)
        st_dev = stats.stdev(grades)
        return f'mean: {mean}, median: {median}, standard deviation: {st_dev}'

    def save_file(database, filename):
        with open(filename, 'a') as file:
            for name, student in database.items():
                file.write(
                    f"{name}, {student.age}, {', '.join(map(str,student.grades))}")
                file.write("\n")

    def main():
        student_database = {}
        while True:
            print('''                  =======================================
                  | Student Database Management System  |
                  |-------------------------------------|
                  | 1. Add a new student                |    
                  | 2. View a student                   |   
                  | 3. Calculate Statistics             |
                  | 4. Save to File                     |   
                  | 5. Quit                             |
                  ======================================= ''')
            choice = input("Enter your option (1-5): ")
            if choice == "1":
                name = input("Enter the student's name: ")
                age = int(input("Enter the student's age: "))
                grade = list(
                    map(int, input("Enter the student's grades separated by comma: ").split(',')))
                Student.add_students(student_database, name, age, grade)
            elif choice == "2":
                Student.view_student(student_database, input(
                    "Enter the student's name to view: "))
            elif choice == "3":
                stud_name = input(
                    "Enter the student's name to see statistics: ")
                print(
                    f"\nStatistics for {stud_name}: \n{Student.calculate_statistics(student_database[stud_name].grades)}")
            elif choice == "4":
                Student.save_file(student_database,
                                  input("Enter the filename: "))
            elif choice == "5":
                print("Exit Program")
                break
            else:
                print("Invalid Input of data")


if __name__ == '__main__':
    Student.main()
