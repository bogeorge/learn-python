import sys

"""
Week 2, Day 10: Lists & List Comprehensions

Exercises to practice list methods, slicing, list comprehensions, 
and filtering/transforming lists.
"""


def exercise_1_list_methods():
    """
    Practice list methods and slicing.

    1. Create lists and use various list methods
    2. Practice slicing with positive and negative indices
    3. Demonstrate list concatenation and repetition
    """

    # Create a list
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    print("List methods practice:")
    print(f"  Original list: {fruits}")

    # Basic list methods
    fruits.append("fig")
    print(f"  After append('fig'): {fruits}")

    fruits.insert(2, "blueberry")
    print(f"  After insert(2, 'blueberry'): {fruits}")

    removed_fruit = fruits.pop(3)
    print(f"  After pop(3) removed '{removed_fruit}': {fruits}")

    fruits.remove("banana")
    print(f"  After remove('banana'): {fruits}")

    fruits.sort()
    print(f"  After sort(): {fruits}")

    fruits.reverse()
    print(f"  After reverse(): {fruits}")

    # Slicing
    print("\n  Slicing examples:")
    print(f"    fruits[1:4]: {fruits[1:4]}")
    print(f"    fruits[:3]: {fruits[:3]}")
    print(f"    fruits[2:]: {fruits[2:]}")
    print(f"    fruits[-3:]: {fruits[-3:]}")
    print(f"    fruits[::2]: {fruits[::2]}")  # Every other item
    print(f"    fruits[::-1]: {fruits[::-1]}")  # Reverse

    # List concatenation and repetition
    vegetables = ["carrot", "broccoli", "spinach"]
    combined = fruits + vegetables
    print(f"\n  Combined list: {combined}")

    repeated = ["hello"] * 3
    print(f"  Repeated list: {repeated}")


def exercise_2_list_comprehensions_basics():
    """
    Practice basic list comprehensions.

    1. Create lists using comprehensions
    2. Use comprehensions with conditions
    3. Transform elements in comprehensions
    """

    # Basic list comprehension
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squares = [x**2 for x in numbers]
    print("Basic list comprehensions:")
    print(f"  Numbers: {numbers}")
    print(f"  Squares: {squares}")

    # Comprehension with condition
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_numbers = [x for x in numbers if x % 2 != 0]

    print(f"\n  Even numbers: {even_numbers}")
    print(f"  Odd numbers: {odd_numbers}")

    # Transform with condition
    transformed = [x * 2 if x % 2 == 0 else x * 3 for x in numbers]
    print(f"  Transform (even*2, odd*3): {transformed}")

    # Create list of strings
    words = ["hello", "world", "python", "list", "comprehension"]

    uppercase_words = [word.upper() for word in words]
    word_lengths = [len(word) for word in words]
    filtered_words = [word for word in words if len(word) > 5]

    print(f"\n  Words: {words}")
    print(f"  Uppercase: {uppercase_words}")
    print(f"  Lengths: {word_lengths}")
    print(f"  Words longer than 5 chars: {filtered_words}")


def exercise_3_nested_list_comprehensions():
    """
    Practice nested list comprehensions.

    1. Create matrices using comprehensions
    2. Flatten nested lists
    3. Create combinations
    """

    # Create a matrix using nested comprehensions
    matrix = [[i + j for j in range(5)] for i in range(5)]

    print("Nested list comprehensions:")
    print("  Matrix (5x5):")
    for row in matrix:
        print(f"    {row}")

    # Flatten the matrix
    flat_list = [num for row in matrix for num in row]
    print(f"\n  Flattened matrix: {flat_list}")

    # Create all pairs from two lists
    colors = ["red", "green", "blue"]
    sizes = ["small", "medium", "large"]

    combinations = [(color, size) for color in colors for size in sizes]
    print(f"\n  Color-size combinations: {combinations}")

    # Create multiplication table
    n = 5
    multiplication_table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

    print(f"\n  Multiplication table (1-{n}):")
    for i, row in enumerate(multiplication_table, 1):
        print(f"    {i}: {row}")


