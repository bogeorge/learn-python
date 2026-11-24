import sys

"""
Week 2, Day 11: Tuples & Dictionaries

Exercises to practice tuples (immutable sequences), dictionaries (key-value pairs),
dictionary methods, and converting between data structures.
"""


def exercise_1_tuples_basics():
    """
    Practice with tuple basics.

    1. Create tuples and access elements
    2. Demonstrate tuple immutability
    3. Use tuple packing and unpacking
    """

    # Creating tuples
    empty_tuple = ()
    single_element = (42,)  # Note the comma!
    multi_element = (1, 2, 3, 4, 5)
    mixed_tuple = ("apple", 3.14, True, 42)

    print("Tuple basics:")
    print(f"  Empty tuple: {empty_tuple}")
    print(f"  Single element: {single_element}")
    print(f"  Multi-element: {multi_element}")
    print(f"  Mixed tuple: {mixed_tuple}")

    # Accessing elements
    print("\n  Accessing elements:")
    print(f"    First element: {mixed_tuple[0]}")
    print(f"    Last element: {mixed_tuple[-1]}")
    print(f"    Slice [1:3]: {mixed_tuple[1:3]}")

    # Tuple immutability demonstration
    print("\n  Tuple immutability:")
    try:
        # This will raise an error
        mixed_tuple[0] = "banana"
    except TypeError as e:
        print(f"    Error: {e}")

    # Tuple packing and unpacking
    coordinates = (10, 20, 30)  # Packing
    x, y, z = coordinates  # Unpacking

    print(f"\n  Packed coordinates: {coordinates}")
    print(f"    Unpacked: x={x}, y={y}, z={z}")

    # Swapping values using tuples
    a = 5
    b = 10
    print(f"\n  Before swap: a={a}, b={b}")
    a, b = b, a  # Tuple packing/unpacking for swap
    print(f"  After swap: a={a}, b={b}")

    # Returning multiple values from function
    def get_min_max(numbers):
        """Return min and max of a list."""
        return min(numbers), max(numbers)

    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    minimum, maximum = get_min_max(nums)
    print(f"\n  Numbers: {nums}")
    print(f"  Min: {minimum}, Max: {maximum}")


def exercise_2_dictionaries_basics():
    """
    Practice with dictionary basics.

    1. Create dictionaries using different methods
    2. Access, add, modify, and delete items
    3. Use dictionary methods
    """

    # Creating dictionaries
    empty_dict = {}
    person = {"name": "Alice", "age": 30, "city": "New York"}
    numbers = dict(one=1, two=2, three=3)
    from_list = dict([("a", 1), ("b", 2), ("c", 3)])

    print("Dictionary basics:")
    print(f"  Empty dict: {empty_dict}")
    print(f"  Person: {person}")
    print(f"  Numbers: {numbers}")
    print(f"  From list: {from_list}")

    # Accessing elements
    print("\n  Accessing elements:")
    print(f"    person['name']: {person['name']}")
    print(f"    person.get('age'): {person.get('age')}")
    print(
        f"    person.get('occupation', 'Not specified'): "
        f"{person.get('occupation', 'Not specified')}"
    )

    # Adding and modifying
    person["occupation"] = "Engineer"
    person["age"] = 31
    print(f"\n  After modifications: {person}")

    # Deleting items
    removed_age = person.pop("age")
    print(f"  After pop('age') removed {removed_age}: {person}")

    del person["city"]
    print(f"  After del person['city']: {person}")

    # Dictionary methods
    print("\n  Dictionary methods:")
    print(f"    Keys: {list(person.keys())}")
    print(f"    Values: {list(person.values())}")
    print(f"    Items: {list(person.items())}")

    # Update method
    updates = {"age": 32, "hobbies": ["reading", "hiking"]}
    person.update(updates)
    print(f"\n  After update: {person}")


def exercise_3_dictionary_operations():
    """
    Practice dictionary operations and methods.

    1. Dictionary comprehension
    2. Nested dictionaries
    3. Merging dictionaries
    4. Dictionary views
    """

    # Dictionary comprehension
    squares = {x: x**2 for x in range(1, 6)}
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}

    print("Dictionary operations:")
    print(f"  Squares (1-5): {squares}")
    print(f"  Even squares (1-10): {even_squares}")

    # Nested dictionaries
    students = {
        "Alice": {
            "age": 20,
            "grades": {"math": 85, "science": 92, "english": 78},
            "hobbies": ["reading", "chess"],
        },
        "Bob": {
            "age": 21,
            "grades": {"math": 72, "science": 68, "english": 80},
            "hobbies": ["basketball", "gaming"],
        },
    }

    print("\n  Nested dictionary - students:")
    for name, info in students.items():
        print(f"    {name}: Age={info['age']}, Math grade={info['grades']['math']}")

    # Dictionary merging (Python 3.9+)
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    dict3 = {"d": 5}

    merged = {**dict1, **dict2, **dict3}
    print("\n  Merged dictionaries:")
    print(f"    dict1: {dict1}")
    print(f"    dict2: {dict2}")
    print(f"    dict3: {dict3}")
    print(f"    Merged: {merged}")

    # Dictionary views
    print("\n  Dictionary views:")
    keys_view = merged.keys()
    values_view = merged.values()
    items_view = merged.items()

    print(f"    Keys view: {keys_view}")
    print(f"    Values view: {values_view}")
    print(f"    Items view: {items_view}")

    # Add to merged and see views update
    merged["e"] = 6
    print(f"    After adding 'e': keys={list(keys_view)}")


