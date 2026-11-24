import csv
import json
import os
import sys

"""
Week 4, Day 23: CSV & JSON

Exercises to practice working with CSV and JSON file formats.
"""


def exercise_1_csv_basics():
    """
    Basic CSV file operations.

    1. Write data to CSV file
    2. Read data from CSV file
    3. Work with different CSV formats
    """
    print("Exercise 1: CSV Basics")
    print("-" * 40)

    # Create sample data
    employees = [
        {"name": "Alice", "age": 30, "department": "Engineering", "salary": 80000},
        {"name": "Bob", "age": 25, "department": "Design", "salary": 65000},
        {"name": "Charlie", "age": 35, "department": "Management", "salary": 95000},
        {"name": "Diana", "age": 28, "department": "Engineering", "salary": 75000},
    ]

    # Write CSV file
    with open("employees.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "age", "department", "salary"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(employees)

    print("Created employees.csv")

    # Read CSV file
    print("\nReading CSV file:")
    with open("employees.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for i, row in enumerate(reader, 1):
            print(
                f"  Employee {i}: {row['name']}, {row['age']} years, "
                f"{row['department']}, ${row['salary']}"
            )

    # Read as list of lists
    print("\nReading as list of lists:")
    with open("employees.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for row in rows:
            print(f"  {row}")

    # Clean up
    os.remove("employees.csv")


def exercise_2_csv_advanced():
    """
    Advanced CSV operations.

    1. Different delimiters
    2. Quotes and special characters
    3. CSV dialects
    4. Filtering and transforming data
    """
    print("\n\nExercise 2: Advanced CSV")
    print("-" * 40)

    # Create data with special characters
    products = [
        ["ID", "Name", "Price", "Description", "In Stock"],
        ["1", "Laptop", "1200.99", "High-performance laptop", "Yes"],
        ["2", "Mouse", "25.50", "Wireless mouse, includes battery", "Yes"],
        ["3", "Keyboard", "89.99", "Mechanical keyboard with RGB", "No"],
        ["4", "Monitor", "450.00", '27" 4K monitor', "Yes"],
    ]

    # Write with different delimiter
    with open("products.tsv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")  # Tab-separated
        writer.writerows(products)

    print("Created tab-separated products.tsv")

    # Read with correct delimiter
    print("\nReading TSV file:")
    with open("products.tsv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        for row in reader:
            print(f"  {row}")

    # Using quotes for fields with delimiters
    print("\n\nCSV with quotes:")
    data_with_commas = [
        ["City", "Population", "Description"],
        ["New York", "8400000", "The city that never sleeps"],
        ["San Francisco", "815000", "Foggy, hilly, tech hub"],
        ["Austin, Texas", "960000", "Live music capital"],
    ]

    with open("cities.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)  # Quote all fields
        writer.writerows(data_with_commas)

    print("\nCSV content (with quotes):")
    with open("cities.csv", "r") as f:
        print(f.read())

    # Filter data
    print("\n\nFiltering CSV data:")
    with open("cities.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        print("Cities with population > 1,000,000:")
        for row in reader:
            population = int(row["Population"])
            if population > 1000000:
                print(f"  {row['City']}: {population:,}")

    # Clean up
    os.remove("products.tsv")
    os.remove("cities.csv")


def exercise_3_json_basics():
    """
    Basic JSON operations.

    1. Write Python objects to JSON
    2. Read JSON files
    3. Pretty-print JSON
    """
    print("\n\nExercise 3: JSON Basics")
    print("-" * 40)

    # Create Python data structures
    company_data = {
        "name": "TechCorp Inc.",
        "founded": 2010,
        "headquarters": "San Francisco",
        "departments": [
            {"name": "Engineering", "employees": 50, "manager": "Alice Johnson"},
            {"name": "Sales", "employees": 25, "manager": "Bob Smith"},
            {"name": "Marketing", "employees": 15, "manager": "Charlie Brown"},
        ],
        "revenue_millions": 45.2,
        "public": False,
    }

    # Write JSON to file
    with open("company.json", "w") as jsonfile:
        json.dump(company_data, jsonfile, indent=2)

    print("Created company.json")

    # Read JSON from file
    with open("company.json", "r") as jsonfile:
        loaded_data = json.load(jsonfile)

    print("\nLoaded data:")
    print(f"Company: {loaded_data['name']}")
    print(f"Founded: {loaded_data['founded']}")
    print(f"Headquarters: {loaded_data['headquarters']}")
    print(f"Revenue: ${loaded_data['revenue_millions']}M")
    print(f"Public: {loaded_data['public']}")

    print("\nDepartments:")
    for dept in loaded_data["departments"]:
        print(
            f"  {dept['name']}: {dept['employees']} employees, "
            f"Manager: {dept['manager']}"
        )

    # Pretty print JSON
    print("\n\nPretty printed JSON:")
    pretty_json = json.dumps(loaded_data, indent=2)
    print(pretty_json[:200] + "...")  # Print first 200 chars

    # Clean up
    os.remove("company.json")


def exercise_4_json_advanced():
    """
    Advanced JSON operations.

    1. Custom JSON encoding/decoding
    2. Handling dates and other non-serializable types
    3. JSON schema validation
    """
    print("\n\nExercise 4: Advanced JSON")
    print("-" * 40)

    from datetime import date, datetime

    # Custom encoder for dates
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime, date)):
                return obj.isoformat()
            elif isinstance(obj, set):
                return list(obj)
            return super().default(obj)

    # Create data with dates and sets
    project_data = {
        "name": "Website Redesign",
        "start_date": date(2024, 1, 15),
        "due_date": date(2024, 6, 30),
        "team": {"Alice", "Bob", "Charlie"},  # Set
        "budget": 50000,
        "milestones": [
            {
                "name": "Design Phase",
                "completed": True,
                "completion_date": date(2024, 2, 28),
            },
            {
                "name": "Development",
                "completed": False,
                "target_date": date(2024, 5, 15),
            },
        ],
    }

    # Write with custom encoder
    with open("project.json", "w") as jsonfile:
        json.dump(project_data, jsonfile, cls=CustomJSONEncoder, indent=2)

    print("Created project.json with custom encoding")

    # Custom decoder for dates
    def custom_json_decoder(dct):
        for key, value in dct.items():
            if isinstance(value, str):
                # Try to parse dates
                try:
                    # Try ISO format date
                    dct[key] = datetime.fromisoformat(value).date()
                except ValueError, AttributeError:
                    # Not a date, keep as string
                    pass
        return dct

    # Read and decode
    with open("project.json", "r") as jsonfile:
        loaded_data = json.load(jsonfile, object_hook=custom_json_decoder)

    print("\nLoaded and decoded data:")
    print(f"Project: {loaded_data['name']}")
    print(
        f"Start date: {loaded_data['start_date']} (type: {type(loaded_data['start_date'])})"
    )
    print(f"Due date: {loaded_data['due_date']}")
    print(f"Team: {loaded_data['team']}")

    # JSON schema validation (simple manual validation)
    print("\n\nManual schema validation:")
    required_fields = {"name", "start_date", "due_date", "budget"}
    actual_fields = set(loaded_data.keys())

    missing_fields = required_fields - actual_fields
    if missing_fields:
        print(f"  ❌ Missing fields: {missing_fields}")
    else:
        print("  ✅ All required fields present")

    # Check data types
    if isinstance(loaded_data["budget"], (int, float)):
        print("  ✅ Budget is numeric")
    else:
        print("  ❌ Budget should be numeric")

    # Clean up
    os.remove("project.json")


def exercise_5_csv_json_interoperability():
    """
    Convert between CSV and JSON formats.

    1. CSV to JSON conversion
    2. JSON to CSV conversion
    3. Data transformation during conversion
    """
    print("\n\nExercise 5: CSV ↔ JSON Interoperability")
    print("-" * 40)

    # Create sample CSV data
    student_data = [
        ["student_id", "name", "grade", "attendance"],
        ["S001", "Alice Johnson", "A", "95%"],
        ["S002", "Bob Smith", "B+", "88%"],
        ["S003", "Charlie Brown", "A-", "92%"],
        ["S004", "Diana Prince", "C", "75%"],
    ]

    # Write CSV
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(student_data)

    print("Created students.csv")

    # Convert CSV to JSON
    print("\nConverting CSV to JSON...")
    students_json = []

    with open("students.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Transform data during conversion
            student = {
                "id": row["student_id"],
                "name": row["name"],
                "grade": row["grade"],
                "attendance_percentage": float(row["attendance"].rstrip("%")),
                "status": "Excellent"
                if float(row["attendance"].rstrip("%")) >= 90
                else "Good",
            }
            students_json.append(student)

    # Save as JSON
    with open("students.json", "w") as jsonfile:
        json.dump(students_json, jsonfile, indent=2)

    print("Created students.json from CSV")

    # Display JSON
    with open("students.json", "r") as jsonfile:
        loaded_json = json.load(jsonfile)

    print("\nConverted JSON data:")
    for student in loaded_json:
        print(
            f"  {student['name']}: {student['grade']}, "
            f"{student['attendance_percentage']}%, {student['status']}"
        )

    # Convert JSON back to CSV
    print("\n\nConverting JSON back to CSV...")

    # Prepare CSV data
    csv_data = [["student_id", "name", "grade", "attendance_percentage", "status"]]

    for student in loaded_json:
        csv_data.append(
            [
                student["id"],
                student["name"],
                student["grade"],
                f"{student['attendance_percentage']}%",
                student["status"],
            ]
        )

    # Write back to CSV
    with open("students_converted.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

    print("Created students_converted.csv from JSON")

    # Compare files
    print("\nFile comparison:")
    print(f"  Original CSV: {os.path.getsize('students.csv')} bytes")
    print(f"  JSON: {os.path.getsize('students.json')} bytes")
    print(f"  Converted CSV: {os.path.getsize('students_converted.csv')} bytes")

    # Clean up
    for file in ["students.csv", "students.json", "students_converted.csv"]:
        os.remove(file)


def mini_project_data_export_import_system():
    """
    Data Export/Import System

    A system to export and import data between different formats:
    1. Export data to CSV or JSON
    2. Import data from CSV or JSON
    3. Convert between formats
    4. Validate and clean data
    """
    print("\n" + "=" * 60)
    print("MINI PROJECT: DATA EXPORT/IMPORT SYSTEM")
    print("=" * 60)

    # Sample data for the system
    sample_products = [
        {
            "id": 1,
            "name": "Laptop",
            "category": "Electronics",
            "price": 1200.99,
            "stock": 25,
        },
        {
            "id": 2,
            "name": "Desk Chair",
            "category": "Furniture",
            "price": 299.50,
            "stock": 15,
        },
        {
            "id": 3,
            "name": "Coffee Mug",
            "category": "Kitchen",
            "price": 15.99,
            "stock": 100,
        },
        {
            "id": 4,
            "name": "Notebook",
            "category": "Stationery",
            "price": 8.99,
            "stock": 200,
        },
    ]

    sample_customers = [
        {
            "customer_id": "C001",
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "orders": 5,
        },
        {
            "customer_id": "C002",
            "name": "Bob Smith",
            "email": "bob@example.com",
            "orders": 12,
        },
        {
            "customer_id": "C003",
            "name": "Charlie Brown",
            "email": "charlie@example.com",
            "orders": 3,
        },
    ]

    def export_data(data, filename, format_type):
        """Export data to specified format."""
        try:
            if format_type == "csv":
                if not data:
                    print("No data to export.")
                    return

                # Get fieldnames from first dictionary
                fieldnames = list(data[0].keys())

                with open(filename, "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)

                print(f"Exported {len(data)} records to {filename} (CSV)")

            elif format_type == "json":
                with open(filename, "w") as jsonfile:
                    json.dump(data, jsonfile, indent=2)

                print(f"Exported {len(data)} records to {filename} (JSON)")

            else:
                print(f"Unsupported format: {format_type}")

        except Exception as e:
            print(f"Export failed: {e}")

    def import_data(filename):
        """Import data from file (auto-detect format)."""
        if not os.path.exists(filename):
            print(f"File {filename} not found.")
            return None

        try:
            # Detect format by extension
            if filename.endswith(".csv"):
                with open(filename, "r") as csvfile:
                    reader = csv.DictReader(csvfile)
                    data = list(reader)

                print(f"Imported {len(data)} records from {filename} (CSV)")
                return data

            elif filename.endswith(".json"):
                with open(filename, "r") as jsonfile:
                    data = json.load(jsonfile)

                print(f"Imported {len(data)} records from {filename} (JSON)")
                return data

            else:
                print(f"Unsupported file format: {filename}")
                return None

        except Exception as e:
            print(f"Import failed: {e}")
            return None

    def convert_format(input_file, output_file):
        """Convert data from one format to another."""
        data = import_data(input_file)
        if data is None:
            return

        # Determine output format
        if output_file.endswith(".csv"):
            format_type = "csv"
        elif output_file.endswith(".json"):
            format_type = "json"
        else:
            print(f"Unknown output format: {output_file}")
            return

        export_data(data, output_file, format_type)
        print(f"Converted {input_file} to {output_file}")

    def validate_data(data):
        """Validate imported data."""
        if not data:
            print("No data to validate.")
            return

        print(f"\nValidating {len(data)} records...")

        issues = 0

        for i, record in enumerate(data, 1):
            # Check if record is a dictionary
            if not isinstance(record, dict):
                print(f"  Record {i}: Not a dictionary")
                issues += 1
                continue

            # Check for required fields (example)
            if "id" in record or "customer_id" in record:
                pass  # Has some kind of ID
            else:
                print(f"  Record {i}: Missing ID field")
                issues += 1

        if issues == 0:
            print("  ✅ All records valid")
        else:
            print(f"  ⚠️  Found {issues} issues")

    def display_data(data, limit=10):
        """Display data in a readable format."""
        if not data:
            print("No data to display.")
            return

        print(f"\nDisplaying first {min(limit, len(data))} records:")

        for i, record in enumerate(data[:limit], 1):
            print(f"\nRecord {i}:")
            for key, value in record.items():
                print(f"  {key}: {value}")

    while True:
        print("\n" + "-" * 60)
        print("DATA EXPORT/IMPORT SYSTEM")
        print("-" * 60)
        print("1. Export sample products data")
        print("2. Export sample customers data")
        print("3. Import data from file")
        print("4. Convert between formats")
        print("5. Validate imported data")
        print("6. Display imported data")
        print("7. Exit")
        print("-" * 60)

        choice = input("Select option (1-7): ")

        if choice == "1":
            filename = input("Enter filename (e.g., products.csv or products.json): ")
            format_type = "csv" if filename.endswith(".csv") else "json"
            export_data(sample_products, filename, format_type)

        elif choice == "2":
            filename = input("Enter filename (e.g., customers.csv or customers.json): ")
            format_type = "csv" if filename.endswith(".csv") else "json"
            export_data(sample_customers, filename, format_type)

        elif choice == "3":
            filename = input("Enter filename to import: ")
            imported_data = import_data(filename)
            if imported_data:
                # Store for later use
                globals()["current_data"] = imported_data

        elif choice == "4":
            input_file = input("Enter input filename: ")
            output_file = input("Enter output filename: ")
            convert_format(input_file, output_file)

        elif choice == "5":
            if "current_data" in globals():
                validate_data(globals()["current_data"])
            else:
                print("No data loaded. Please import data first.")

        elif choice == "6":
            if "current_data" in globals():
                display_data(globals()["current_data"])
            else:
                print("No data loaded. Please import data first.")

        elif choice == "7":
            # Clean up any files created
            for file in [
                "products.csv",
                "products.json",
                "customers.csv",
                "customers.json",
            ]:
                if os.path.exists(file):
                    os.remove(file)
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")


def run_all_exercises():
    """Run all Day 23 exercises."""
    print("=" * 60)
    print("Week 4, Day 23: CSV & JSON")
    print("=" * 60)

    print("\nThis day covers working with CSV and JSON file formats,")
    print("including reading, writing, and converting between them.")
    print("\nRunning exercises...")

    exercise_1_csv_basics()
    exercise_2_csv_advanced()
    exercise_3_json_basics()
    exercise_4_json_advanced()
    exercise_5_csv_json_interoperability()

    print("\n" + "=" * 60)
    print("Mini Project: Data Export/Import System")
    print("=" * 60)
    mini_project_data_export_import_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 23 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
