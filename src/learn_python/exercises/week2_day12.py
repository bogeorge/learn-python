import sys

"""
Week 2, Day 12: Sets & Strings

Exercises to practice set operations (union, intersection, difference),
string methods, formatting, and text processing.
"""


def exercise_1_set_operations():
    """
    Practice set operations.

    1. Create sets and use basic operations
    2. Demonstrate union, intersection, difference
    3. Use set methods
    """

    # Creating sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {5, 6, 9, 10}

    print("Set operations:")
    print(f"  Set1: {set1}")
    print(f"  Set2: {set2}")
    print(f"  Set3: {set3}")

    # Basic set operations
    union_12 = set1 | set2  # or set1.union(set2)
    intersection_12 = set1 & set2  # or set1.intersection(set2)
    difference_12 = set1 - set2  # or set1.difference(set2)
    symmetric_diff = set1 ^ set2  # or set1.symmetric_difference(set2)

    print(f"\n  Union (set1 | set2): {union_12}")
    print(f"  Intersection (set1 & set2): {intersection_12}")
    print(f"  Difference (set1 - set2): {difference_12}")
    print(f"  Symmetric difference (set1 ^ set2): {symmetric_diff}")

    # Multiple set operations
    all_union = set1 | set2 | set3
    all_intersection = set1 & set2 & set3
    print(f"\n  Union of all sets: {all_union}")
    print(f"  Intersection of all sets: {all_intersection}")

    # Set methods
    print("\n  Set methods:")
    set1.add(6)
    print(f"    After add(6): {set1}")

    set1.remove(1)  # Raises KeyError if not present
    print(f"    After remove(1): {set1}")

    set1.discard(10)  # Doesn't raise error if not present
    print(f"    After discard(10): {set1}")

    popped = set1.pop()
    print(f"    After pop() removed {popped}: {set1}")

    # Subset and superset
    small_set = {4, 5}
    print(f"\n  Small set: {small_set}")
    print(f"    small_set ⊆ set1: {small_set.issubset(set1)}")
    print(f"    set1 ⊇ small_set: {set1.issuperset(small_set)}")
    print(f"    set1 disjoint with {9, 10}: {set1.isdisjoint({9, 10})}")


def exercise_2_string_methods():
    """
    Practice string methods.

    1. Use various string manipulation methods
    2. Demonstrate string searching and checking
    3. Practice string transformations
    """

    text = "  Hello, Python World!  "
    sentence = "the quick brown fox jumps over the lazy dog"

    print("String methods:")
    print(f"  Original text: '{text}'")
    print(f"  Original sentence: '{sentence}'")

    # Basic string methods
    print(f"\n  Basic methods:")
    print(f"    strip(): '{text.strip()}'")
    print(f"    lower(): '{text.lower()}'")
    print(f"    upper(): '{text.upper()}'")
    print(f"    title(): '{sentence.title()}'")
    print(f"    capitalize(): '{sentence.capitalize()}'")

    # String searching
    print(f"\n  Searching:")
    print(f"    find('Python'): {text.find('Python')}")
    print(f"    find('Java'): {text.find('Java')}")  # Returns -1
    print(f"    index('World'): {text.index('World')}")
    print(f"    count('o'): {text.count('o')}")
    print(f"    startswith('Hello'): {text.strip().startswith('Hello')}")
    print(f"    endswith('World!'): {text.strip().endswith('World!')}")

    # String checking
    print(f"\n  Checking:")
    alpha_text = "Hello"
    numeric_text = "12345"
    mixed_text = "Hello123"

    print(f"    '{alpha_text}'.isalpha(): {alpha_text.isalpha()}")
    print(f"    '{numeric_text}'.isdigit(): {numeric_text.isdigit()}")
    print(f"    '{mixed_text}'.isalnum(): {mixed_text.isalnum()}")
    print(f"    'Hello World'.isspace(): {'   '.isspace()}")

    # String transformations
    print(f"\n  Transformations:")
    words = sentence.split()
    print(f"    split(): {words}")
    print(f"    join(): {'-'.join(words)}")

    replaced = sentence.replace("the", "a")
    print(f"    replace('the', 'a'): {replaced}")

    print(f"    partition('fox'): {sentence.partition('fox')}")
    print(f"    rpartition('the'): {sentence.rpartition('the')}")


