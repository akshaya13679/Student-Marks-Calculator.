"""
Student Marks Calculator
Beginner-friendly Python student project.
"""

def get_marks(subject):
    """Ask for valid marks between 0 and 100."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(percentage):
    """Return a grade based on the percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def main():
    print("=" * 38)
    print("       STUDENT MARKS CALCULATOR")
    print("=" * 38)

    name = input("Enter student name: ").strip()
    if not name:
        name = "Student"

    subjects = ["English", "Mathematics", "Science", "Computer Science", "Social Studies"]
    marks_list = []

    for subject in subjects:
        marks_list.append(get_marks(subject))

    total = sum(marks_list)
    maximum = len(subjects) * 100
    percentage = total / maximum * 100
    grade = calculate_grade(percentage)

    print("\n" + "=" * 38)
    print("             MARKS REPORT")
    print("=" * 38)
    print(f"Student Name : {name}")
    for subject, marks in zip(subjects, marks_list):
        print(f"{subject:<20}: {marks:g}/100")
    print("-" * 38)
    print(f"Total Marks  : {total:g}/{maximum}")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")
    print("=" * 38)


if __name__ == "__main__":
    main()
