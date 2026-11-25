import os
import sys

"""
Week 4, Day 22: File I/O Basics

Exercises to practice reading from and writing to files.
"""


def exercise_1_read_text_file():
    """
    Read content from a text file.

    1. Create a sample text file with some content
    2. Read the entire file content
    3. Read line by line
    4. Count the number of lines, words, and characters
    """
    print("Exercise 1: Reading Text Files")
    print("-" * 40)

    # Create a sample file
    sample_content = """This is a sample text file.
It contains multiple lines.
We can use this to practice file I/O.
File handling is important for many applications."""

    with open("sample.txt", "w") as f:
        f.write(sample_content)

    # Read entire file
    with open("sample.txt", "r") as f:
        content = f.read()

    print("Entire file content:")
    print(content)
    print()

    # Read line by line
    with open("sample.txt", "r") as f:
        lines = f.readlines()

    print("Line by line:")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

    # Count statistics
    with open("sample.txt", "r") as f:
        content = f.read()

    line_count = len(content.splitlines())
    word_count = len(content.split())
    char_count = len(content)

    print("\nStatistics:")
    print(f"  Lines: {line_count}")
    print(f"  Words: {word_count}")
    print(f"  Characters: {char_count}")

    # Clean up
    os.remove("sample.txt")


def exercise_2_write_text_file():
    """
    Write content to text files.

    1. Write different types of data to a file
    2. Append to an existing file
    3. Handle different writing modes
    """
    print("\n\nExercise 2: Writing Text Files")
    print("-" * 40)

    # Write new file
    data = [
        "Alice,30,Engineer",
        "Bob,25,Designer",
        "Charlie,35,Manager",
        "Diana,28,Developer",
    ]

    with open("employees.csv", "w") as f:
        f.write("Name,Age,Position\n")
        f.writelines(f"{entry}\n" for entry in data)

    print("Created employees.csv with data:")
    with open("employees.csv", "r") as f:
        print(f.read())

    # Append to file
    new_employees = ["Eve,32,Analyst", "Frank,40,Director"]

    with open("employees.csv", "a") as f:
        f.writelines(f"{entry}\n" for entry in new_employees)

    print("\nAfter appending:")
    with open("employees.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(f"  {line.strip()}")

    # Write with different modes
    print("\n\nFile modes demonstration:")

    # 'x' mode - exclusive creation (fails if file exists)
    try:
        with open("new_file.txt", "x") as f:
            f.write("This file was created with 'x' mode")
        print("  Created new_file.txt with 'x' mode")
    except FileExistsError:
        print("  File already exists (can't use 'x' mode)")

    # 'w+' mode - write and read
    with open("wplus_demo.txt", "w+") as f:
        f.write("Written with w+ mode\n")
        f.write("Second line\n")

        # Go back to beginning and read
        f.seek(0)
        content = f.read()
        print("  Content written and read with 'w+' mode:")
        print(f"  {content}")

    # Clean up
    os.remove("employees.csv")
    if os.path.exists("new_file.txt"):
        os.remove("new_file.txt")
    os.remove("wplus_demo.txt")


def exercise_3_binary_files():
    """
    Work with binary files.

    1. Write binary data to a file
    2. Read binary data from a file
    3. Work with different binary formats
    """
    print("\n\nExercise 3: Binary Files")
    print("-" * 40)

    # Write binary data
    binary_data = bytes(range(256))  # 0-255

    with open("data.bin", "wb") as f:
        f.write(binary_data)

    print(f"Wrote {len(binary_data)} bytes to data.bin")

    # Read binary data
    with open("data.bin", "rb") as f:
        read_data = f.read()

    print(f"Read {len(read_data)} bytes from data.bin")
    print(f"First 10 bytes: {list(read_data[:10])}")
    print(f"Last 10 bytes: {list(read_data[-10:])}")

    # Demonstrate reading specific parts
    with open("data.bin", "rb") as f:
        f.seek(100)  # Go to byte 100
        byte_100 = f.read(1)  # Read 1 byte
        f.seek(200)
        byte_200 = f.read(1)

    print(f"Byte at position 100: {next(iter(byte_100))}")
    print(f"Byte at position 200: {next(iter(byte_200))}")

    # Clean up
    os.remove("data.bin")


def exercise_4_file_exceptions():
    """
    Handle file-related exceptions.

    1. FileNotFoundError
    2. PermissionError
    3. IsADirectoryError
    4. Using try-except-finally
    """
    print("\n\nExercise 4: File Exceptions")
    print("-" * 40)

    # FileNotFoundError
    print("1. Handling FileNotFoundError:")
    try:
        with open("nonexistent.txt", "r") as f:
            f.read()
    except FileNotFoundError:
        print("  File doesn't exist. Creating it...")
        with open("nonexistent.txt", "w") as f:
            f.write("Now I exist!")

    # PermissionError (simulated)
    print("\n2. Handling PermissionError:")
    try:
        # Try to create a file in a protected location
        protected_path = "/etc/test.txt"
        with open(protected_path, "w") as f:
            f.write("test")
    except PermissionError:
        print("  Permission denied - can't write to protected location")
    except OSError as e:
        # Other file-system errors (e.g. read-only disk) are OSError subclasses
        print(f"  Other error: {type(e).__name__}")

    # IsADirectoryError
    print("\n3. Handling IsADirectoryError:")
    try:
        # Create a directory
        os.makedirs("test_dir", exist_ok=True)
        # Try to open directory as file
        with open("test_dir", "r") as f:
            f.read()
    except IsADirectoryError:
        print("  Can't open a directory as a file")

    # Using finally
    print("\n4. Using try-except-finally:")
    f = None
    try:
        with open("temp_file.txt", "w") as f:
            f.write("Some data")
        # Simulate an error
    except ZeroDivisionError:
        print("  Math error occurred")
    finally:
        if f:
            f.close()
            print("  File closed in finally block")

    # Clean up
    if os.path.exists("nonexistent.txt"):
        os.remove("nonexistent.txt")
    if os.path.exists("test_dir"):
        os.rmdir("test_dir")
    if os.path.exists("temp_file.txt"):
        os.remove("temp_file.txt")


def exercise_5_file_operations():
    """
    Perform file system operations.

    1. Check if file exists
    2. Get file information
    3. Rename files
    4. Delete files
    5. List directory contents
    """
    print("\n\nExercise 5: File Operations")
    print("-" * 40)

    # Create test files
    with open("test1.txt", "w") as f:
        f.write("Test file 1")

    with open("test2.txt", "w") as f:
        f.write("Test file 2")

    os.makedirs("test_subdir", exist_ok=True)
    with open("test_subdir/test3.txt", "w") as f:
        f.write("Test file 3 in subdirectory")

    # Check if file exists
    print("1. Check if files exist:")
    print(f"  test1.txt exists: {os.path.exists('test1.txt')}")
    print(f"  test4.txt exists: {os.path.exists('test4.txt')}")

    # Get file information
    print("\n2. File information:")
    if os.path.exists("test1.txt"):
        stats = os.stat("test1.txt")
        print(f"  test1.txt size: {stats.st_size} bytes")
        print(f"  Last modified: {stats.st_mtime}")
        print(f"  Is file: {os.path.isfile('test1.txt')}")
        print(f"  Is directory: {os.path.isdir('test1.txt')}")

    # Rename files
    print("\n3. Rename file:")
    if os.path.exists("test2.txt"):
        os.rename("test2.txt", "renamed_test.txt")
        print("  Renamed test2.txt to renamed_test.txt")
        print(f"  renamed_test.txt exists: {os.path.exists('renamed_test.txt')}")

    # List directory contents
    print("\n4. List directory contents:")
    print("  Current directory:")
    for item in os.listdir("."):
        if os.path.isfile(item):
            print(f"    File: {item}")
        elif os.path.isdir(item):
            print(f"    Directory: {item}")

    # Clean up
    print("\n5. Clean up:")
    for file in ["test1.txt", "renamed_test.txt"]:
        if os.path.exists(file):
            os.remove(file)
            print(f"  Removed {file}")

    if os.path.exists("test_subdir"):
        for file in os.listdir("test_subdir"):
            os.remove(os.path.join("test_subdir", file))
        os.rmdir("test_subdir")
        print("  Removed test_subdir")


def mini_project_simple_text_editor():
    """
    Simple Text Editor

    A basic text editor with the following features:
    1. Create new text files
    2. Open existing files
    3. Edit and save files
    4. Basic text operations (count words/lines)
    5. Find and replace text
    """
    print("\n" + "=" * 60)
    print("MINI PROJECT: SIMPLE TEXT EDITOR")
    print("=" * 60)

    def create_file():
        """Create a new text file."""
        filename = input("Enter filename to create: ")
        if os.path.exists(filename):
            overwrite = input(f"{filename} already exists. Overwrite? (y/n): ")
            if overwrite.lower() != "y":
                print("Cancelled.")
                return

        print("Enter your text (type 'END' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line == "END":
                break
            lines.append(line)

        with open(filename, "w") as f:
            f.write("\n".join(lines))

        print(f"File '{filename}' created successfully.")

    def open_file():
        """Open and display a text file."""
        filename = input("Enter filename to open: ")
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return

        try:
            with open(filename, "r") as f:
                content = f.read()

            print(f"\n=== Contents of '{filename}' ===")
            print(content)
            print("=" * (len(filename) + 30))

            # Show statistics
            lines = content.splitlines()
            words = content.split()
            chars = len(content)

            print("\nStatistics:")
            print(f"  Lines: {len(lines)}")
            print(f"  Words: {len(words)}")
            print(f"  Characters: {chars}")

            return filename, content
        except (OSError, UnicodeDecodeError) as e:
            # UnicodeDecodeError: the file isn't text (e.g. an image)
            print(f"Error reading file: {e}")
            return None, None

    def edit_file():
        """Edit an existing file."""
        filename, content = open_file()
        if not filename:
            return

        print("\nEdit options:")
        print("  1. Append text")
        print("  2. Replace entire file")
        print("  3. Find and replace text")
        choice = input("Select option (1-3): ")

        if choice == "1":
            print("Enter text to append (type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)

            with open(filename, "a") as f:
                if lines:
                    f.write("\n" + "\n".join(lines))
            print("Text appended.")

        elif choice == "2":
            print("Enter new content (type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)

            with open(filename, "w") as f:
                f.write("\n".join(lines))
            print("File replaced.")

        elif choice == "3":
            find_text = input("Text to find: ")
            replace_text = input("Replace with: ")

            with open(filename, "r") as f:
                content = f.read()

            if find_text in content:
                new_content = content.replace(find_text, replace_text)

                with open(filename, "w") as f:
                    f.write(new_content)
                print(f"Replaced '{find_text}' with '{replace_text}'")
            else:
                print(f"Text '{find_text}' not found.")

    def delete_file():
        """Delete a text file."""
        filename = input("Enter filename to delete: ")
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return

        confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ")
        if confirm.lower() == "y":
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print("Deletion cancelled.")

    while True:
        print("\n" + "-" * 40)
        print("SIMPLE TEXT EDITOR")
        print("-" * 40)
        print("1. Create new file")
        print("2. Open file")
        print("3. Edit file")
        print("4. Delete file")
        print("5. Exit")
        print("-" * 40)

        choice = input("Select option (1-5): ")

        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            edit_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("Exiting text editor.")
            break
        else:
            print("Invalid choice. Please try again.")


def run_all_exercises():
    """Run all Day 22 exercises."""
    print("=" * 60)
    print("Week 4, Day 22: File I/O Basics")
    print("=" * 60)

    print("\nThis day covers reading from and writing to files,")
    print("handling binary data, and working with the file system.")
    print("\nRunning exercises...")

    exercise_1_read_text_file()
    exercise_2_write_text_file()
    exercise_3_binary_files()
    exercise_4_file_exceptions()
    exercise_5_file_operations()

    print("\n" + "=" * 60)
    print("Mini Project: Simple Text Editor")
    print("=" * 60)
    mini_project_simple_text_editor()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 22 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