def exercise_3_string_formatting():
    """
    Practice different string formatting methods.

    1. f-strings (Python 3.6+)
    2. str.format() method
    3. Old-style % formatting
    4. Advanced formatting options
    """

    name = "Alice"
    age = 30
    salary = 75000.50
    pi = 3.141592653589793

    print("String formatting:")

    # f-strings (modern, preferred)
    print(f"  f-strings:")
    print(f"    Basic: Hello, {name}!")
    print(f"    Expression: In 5 years, {name} will be {age + 5} years old.")
    print(f"    Formatting: Salary: ${salary:,.2f}")
    print(f"    Alignment: |{name:<10}| |{name:>10}| |{name:^10}|")

    # str.format() method
    print(f"\n  str.format():")
    print("    Basic: Hello, {}!".format(name))
    print("    Positional: {0} is {1} years old.".format(name, age))
    print("    Named: {n} earns ${s:,.2f}".format(n=name, s=salary))
    print("    Formatting: π = {:.4f}".format(pi))

    # Old-style % formatting
    print(f"\n  % formatting:")
    print("    Basic: Hello, %s!" % name)
    print("    Multiple: %s is %d years old." % (name, age))
    print("    Float: π = %.3f" % pi)

    # Advanced formatting examples
    print(f"\n  Advanced formatting:")

    # Padding and alignment
    for i in range(1, 6):
        print(f"    Number {i:02d}: {i * i:3d} {i * i * i:4d}")

    # Percentage formatting
    completion = 0.756
    print(f"    Progress: {completion:.1%}")

    # Scientific notation
    large_number = 123456789
    print(f"    Scientific: {large_number:.2e}")

    # Binary, octal, hexadecimal
    num = 255
    print(f"    Binary: {num:#b}")
    print(f"    Octal: {num:#o}")
    print(f"    Hex: {num:#x}")