def exercise_4_filter_and_transform():
    """
    Filter and transform lists using comprehensions.

    1. Filter lists based on multiple conditions
    2. Transform elements in complex ways
    3. Create dictionaries from lists
    """

    # Sample data
    students = [
        {"name": "Alice", "grade": 85, "attendance": 95},
        {"name": "Bob", "grade": 72, "attendance": 88},
        {"name": "Charlie", "grade": 91, "attendance": 92},
        {"name": "Diana", "grade": 68, "attendance": 75},
        {"name": "Eve", "grade": 95, "attendance": 98},
    ]

    print("Filter and transform practice:")
    print(f"  Students data: {students}")

    # Filter students with grade >= 80 and attendance >= 90
    high_performers = [
        student
        for student in students
        if student["grade"] >= 80 and student["attendance"] >= 90
    ]
    print(f"\n  High performers (grade>=80, attendance>=90): {high_performers}")

    # Create list of names with grades
    student_grades = [f"{s['name']}: {s['grade']}" for s in students]
    print(f"  Student grades: {student_grades}")

    # Create dictionary of students by first letter
    students_by_letter = {}
    for student in students:
        letter = student["name"][0].lower()
        if letter not in students_by_letter:
            students_by_letter[letter] = []
        students_by_letter[letter].append(student["name"])

    print(f"  Students by first letter: {students_by_letter}")

    # Transform with complex logic
    performance_levels = []
    for student in students:
        grade = student["grade"]
        if grade >= 90:
            level = "Excellent"
        elif grade >= 80:
            level = "Good"
        elif grade >= 70:
            level = "Average"
        else:
            level = "Needs Improvement"
        performance_levels.append(f"{student['name']}: {level}")

    print(f"  Performance levels: {performance_levels}")


def exercise_5_advanced_comprehensions():
    """
    Advanced list comprehension techniques.

    1. Use walrus operator (Python 3.8+)
    2. Create sets and dictionaries with comprehensions
    3. Handle multiple iterables
    """

    # Set comprehension
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

    unique_numbers = {x for x in numbers}
    unique_squares = {x**2 for x in numbers}

    print("Advanced comprehensions:")
    print(f"  Numbers with duplicates: {numbers}")
    print(f"  Unique numbers (set): {unique_numbers}")
    print(f"  Unique squares: {unique_squares}")

    # Dictionary comprehension
    words = ["apple", "banana", "cherry", "date", "elderberry"]

    word_lengths = {word: len(word) for word in words}
    long_words = {word: len(word) for word in words if len(word) > 5}

    print(f"\n  Words: {words}")
    print(f"  Word lengths (dict): {word_lengths}")
    print(f"  Long words only: {long_words}")

    # Multiple iterables with zip
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 72, 91]

    score_dict = {name: score for name, score in zip(names, scores)}
    print(f"\n  Names: {names}")
    print(f"  Scores: {scores}")
    print(f"  Name-score dictionary: {score_dict}")

    # Using enumerate in comprehension
    enumerated_words = [(i, word) for i, word in enumerate(words, 1)]
    print(f"\n  Enumerated words: {enumerated_words}")

    # Conditional dictionary comprehension
    temperatures = [
        ("Monday", 72),
        ("Tuesday", 68),
        ("Wednesday", 75),
        ("Thursday", 80),
        ("Friday", 82),
    ]

    hot_days = {day: temp for day, temp in temperatures if temp >= 75}
    print(f"\n  Hot days (temp >= 75): {hot_days}")


