# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Name: Your Name

def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent!"
    elif avg >= 80:
        return "B", "Very Good!"
    elif avg >= 70:
        return "C", "Good"
    elif avg >= 60:
        return "D", "Needs Improvement"
    else:
        return "F", "Failed"

def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} marks (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Enter numbers only.")

def main():
    names = []
    results = []

    count = int(input("How many students? "))

    for i in range(count):
        name = input("Student Name: ")
        m1 = get_valid_mark("Math")
        m2 = get_valid_mark("Science")
        m3 = get_valid_mark("English")

        avg = (m1 + m2 + m3) / 3
        grade, comment = calculate_grade(avg)

        names.append(name)
        results.append((avg, grade, comment))

    print("\nResults:")
    for i in range(count):
        print(names[i], results[i])

if __name__ == "__main__":
    main()