def exercise_4_text_processing():
    """
    Practice text processing techniques.

    1. String slicing and manipulation
    2. Working with multi-line strings
    3. Character encoding
    4. Regular expressions basics
    """
    import re

    text = "Python programming is fun and powerful. Python is used for web development, data science, and automation."

    print("Text processing:")
    print(f"  Original text: {text}")

    # String slicing
    print(f"\n  Slicing:")
    print(f"    First 10 chars: '{text[:10]}'")
    print(f"    Last 15 chars: '{text[-15:]}'")
    print(f"    Every other char: '{text[::2]}'")
    print(f"    Reverse: '{text[::-1]}'")

    # Multi-line strings
    multiline = """This is a multi-line string.
    It preserves line breaks and indentation.
    Useful for documentation and formatted output."""

    print(f"\n  Multi-line string:")
    print(multiline)

    # Line splitting and joining
    lines = multiline.splitlines()
    print(f"\n  Split into lines ({len(lines)} lines):")
    for i, line in enumerate(lines, 1):
        print(f"    Line {i}: '{line.strip()}'")

    # Character encoding
    print(f"\n  Character encoding:")
    encoded = text.encode("utf-8")
    print(f"    UTF-8 encoded: {encoded[:20]}...")
    decoded = encoded.decode("utf-8")
    print(f"    Decoded (first 30 chars): '{decoded[:30]}'")

    # Regular expressions basics
    print(f"\n  Regular expressions:")

    # Find all occurrences of "Python"
    python_matches = re.findall(r"Python", text, re.IGNORECASE)
    print(f"    Find 'Python': {python_matches}")

    # Split by punctuation
    sentences = re.split(r"[.!?]", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    print(f"    Sentences: {sentences}")

    # Search for patterns
    pattern = r"\b\w{4,}\b"  # Words with 4+ letters
    long_words = re.findall(pattern, text)
    print(f"    Words with 4+ letters: {long_words}")

    # Replace using regex
    replaced = re.sub(r"\bPython\b", "JavaScript", text)
    print(f"    Replace 'Python' with 'JavaScript': {replaced}")


def exercise_5_set_and_string_combinations():
    """
    Combine set operations with string processing.

    1. Find unique characters in strings
    2. Compare strings using sets
    3. Text analysis with sets
    """

    text1 = "hello world"
    text2 = "world of python"
    pangram = "the quick brown fox jumps over the lazy dog"

    print("Set and string combinations:")
    print(f"  Text1: '{text1}'")
    print(f"  Text2: '{text2}'")
    print(f"  Pangram: '{pangram}'")

    # Unique characters
    chars1 = set(text1)
    chars2 = set(text2)

    print(f"\n  Unique characters in text1: {sorted(chars1)}")
    print(f"  Unique characters in text2: {sorted(chars2)}")

    # Character comparisons
    common_chars = chars1 & chars2
    unique_to_1 = chars1 - chars2
    unique_to_2 = chars2 - chars1
    all_chars = chars1 | chars2

    print(f"\n  Common characters: {sorted(common_chars)}")
    print(f"  Unique to text1: {sorted(unique_to_1)}")
    print(f"  Unique to text2: {sorted(unique_to_2)}")
    print(f"  All characters: {sorted(all_chars)}")

    # Check if string uses all letters
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    pangram_chars = set(pangram.replace(" ", "").lower())

    missing_letters = alphabet - pangram_chars
    print(f"\n  Pangram analysis:")
    print(f"    Letters in pangram: {len(pangram_chars)}")
    print(f"    Missing letters: {sorted(missing_letters)}")
    print(f"    Is perfect pangram? {len(missing_letters) == 0}")

    # Word analysis using sets
    words1 = set(text1.split())
    words2 = set(text2.split())

    print(f"\n  Word analysis:")
    print(f"    Words in text1: {words1}")
    print(f"    Words in text2: {words2}")
    print(f"    Common words: {words1 & words2}")
    print(f"    Unique words in text1: {words1 - words2}")

    # Remove duplicate characters from string
    duplicate_text = "programming"
    unique_chars = "".join(sorted(set(duplicate_text)))
    print(f"\n  Remove duplicates from '{duplicate_text}': '{unique_chars}'")


def mini_project_word_counter():
    """
    Word Counter with Set Operations

    Analyze text using string methods and set operations.

    Features:
    1. Count words, characters, sentences
    2. Find unique words
    3. Word frequency analysis
    4. Set operations on text
    """
    import string

    print("=" * 50)
    print("WORD COUNTER WITH SET OPERATIONS")
    print("=" * 50)

    sample_text = """
    Python is an interpreted, high-level, general-purpose programming language.
    Created by Guido van Rossum and first released in 1991, Python's design philosophy 
    emphasizes code readability with its notable use of significant whitespace.
    Its language constructs and object-oriented approach aim to help programmers 
    write clear, logical code for small and large-scale projects.
    
    Python is dynamically typed and garbage-collected. It supports multiple 
    programming paradigms, including structured (particularly procedural), 
    object-oriented, and functional programming. Python is often described as a 
    "batteries included" language due to its comprehensive standard library.
    """

    def clean_text(text):
        """Clean text by removing punctuation and converting to lowercase."""
        # Remove punctuation
        translator = str.maketrans("", "", string.punctuation)
        text = text.translate(translator)

        # Convert to lowercase
        text = text.lower()

        return text

    def analyze_text(text):
        """Perform comprehensive text analysis."""
        # Clean the text
        cleaned = clean_text(text)

        # Basic statistics
        characters = len(text)
        characters_no_spaces = len(text.replace(" ", "").replace("\n", ""))
        words = cleaned.split()
        sentences = text.count(".") + text.count("!") + text.count("?")

        # Word statistics
        word_count = len(words)
        unique_words = set(words)
        unique_word_count = len(unique_words)

        # Word frequency
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Most common words
        most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

        return {
            "characters": characters,
            "characters_no_spaces": characters_no_spaces,
            "words": word_count,
            "unique_words": unique_word_count,
            "sentences": sentences,
            "avg_word_length": sum(len(w) for w in words) / word_count
            if word_count > 0
            else 0,
            "avg_sentence_length": word_count / sentences if sentences > 0 else 0,
            "word_frequency": word_freq,
            "most_common_words": most_common,
            "unique_word_set": unique_words,
        }

    def compare_texts(text1, text2):
        """Compare two texts using set operations."""
        cleaned1 = clean_text(text1).split()
        cleaned2 = clean_text(text2).split()

        set1 = set(cleaned1)
        set2 = set(cleaned2)

        return {
            "common_words": set1 & set2,
            "unique_to_text1": set1 - set2,
            "unique_to_text2": set2 - set1,
            "all_words": set1 | set2,
            "jaccard_similarity": len(set1 & set2) / len(set1 | set2)
            if (set1 | set2)
            else 0,
        }

    print("Sample text loaded.")
    print(f"Text preview: {sample_text[:100]}...")

    while True:
        print("\nMenu:")
        print("1. Analyze sample text")
        print("2. Enter custom text to analyze")
        print("3. Compare two texts")
        print("4. Word frequency analysis")
        print("5. Set operations on text")
        print("0. Exit")

        choice = input("\nEnter your choice (0-5): ")

        if choice == "0":
            print("Exiting Word Counter. Goodbye!")
            break

        elif choice == "1":
            results = analyze_text(sample_text)
            print(f"\nText Analysis Results:")
            print(f"  Characters: {results['characters']}")
            print(f"  Characters (no spaces): {results['characters_no_spaces']}")
            print(f"  Words: {results['words']}")
            print(f"  Unique words: {results['unique_words']}")
            print(f"  Sentences: {results['sentences']}")
            print(f"  Average word length: {results['avg_word_length']:.2f} chars")
            print(
                f"  Average sentence length: {results['avg_sentence_length']:.2f} words"
            )

        elif choice == "2":
            custom_text = input("Enter your text (press Enter twice to finish):\n")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)

            if lines:
                custom_text = "\n".join(lines)
                results = analyze_text(custom_text)
                print(f"\nCustom Text Analysis:")
                print(f"  Words: {results['words']}")
                print(f"  Unique words: {results['unique_words']}")
                print(f"  Characters: {results['characters']}")

        elif choice == "3":
            print("Enter first text:")
            text1 = input("> ")
            print("Enter second text:")
            text2 = input("> ")

            comparison = compare_texts(text1, text2)
            print(f"\nText Comparison:")
            print(f"  Common words: {len(comparison['common_words'])}")
            print(f"  Unique to text1: {len(comparison['unique_to_text1'])}")
            print(f"  Unique to text2: {len(comparison['unique_to_text2'])}")
            print(f"  Jaccard similarity: {comparison['jaccard_similarity']:.2%}")

            if input("Show common words? (y/n): ").lower() == "y":
                print(f"  Common words list: {sorted(comparison['common_words'])}")

        elif choice == "4":
            results = analyze_text(sample_text)
            print(f"\nTop 10 most common words:")
            for word, count in results["most_common_words"]:
                print(f"  {word}: {count}")

            search_word = input("\nSearch for specific word frequency: ").lower()
            if search_word in results["word_frequency"]:
                print(
                    f"'{search_word}' appears {results['word_frequency'][search_word]} times."
                )
            else:
                print(f"'{search_word}' not found in text.")

        elif choice == "5":
            # Demonstrate set operations on the sample text
            cleaned = clean_text(sample_text).split()
            word_set = set(cleaned)

            print(f"\nSet operations on sample text:")
            print(f"  Total unique words: {len(word_set)}")

            # Words starting with 'p'
            p_words = {w for w in word_set if w.startswith("p")}
            print(f"  Words starting with 'p': {sorted(p_words)}")

            # Words with length > 8
            long_words = {w for w in word_set if len(w) > 8}
            print(f"  Words longer than 8 chars: {sorted(long_words)[:10]}...")

            # Words containing 'ing'
            ing_words = {w for w in word_set if "ing" in w}
            print(f"  Words containing 'ing': {sorted(ing_words)}")

        else:
            print("Invalid choice. Please enter 0-5.")


def run_all_exercises():
    """Run all Day 12 exercises."""
    print("=" * 60)
    print("Week 2, Day 12: Sets & Strings")
    print("=" * 60)

    print("\n--- Exercise 1: Set Operations ---")
    exercise_1_set_operations()

    print("\n--- Exercise 2: String Methods ---")
    exercise_2_string_methods()

    print("\n--- Exercise 3: String Formatting ---")
    exercise_3_string_formatting()

    print("\n--- Exercise 4: Text Processing ---")
    exercise_4_text_processing()

    print("\n--- Exercise 5: Set and String Combinations ---")
    exercise_5_set_and_string_combinations()

    print("\n" + "=" * 60)
    print("Mini Project: Word Counter with Set Operations")
    print("=" * 60)
    mini_project_word_counter()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 12 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