def mini_project_student_grade_analyzer():
    """
    Student Grade Analyzer

    Analyze student grades using list comprehensions and transformations.

    Features:
    1. Calculate statistics (average, min, max)
    2. Filter students by grade ranges
    3. Transform grades to letter grades
    4. Generate reports
    """
    import statistics

    print("=" * 50)
    print("STUDENT GRADE ANALYZER")
    print("=" * 50)

    # Sample student data
    students = [
        {"id": 1, "name": "Alice", "grades": [85, 92, 78, 95, 88]},
        {"id": 2, "name": "Bob", "grades": [72, 65, 80, 68, 74]},
        {"id": 3, "name": "Charlie", "grades": [91, 94, 89, 92, 95]},
        {"id": 4, "name": "Diana", "grades": [68, 72, 65, 70, 67]},
        {"id": 5, "name": "Eve", "grades": [95, 98, 92, 96, 97]},
        {"id": 6, "name": "Frank", "grades": [82, 85, 88, 79, 84]},
        {"id": 7, "name": "Grace", "grades": [55, 60, 58, 62, 57]},
        {"id": 8, "name": "Henry", "grades": [75, 78, 72, 80, 76]},
    ]

    def calculate_average(grades):
        """Calculate average of grades."""
        return sum(grades) / len(grades)

    def get_letter_grade(average):
        """Convert average to letter grade."""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    # Process students using list comprehensions
    processed_students = []
    for student in students:
        avg = calculate_average(student["grades"])
        letter = get_letter_grade(avg)
        processed_students.append(
            {
                "name": student["name"],
                "average": round(avg, 2),
                "letter_grade": letter,
                "grades": student["grades"],
            }
        )

    # Calculate class statistics
    class_averages = [s["average"] for s in processed_students]
    class_avg = statistics.mean(class_averages)
    class_min = min(class_averages)
    class_max = max(class_averages)

    # Filter students by grade range
    def filter_students_by_grade(min_grade=None, max_grade=None):
        """Filter students by average grade range."""
        filtered = processed_students

        if min_grade is not None:
            filtered = [s for s in filtered if s["average"] >= min_grade]

        if max_grade is not None:
            filtered = [s for s in filtered if s["average"] <= max_grade]

        return filtered

    print("\nClass Statistics:")
    print(f"  Class Average: {class_avg:.2f}")
    print(f"  Highest Average: {class_max:.2f}")
    print(f"  Lowest Average: {class_min:.2f}")

    print("\nStudent Report:")
    for student in processed_students:
        print(
            f"  {student['name']}: Avg={student['average']}, "
            f"Grade={student['letter_grade']}, Grades={student['grades']}"
        )

    print("\nAnalysis Options:")
    print("1. Show students with A grades (90+)")
    print("2. Show students with B grades (80-89)")
    print("3. Show students with C grades (70-79)")
    print("4. Show students with D grades (60-69)")
    print("5. Show students with F grades (<60)")
    print("6. Custom grade range")
    print("0. Exit")

    while True:
        try:
            choice = input("\nEnter your choice (0-6): ")

            if choice == "0":
                print("Exiting Grade Analyzer. Goodbye!")
                break

            elif choice == "1":
                filtered = filter_students_by_grade(min_grade=90)
                print("\nStudents with A grades (90+):")
                for s in filtered:
                    print(f"  {s['name']}: {s['average']}")

            elif choice == "2":
                filtered = filter_students_by_grade(min_grade=80, max_grade=89.99)
                print("\nStudents with B grades (80-89):")
                for s in filtered:
                    print(f"  {s['name']}: {s['average']}")

            elif choice == "3":
                filtered = filter_students_by_grade(min_grade=70, max_grade=79.99)
                print("\nStudents with C grades (70-79):")
                for s in filtered:
                    print(f"  {s['name']}: {s['average']}")

            elif choice == "4":
                filtered = filter_students_by_grade(min_grade=60, max_grade=69.99)
                print("\nStudents with D grades (60-69):")
                for s in filtered:
                    print(f"  {s['name']}: {s['average']}")

            elif choice == "5":
                filtered = filter_students_by_grade(max_grade=59.99)
                print("\nStudents with F grades (<60):")
                for s in filtered:
                    print(f"  {s['name']}: {s['average']}")

            elif choice == "6":
                try:
                    min_g = float(input("Enter minimum average: "))
                    max_g = float(input("Enter maximum average: "))
                    filtered = filter_students_by_grade(
                        min_grade=min_g, max_grade=max_g
                    )
                    print(f"\nStudents with averages between {min_g} and {max_g}:")
                    for s in filtered:
                        print(f"  {s['name']}: {s['average']}")
                except ValueError:
                    print("Please enter valid numbers.")

            else:
                print("Invalid choice. Please enter 0-6.")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break


def run_all_exercises():
    """Run all Day 10 exercises."""
    print("=" * 60)
    print("Week 2, Day 10: Lists & List Comprehensions")
    print("=" * 60)

    print("\n--- Exercise 1: List Methods ---")
    exercise_1_list_methods()

    print("\n--- Exercise 2: List Comprehensions Basics ---")
    exercise_2_list_comprehensions_basics()

    print("\n--- Exercise 3: Nested List Comprehensions ---")
    exercise_3_nested_list_comprehensions()

    print("\n--- Exercise 4: Filter and Transform ---")
    exercise_4_filter_and_transform()

    print("\n--- Exercise 5: Advanced Comprehensions ---")
    exercise_5_advanced_comprehensions()

    print("\n" + "=" * 60)
    print("Mini Project: Student Grade Analyzer")
    print("=" * 60)
    mini_project_student_grade_analyzer()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 10 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
