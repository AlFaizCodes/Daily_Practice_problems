FILE_NAME = "students.txt"


def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            students = []

            for line in lines:
                name, age, course = line.strip().split(",")
                students.append({
                    "name": name,
                    "age": age,
                    "course": course
                })
            return students

    except FileNotFoundError:
        return []


def save_data(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for s in students:
            file.write(f"{s['name']},{s['age']},{s['course']}\n")


def show_menu():
    print("\n Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


def add_student(students):
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    students.append({
        "name": name,
        "age": age,
        "course": course
    })

    save_data(students)
    print(" Student added successfully")


def view_students(students):
    if not students:
        print("No students found")
        return

    print("\n--- Student List ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")


def search_student(students):
    key = input("Enter name to search: ").lower()

    found = False
    for s in students:
        if key in s["name"].lower():
            print(f"Found → {s['name']} | Age: {s['age']} | Course: {s['course']}")
            found = True

    if not found:
        print(" Student not found")


def delete_student(students):
    name = input("Enter name to delete: ").lower()

    for s in students:
        if s["name"].lower() == name:
            students.remove(s)
            save_data(students)
            print(" Student deleted")
            return

    print(" Student not found")


# ---------- MAIN PROGRAM ----------

students = load_data()

while True:
    show_menu()
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number")
        continue

    if choice == 1:
        add_student(students)

    elif choice == 2:
        view_students(students)

    elif choice == 3:
        search_student(students)

    elif choice == 4:
        delete_student(students)

    elif choice == 5:
        print("👋 Goodbye!")
        break

    else:
        print("Invalid choice")