def exercise_4_converting_data_structures():
    """
    Convert between different data structures.

    1. Convert lists to dictionaries and vice versa
    2. Convert tuples to dictionaries
    3. Convert between sets and lists
    """

    # List of tuples to dictionary
    pairs = [("name", "Alice"), ("age", 30), ("city", "New York")]
    dict_from_pairs = dict(pairs)

    print("Converting data structures:")
    print(f"  List of tuples: {pairs}")
    print(f"  Converted to dict: {dict_from_pairs}")

    # Dictionary to list of tuples
    dict_to_pairs = list(dict_from_pairs.items())
    print(f"\n  Dict back to list of tuples: {dict_to_pairs}")

    # Two lists to dictionary
    keys = ["a", "b", "c", "d"]
    values = [1, 2, 3, 4]
    dict_from_zip = dict(zip(keys, values))

    print(f"\n  Keys: {keys}")
    print(f"  Values: {values}")
    print(f"  Zipped to dict: {dict_from_zip}")

    # List comprehension from dictionary
    items = [(k, v) for k, v in dict_from_zip.items()]
    values_list = [v for v in dict_from_zip.values()]

    print(f"\n  Items list: {items}")
    print(f"  Values list: {values_list}")

    # Set operations with conversion
    list1 = [1, 2, 2, 3, 4, 4, 5]
    list2 = [4, 5, 6, 6, 7, 8]

    set1 = set(list1)
    set2 = set(list2)

    print(f"\n  List1: {list1}")
    print(f"  List2: {list2}")
    print(f"  Set1: {set1}")
    print(f"  Set2: {set2}")
    print(f"  Union: {set1 | set2}")
    print(f"  Intersection: {set1 & set2}")
    print(f"  Difference (list1 - list2): {set1 - set2}")


def exercise_5_dictionary_advanced():
    """
    Advanced dictionary techniques.

    1. Default dictionaries
    2. Counter objects
    3. Ordered dictionaries
    4. Dictionary with complex keys
    """
    from collections import Counter, OrderedDict, defaultdict

    # Default dictionary
    print("Advanced dictionary techniques:")

    word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_count = defaultdict(int)

    for word in word_list:
        word_count[word] += 1

    print(f"  Word list: {word_list}")
    print(f"  Word count (defaultdict): {dict(word_count)}")

    # Using Counter
    counter = Counter(word_list)
    print(f"  Word count (Counter): {counter}")
    print(f"  Most common: {counter.most_common(2)}")

    # Grouping with defaultdict
    students_by_grade = defaultdict(list)

    student_grades = [
        ("Alice", "A"),
        ("Bob", "B"),
        ("Charlie", "A"),
        ("Diana", "C"),
        ("Eve", "A"),
        ("Frank", "B"),
    ]

    for name, grade in student_grades:
        students_by_grade[grade].append(name)

    print(f"\n  Students by grade: {dict(students_by_grade)}")

    # Ordered dictionary
    ordered = OrderedDict()
    ordered["z"] = 26
    ordered["a"] = 1
    ordered["m"] = 13

    print("\n  OrderedDict maintains insertion order:")
    for k, v in ordered.items():
        print(f"    {k}: {v}")

    # Dictionary with tuple keys
    coordinate_map = {}
    coordinate_map[(0, 0)] = "Origin"
    coordinate_map[(1, 2)] = "Point A"
    coordinate_map[(3, 4)] = "Point B"

    print("\n  Dictionary with tuple keys:")
    for coord, label in coordinate_map.items():
        print(f"    {coord} -> {label}")


