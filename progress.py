# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"  # Assigning 'F' for scores below 40

# Function to handle error checking for numeric input
def get_marks_input(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Please enter marks between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Function to input student data and generate report cards
def student_report_card():
    students = []
    
    while True:
        print("\n📌 Enter details for a new student:")
        name = input("Student Name: ")
        roll_number = input("Roll Number: ")

        # Getting marks for subjects
        math = get_marks_input("Math")
        physics = get_marks_input("Physics")
        urdu = get_marks_input("Urdu")
        english = get_marks_input("English")
        computer = get_marks_input("Computer")

        # Calculate total and percentage
        total_marks = math + physics + urdu + english + computer
        percentage = (total_marks / 500) * 100
        grade = calculate_grade(percentage)

        # Store student data
        student_data = {
            "Name": name,
            "Roll Number": roll_number,
            "Math": math,
            "Physics": physics,
            "Urdu": urdu,
            "English": english,
            "Computer": computer,
            "Total Marks": total_marks,
            "Percentage": percentage,
            "Grade": grade
        }

        students.append(student_data)

        # Ask if the user wants to enter more student data
        more_data = input(f"\n✅ Record for {name} inserted successfully. Do you want to insert more? (Y/N): ").strip().upper()
        if more_data != 'Y':
            break

    # Generate report cards for all students
    print("\n📄 Generating Report Cards...\n")
    for student in students:
        print("=" * 40)
        print(f"📜 Report Card for {student['Name']} (Roll No: {student['Roll Number']})")
        print("=" * 40)
        print(f"📌 Math: {student['Math']}")
        print(f"📌 Physics: {student['Physics']}")
        print(f"📌 Urdu: {student['Urdu']}")
        print(f"📌 English: {student['English']}")
        print(f"📌 Computer: {student['Computer']}")
        print("-" * 40)
        print(f"🎯 Total Marks: {student['Total Marks']} / 500")
        print(f"📊 Percentage: {student['Percentage']:.2f}%")
        print(f"🏆 Grade: {student['Grade']}")
        print("=" * 40, "\n")

# Main function to start the program
if __name__ == "__main__":
    student_report_card()
