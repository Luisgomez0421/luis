import json

# --- Configuration and Data Structures ---
# Tuple for fixed fields (Requirement 3 from Image 1)
FIELDS = ("id", "name", "age", "course", "status")
FILE_NAME = "students.json"
students = []

def load_data():
    """Loads student data from a JSON file into the students list."""
    global students
    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
            print("\n[System] Data loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        students = []
        print("\n[System] No existing data found. Starting fresh.")

def save_data():
    """Saves the current list of students to a JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        print("\n[System] Data saved to students.json.")
    except Exception as e:
        print(f"\n[Error] Could not save: {e}")

def add_student():
    """Collects input to add a new student dictionary to the list."""
    try:
        student_id = input("ID: ")
        # Check if ID already exists
        for s in students:
            if s["id"] == student_id:
                print("Error: ID already exists.")
                return

        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        status = input("Status (active/inactive): ").lower()

        if status not in ("active", "inactive"):
            print("Error: Invalid status.")
            return

        # Dictionary structure (Requirement 3 from Image 1)
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "status": status
        }

        students.append(student)
        print("Success: Student added.")
    except ValueError:
        print("Error: Age must be a number.")

def view_students():
    """Displays all student records currently in memory."""
    if not students:
        print("No students found.")
        return
    print("\n--- Current Students ---")
    for s in students:
        print(s)

def search_student():
    """Searches for a student by ID or Name."""
    query = input("Search ID or name: ")
    for s in students:
        if s["id"] == query or s["name"] == query:
            print(f"Found: {s}")
            return
    print("Not found.")

def update_student():
    """Updates fields of an existing student record."""
    student_id = input("ID to update: ")
    for s in students:
        if s["id"] == student_id:
            try:
                s["name"] = input("New name: ")
                s["age"] = int(input("New age: "))
                s["course"] = input("New course: ")
                s["status"] = input("New status: ")
                print("Updated successfully.")
                return
            except ValueError:
                print("Error: Age must be a number.")
                return
    print("Not found.")

def delete_student():
    """Removes a student from the list by ID."""
    student_id = input("ID to delete: ")
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("Deleted successfully.")
            return
    print("Not found.")

def menu():
    """Main application loop controlled by a boolean variable."""
    load_data()
    running = True # Control variable (Requirement 4 from Image 2)

    while running:
        print("\n1.Add | 2.View | 3.Search | 4.Update | 5.Delete | 6.Save | 7.Exit")
        op = input("Option: ")

        if op == "1":
            add_student()
        elif op == "2":
            view_students()
        elif op == "3":
            search_student()
        elif op == "4":
            update_student()
        elif op == "5":
            delete_student()
        elif op == "6":
            save_data()
        elif op == "7":
            save_data()
            print("Goodbye!")
            running = False # Stop the loop
        else:
            print("Invalid option.")

if __name__ == "__main__":
    print("=" * 60)
    print("Welcome to the Student Management System")
    print("=" * 60)
    menu()