def mini_project_contact_information_system():
    """
    Contact Information System

    Manage contact information using dictionaries and tuples.

    Features:
    1. Add/remove/update contacts
    2. Search for contacts
    3. Group contacts by category
    4. Save/load contacts (simulated)
    """
    print("=" * 50)
    print("CONTACT INFORMATION SYSTEM")
    print("=" * 50)

    # Sample contacts
    contacts = {
        "alice@email.com": {
            "name": "Alice Smith",
            "phone": "555-0101",
            "address": "123 Main St, New York, NY",
            "category": "Friends",
        },
        "bob.johnson@work.com": {
            "name": "Bob Johnson",
            "phone": "555-0202",
            "address": "456 Oak Ave, Chicago, IL",
            "category": "Work",
        },
        "charlie.brown@email.com": {
            "name": "Charlie Brown",
            "phone": "555-0303",
            "address": "789 Pine Rd, Boston, MA",
            "category": "Family",
        },
    }

    def display_contact(email):
        """Display a single contact."""
        if email in contacts:
            contact = contacts[email]
            print(f"\nEmail: {email}")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Address: {contact['address']}")
            print(f"  Category: {contact['category']}")
        else:
            print(f"Contact '{email}' not found.")

    def add_contact():
        """Add a new contact."""
        print("\nAdd New Contact:")
        email = input("Email: ")

        if email in contacts:
            print(f"Contact '{email}' already exists.")
            return

        name = input("Name: ")
        phone = input("Phone: ")
        address = input("Address: ")
        category = input("Category: ")

        contacts[email] = {
            "name": name,
            "phone": phone,
            "address": address,
            "category": category,
        }
        print(f"Contact '{email}' added successfully.")

    def search_contacts():
        """Search contacts by various criteria."""
        print("\nSearch Options:")
        print("1. Search by name")
        print("2. Search by email")
        print("3. Search by category")
        print("4. Search by phone")

        choice = input("Enter search option (1-4): ")

        if choice == "1":
            search_term = input("Enter name to search: ").lower()
            results = []
            for email, contact in contacts.items():
                if search_term in contact["name"].lower():
                    results.append((email, contact))

        elif choice == "2":
            search_term = input("Enter email to search: ").lower()
            results = []
            for email, contact in contacts.items():
                if search_term in email.lower():
                    results.append((email, contact))

        elif choice == "3":
            search_term = input("Enter category to search: ").lower()
            results = []
            for email, contact in contacts.items():
                if search_term in contact["category"].lower():
                    results.append((email, contact))

        elif choice == "4":
            search_term = input("Enter phone to search: ")
            results = []
            for email, contact in contacts.items():
                if search_term in contact["phone"]:
                    results.append((email, contact))

        else:
            print("Invalid choice.")
            return

        if results:
            print(f"\nFound {len(results)} contact(s):")
            for email, contact in results:
                print(f"  {email}: {contact['name']} ({contact['category']})")
        else:
            print("No contacts found.")

    def group_by_category():
        """Group contacts by category."""
        categories = {}

        for email, contact in contacts.items():
            category = contact["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append({"email": email, "name": contact["name"]})

        print("\nContacts by category:")
        for category, contact_list in categories.items():
            print(f"\n{category} ({len(contact_list)} contacts):")
            for contact in contact_list:
                print(f"  {contact['name']} - {contact['email']}")

    print(f"Current contacts: {len(contacts)}")

    while True:
        print("\nMenu:")
        print("1. View all contacts")
        print("2. Add new contact")
        print("3. View contact details")
        print("4. Search contacts")
        print("5. Group by category")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("\nEnter your choice (0-6): ")

        if choice == "0":
            print("Exiting Contact System. Goodbye!")
            break

        elif choice == "1":
            print("\nAll Contacts:")
            for email in contacts:
                print(f"  {email}: {contacts[email]['name']}")

        elif choice == "2":
            add_contact()

        elif choice == "3":
            email = input("Enter email to view: ")
            display_contact(email)

        elif choice == "4":
            search_contacts()

        elif choice == "5":
            group_by_category()

        elif choice == "6":
            email = input("Enter email to delete: ")
            if email in contacts:
                del contacts[email]
                print(f"Contact '{email}' deleted.")
            else:
                print(f"Contact '{email}' not found.")

        else:
            print("Invalid choice. Please enter 0-6.")


def run_all_exercises():
    """Run all Day 11 exercises."""
    print("=" * 60)
    print("Week 2, Day 11: Tuples & Dictionaries")
    print("=" * 60)

    print("\n--- Exercise 1: Tuples Basics ---")
    exercise_1_tuples_basics()

    print("\n--- Exercise 2: Dictionaries Basics ---")
    exercise_2_dictionaries_basics()

    print("\n--- Exercise 3: Dictionary Operations ---")
    exercise_3_dictionary_operations()

    print("\n--- Exercise 4: Converting Data Structures ---")
    exercise_4_converting_data_structures()

    print("\n--- Exercise 5: Dictionary Advanced ---")
    exercise_5_dictionary_advanced()

    print("\n" + "=" * 60)
    print("Mini Project: Contact Information System")
    print("=" * 60)
    mini_project_contact_information_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 11 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
