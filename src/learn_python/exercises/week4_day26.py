import itertools
import sys

"""
Week 4, Day 26: Generators & Iterators

Exercises to practice generators, iterators, and iteration protocols.
"""


def exercise_1_generator_basics():
    """
    Basic generator functions.

    1. Create simple generators with yield
    2. Iterate over generators
    3. Generator expressions
    """
    print("Exercise 1: Generator Basics")
    print("-" * 40)

    # Simple generator function
    def count_up_to(n):
        """Generate numbers from 1 to n."""
        i = 1
        while i <= n:
            yield i
            i += 1

    print("Simple generator function:")
    for num in count_up_to(5):
        print(f"  Generated: {num}")

    print()

    # Generator that yields multiple values
    def fibonacci_sequence(limit):
        """Generate Fibonacci numbers up to limit."""
        a, b = 0, 1
        while a <= limit:
            yield a
            a, b = b, a + b

    print("Fibonacci sequence generator:")
    fib_gen = fibonacci_sequence(100)
    for fib in fib_gen:
        print(f"  {fib}", end=" ")
    print("\n")

    # Generator expression (similar to list comprehension)
    print("Generator expressions:")

    # List comprehension (creates full list in memory)
    squares_list = [x**2 for x in range(10)]
    print(f"  List comprehension (in memory): {squares_list}")

    # Generator expression (lazy evaluation)
    squares_gen = (x**2 for x in range(10))
    print(f"  Generator expression (lazy): {squares_gen}")
    print("  Values from generator:", end=" ")
    for square in squares_gen:
        print(square, end=" ")
    print("\n")

    # Comparing memory usage
    import sys

    big_list = [x for x in range(1000000)]  # Creates list in memory
    big_gen = (x for x in range(1000000))  # Generator, no list created

    print("Memory comparison:")
    print(f"  List size: {sys.getsizeof(big_list):,} bytes")
    print(f"  Generator size: {sys.getsizeof(big_gen):,} bytes")

    # Clean up large objects
    del big_list
    del big_gen


def exercise_2_iterator_protocol():
    """
    Iterator protocol and custom iterators.

    1. iter() and next() functions
    2. Creating custom iterator classes
    3. StopIteration exception
    """
    print("\n\nExercise 2: Iterator Protocol")
    print("-" * 40)

    # Using iter() and next()
    print("Using iter() and next():")
    numbers = [1, 2, 3, 4, 5]
    iterator = iter(numbers)

    print(f"  First next(): {next(iterator)}")
    print(f"  Second next(): {next(iterator)}")
    print(f"  Third next(): {next(iterator)}")

    # Iterate through rest
    print("  Rest of iteration:")
    for num in iterator:
        print(f"    {num}")

    print()

    # Custom iterator class
    class Countdown:
        """Countdown from n to 1."""

        def __init__(self, start):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            value = self.current
            self.current -= 1
            return value

    print("Custom Countdown iterator:")
    countdown = Countdown(5)
    for number in countdown:
        print(f"  T-minus {number}")

    print()

    # Iterator that returns infinite sequence
    class InfiniteCounter:
        """Infinite counter iterator."""

        def __init__(self, start=0):
            self.current = start

        def __iter__(self):
            return self

        def __next__(self):
            value = self.current
            self.current += 1
            return value

    print("Infinite counter (first 10 values):")
    counter = InfiniteCounter()
    for i, value in enumerate(counter):
        if i >= 10:
            break
        print(f"  {value}", end=" ")
    print("\n")

    # Practical example: Reading large files line by line
    print("File reading with iterator protocol:")

    class FileLineReader:
        """Read a file line by line."""

        def __init__(self, filename):
            self.filename = filename

        def __iter__(self):
            self.file = open(self.filename, "r")
            return self

        def __next__(self):
            line = self.file.readline()
            if not line:
                self.file.close()
                raise StopIteration
            return line.strip()

    # Create a test file
    test_content = """Line 1: Hello
    Line 2: This is a test
    Line 3: Of the file reader
    Line 4: Using iterator protocol
    Line 5: Goodbye"""

    with open("test_file.txt", "w") as f:
        f.write(test_content)

    # Use the iterator
    reader = FileLineReader("test_file.txt")
    for line in reader:
        print(f"  {line}")

    # Clean up
    import os

    os.remove("test_file.txt")


def exercise_3_generator_state():
    """
    Generator state and communication.

    1. Generator state with .send()
    2. .throw() to raise exceptions in generators
    3. .close() to stop generators
    4. Generator return values
    """
    print("\n\nExercise 3: Generator State & Communication")
    print("-" * 40)

    # Generator with send()
    def accumulator():
        """Accumulate values sent to generator."""
        total = 0
        while True:
            value = yield total
            if value is None:
                break
            total += value

    print("Generator with send():")
    acc = accumulator()
    next(acc)  # Prime the generator

    print(f"  Initial state: {acc.send(10)}")
    print(f"  After adding 5: {acc.send(5)}")
    print(f"  After adding 3: {acc.send(3)}")

    # Close the generator
    acc.close()
    print("  Generator closed")

    print()

    # Generator with throw()
    def resilient_generator():
        """Generator that handles exceptions."""
        try:
            i = 0
            while True:
                try:
                    value = yield i
                    if value == "error":
                        raise ValueError("Simulated error")
                    i += 1
                except ValueError as e:
                    print(f"  Caught error in generator: {e}")
                    i = 0  # Reset on error
        except GeneratorExit:
            print("  Generator exiting cleanly")

    print("Generator with throw():")
    gen = resilient_generator()
    next(gen)

    print(f"  Normal yield: {gen.send(None)}")
    print(f"  Normal yield: {gen.send(None)}")

    # Send error signal
    print("  Sending error signal...")
    print(f"  Result: {gen.send('error')}")

    # Throw exception into generator
    print("  Throwing exception into generator...")
    try:
        gen.throw(RuntimeError("External error"))
    except RuntimeError as e:
        print(f"  Exception caught: {e}")

    gen.close()

    print()

    # Generator return values (Python 3.3+)
    def generator_with_return():
        """Generator that returns a final value."""
        yield 1
        yield 2
        yield 3
        return "Done"

    print("Generator return value:")
    gen = generator_with_return()

    try:
        while True:
            value = next(gen)
            print(f"  Yielded: {value}")
    except StopIteration as e:
        print(f"  Returned: {e.value}")


def exercise_4_itertools_module():
    """
    The itertools module.

    1. Infinite iterators
    2. Combinatoric iterators
    3. Iterators terminating on shortest input
    """
    print("\n\nExercise 4: itertools Module")
    print("-" * 40)

    print("Infinite iterators:")

    # count()
    print("  itertools.count():")
    counter = itertools.count(start=10, step=2)
    print("    First 5:", [next(counter) for _ in range(5)])

    # cycle()
    print("  itertools.cycle():")
    cycler = itertools.cycle(["A", "B", "C"])
    print("    First 6:", [next(cycler) for _ in range(6)])

    # repeat()
    print("  itertools.repeat():")
    repeater = itertools.repeat("Python", 3)
    print("    Limited repeat:", list(repeater))

    print()

    print("Iterators terminating on shortest input:")

    # chain()
    print("  itertools.chain():")
    chained = itertools.chain([1, 2, 3], ["a", "b", "c"])
    print("    Chained:", list(chained))

    # zip_longest()
    print("  itertools.zip_longest():")
    zipped = itertools.zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")
    print("    Zip longest:", list(zipped))

    # islice()
    print("  itertools.islice():")
    numbers = itertools.count()
    sliced = itertools.islice(numbers, 5, 15, 2)  # Start at 5, stop at 15, step 2
    print("    Sliced infinite iterator:", list(sliced))

    print()

    print("Combinatoric iterators:")

    # product()
    print("  itertools.product():")
    product_result = itertools.product([1, 2], ["a", "b"])
    print("    Cartesian product:", list(product_result))

    # permutations()
    print("  itertools.permutations():")
    perm_result = itertools.permutations([1, 2, 3], 2)
    print("    Permutations of length 2:", list(perm_result))

    # combinations()
    print("  itertools.combinations():")
    comb_result = itertools.combinations([1, 2, 3, 4], 3)
    print("    Combinations of 3 items:", list(comb_result))

    print()

    # Practical example: Batch processing
    print("Practical example: Batch processing")

    def batched(iterable, batch_size):
        """Batch an iterable into chunks of given size."""
        iterator = iter(iterable)
        while True:
            batch = list(itertools.islice(iterator, batch_size))
            if not batch:
                break
            yield batch

    data = list(range(20))  # 0-19
    print(f"  Original data: {data}")
    print("  Batched (size 5):")
    for i, batch in enumerate(batched(data, 5), 1):
        print(f"    Batch {i}: {batch}")


def exercise_5_lazy_evaluation():
    """
    Lazy evaluation patterns.

    1. Memory-efficient data processing
    2. Pipeline processing with generators
    3. Infinite sequences
    4. Coroutine patterns
    """
    print("\n\nExercise 5: Lazy Evaluation Patterns")
    print("-" * 40)

    # Memory-efficient processing pipeline
    print("Processing pipeline with generators:")

    def read_numbers(filename):
        """Read numbers from file, one per line."""
        with open(filename, "r") as f:
            for line in f:
                yield int(line.strip())

    def filter_even(numbers):
        """Filter even numbers."""
        for n in numbers:
            if n % 2 == 0:
                yield n

    def square(numbers):
        """Square numbers."""
        for n in numbers:
            yield n**2

    def take_first(numbers, n):
        """Take first n numbers."""
        count = 0
        for value in numbers:
            if count >= n:
                break
            yield value
            count += 1

    # Create test file
    with open("numbers.txt", "w") as f:
        f.writelines(f"{i}\n" for i in range(100))

    # Build processing pipeline
    pipeline = take_first(square(filter_even(read_numbers("numbers.txt"))), 10)

    print("  Pipeline: read → filter_even → square → take_first(10)")
    print("  Results:", list(pipeline))

    # Clean up
    import os

    os.remove("numbers.txt")

    print()

    # Infinite sequence generation
    print("Infinite sequence: Prime numbers")

    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_generator():
        """Generate prime numbers indefinitely."""
        n = 2
        while True:
            if is_prime(n):
                yield n
            n += 1

    primes = prime_generator()
    print("  First 10 primes:", [next(primes) for _ in range(10)])

    print()

    # Coroutine pattern with generators
    print("Coroutine pattern:")

    def grep(pattern):
        """Search for pattern in lines."""
        print(f"  Looking for {pattern}")
        while True:
            line = yield
            if pattern in line:
                print(f"    Found: {line}")

    # Create coroutine
    searcher = grep("python")
    next(searcher)  # Prime

    # Send data
    searcher.send("I love python programming")
    searcher.send("Java is also a language")
    searcher.send("Python is great for data science")
    searcher.send("C++ is fast")

    searcher.close()

    print()

    # Generator-based state machine
    print("State machine with generators:")

    def traffic_light():
        """Simulate a traffic light."""
        states = ["RED", "GREEN", "YELLOW"]
        index = 0

        while True:
            current_state = states[index]
            command = yield current_state

            if command == "next":
                index = (index + 1) % len(states)
            elif command == "reset":
                index = 0

    light = traffic_light()
    next(light)  # Prime

    print("  Initial state:", light.send(None))
    print("  After 'next':", light.send("next"))
    print("  After 'next':", light.send("next"))
    print("  After 'next':", light.send("next"))
    print("  After 'reset':", light.send("reset"))


def mini_project_pagination_system():
    """
    Pagination System

    A system for paginating large datasets with features:
    1. Paginate any iterable or generator
    2. Support for different page sizes
    3. Navigation between pages
    4. Efficient memory usage for large datasets
    """
    print("\n" + "=" * 60)
    print("MINI PROJECT: PAGINATION SYSTEM")
    print("=" * 60)

    class Paginator:
        """Paginate any iterable."""

        def __init__(self, data, page_size=10):
            """
            Initialize paginator.

            Args:
                data: Any iterable (list, generator, etc.)
                page_size: Number of items per page
            """
            self.data = data
            self.page_size = page_size
            self.total_items = 0
            self._cache = {}  # Cache pages for efficient navigation

            # If data is a generator or iterator, we need to be careful
            self.is_generator = hasattr(data, "__next__") or hasattr(data, "send")

            if not self.is_generator:
                # For non-generators, we can calculate total
                try:
                    self.total_items = len(data)
                except TypeError:
                    # Convert to list to get length (only for small datasets)
                    temp_list = list(data)
                    self.total_items = len(temp_list)
                    self.data = temp_list  # Replace with list for efficient access

        def get_page(self, page_number):
            """Get a specific page (1-indexed)."""
            if page_number < 1:
                raise ValueError("Page number must be >= 1")

            # Check cache first
            if page_number in self._cache:
                return self._cache[page_number]

            # Calculate start and end indices
            start_idx = (page_number - 1) * self.page_size

            if self.is_generator:
                # For generators, we need to iterate to the right position
                result = []
                iterator = iter(self.data)

                # Skip to start position
                for _ in range(start_idx):
                    try:
                        next(iterator)
                    except StopIteration:
                        break

                # Collect page_size items
                for _ in range(self.page_size):
                    try:
                        result.append(next(iterator))
                    except StopIteration:
                        break

                page = Page(
                    result,
                    page_number,
                    self.page_size,
                    has_next=len(result) == self.page_size,
                )
            else:
                # For lists/sequences, use slicing
                end_idx = start_idx + self.page_size
                page_data = list(self.data)[start_idx:end_idx]

                has_next = (
                    end_idx < self.total_items
                    if self.total_items > 0
                    else len(page_data) == self.page_size
                )
                page = Page(page_data, page_number, self.page_size, has_next=has_next)

            # Cache the page
            self._cache[page_number] = page
            return page

        def total_pages(self):
            """Calculate total number of pages."""
            if self.total_items > 0:
                return (self.total_items + self.page_size - 1) // self.page_size
            return None  # Unknown for infinite generators

        def iter_pages(self):
            """Iterate through all pages."""
            page_num = 1
            while True:
                page = self.get_page(page_num)
                if not page.items:
                    break
                yield page
                if not page.has_next:
                    break
                page_num += 1

        def get_page_info(self, page_number):
            """Get information about a specific page."""
            page = self.get_page(page_number)
            return {
                "page_number": page_number,
                "page_size": self.page_size,
                "item_count": len(page.items),
                "items": page.items,
                "has_previous": page_number > 1,
                "has_next": page.has_next,
                "total_pages": self.total_pages(),
                "total_items": self.total_items if self.total_items > 0 else "unknown",
            }

    class Page:
        """Represents a single page of data."""

        def __init__(self, items, number, page_size, has_next=False):
            self.items = items
            self.number = number
            self.page_size = page_size
            self.has_next = has_next

        def __str__(self):
            return f"Page {self.number} ({len(self.items)} items)"

        def __repr__(self):
            return f"Page(number={self.number}, items={len(self.items)})"

    # Test with different data sources

    print("1. Paginating a list:")
    data_list = list(range(1, 101))  # 1 to 100
    paginator_list = Paginator(data_list, page_size=10)

    print(f"   Total items: {paginator_list.total_items}")
    print(f"   Page size: {paginator_list.page_size}")
    print(f"   Total pages: {paginator_list.total_pages()}")

    page1 = paginator_list.get_page(1)
    print(f"   Page 1: {page1.items}")

    page5 = paginator_list.get_page(5)
    print(f"   Page 5: {page5.items}")

    page10 = paginator_list.get_page(10)
    print(f"   Page 10: {page10.items}")
    print(f"   Has next page: {page10.has_next}")

    print("\n2. Paginating a generator:")

    def data_generator(n=100):
        """Generate data on the fly."""
        for i in range(1, n + 1):
            yield {"id": i, "name": f"Item {i}", "value": i * 10}

    paginator_gen = Paginator(data_generator(50), page_size=7)

    print(f"   Page size: {paginator_gen.page_size}")

    page_info = paginator_gen.get_page_info(1)
    print(f"   Page 1 info: {page_info['item_count']} items")
    print(f"   Sample item: {page_info['items'][0] if page_info['items'] else 'None'}")

    page_info = paginator_gen.get_page_info(3)
    print(f"   Page 3: {[item['id'] for item in page_info['items']]}")

    print("\n3. Iterating through all pages:")
    print("   Pages from generator paginator:")
    for i, page in enumerate(paginator_gen.iter_pages(), 1):
        print(f"     {page} - Items: {[item['id'] for item in page.items]}")
        if i >= 3:  # Show first 3 pages only
            print("     ...")
            break

    print("\n4. Infinite data source (with limit):")

    def infinite_counter():
        """Generate infinite sequence."""
        i = 1
        while True:
            yield f"Data point {i}"
            i += 1

    # Paginate infinite generator with safety limit
    class SafePaginator(Paginator):
        """Paginator with safety limits for infinite data."""

        def __init__(self, data, page_size=10, max_items=1000):
            super().__init__(data, page_size)
            self.max_items = max_items
            self._items_seen = 0

        def get_page(self, page_number):
            if page_number < 1:
                raise ValueError("Page number must be >= 1")

            start_idx = (page_number - 1) * self.page_size

            # Safety check
            if start_idx >= self.max_items:
                return Page([], page_number, self.page_size, has_next=False)

            result = []
            iterator = iter(self.data)

            # Skip to start position
            skip_count = min(start_idx, self.max_items)
            for _ in range(skip_count):
                try:
                    next(iterator)
                    self._items_seen += 1
                except StopIteration:
                    break

            # Collect page_size items
            for _ in range(self.page_size):
                if self._items_seen >= self.max_items:
                    break
                try:
                    result.append(next(iterator))
                    self._items_seen += 1
                except StopIteration:
                    break

            has_next = (
                len(result) == self.page_size and self._items_seen < self.max_items
            )
            return Page(result, page_number, self.page_size, has_next=has_next)

    safe_paginator = SafePaginator(infinite_counter(), page_size=5, max_items=20)

    print("   First 4 pages of infinite data (limited to 20 items):")
    for page in safe_paginator.iter_pages():
        print(f"     {page}: {page.items}")

    print("\n5. Interactive pagination demo:")

    # Sample dataset
    products = [
        {
            "id": i,
            "name": f"Product {i}",
            "price": 10 + i * 5,
            "category": "Electronics" if i % 3 == 0 else "Home",
        }
        for i in range(1, 51)
    ]

    product_paginator = Paginator(products, page_size=8)
    current_page = 1

    while True:
        page_info = product_paginator.get_page_info(current_page)

        print(f"\n{'=' * 50}")
        print(f"PAGE {current_page} of {page_info['total_pages'] or '?'}")
        print(
            f"Showing {len(page_info['items'])} of {page_info['total_items']} products"
        )
        print(f"{'=' * 50}")

        for product in page_info["items"]:
            print(
                f"  #{product['id']:3d} {product['name']:15s} ${product['price']:6.2f} [{product['category']}]"
            )

        print("\nNavigation:")
        if page_info["has_previous"]:
            print("  P - Previous page")
        if page_info["has_next"]:
            print("  N - Next page")
        print("  # - Go to page number")
        print("  Q - Quit")

        choice = input("\nEnter choice: ").strip().upper()

        if choice == "Q":
            print("Exiting pagination demo.")
            break
        elif choice == "P" and page_info["has_previous"]:
            current_page -= 1
        elif choice == "N" and page_info["has_next"]:
            current_page += 1
        elif choice.isdigit():
            page_num = int(choice)
            if 1 <= page_num <= (page_info["total_pages"] or float("inf")):
                current_page = page_num
            else:
                print(
                    f"Invalid page number. Must be between 1 and {page_info['total_pages']}"
                )
        else:
            print("Invalid choice.")


def run_all_exercises():
    """Run all Day 26 exercises."""
    print("=" * 60)
    print("Week 4, Day 26: Generators & Iterators")
    print("=" * 60)

    print("\nThis day covers generators, iterators, lazy evaluation,")
    print("and practical applications like pagination systems.")
    print("\nRunning exercises...")

    exercise_1_generator_basics()
    exercise_2_iterator_protocol()
    exercise_3_generator_state()
    exercise_4_itertools_module()
    exercise_5_lazy_evaluation()

    print("\n" + "=" * 60)
    print("Mini Project: Pagination System")
    print("=" * 60)
    mini_project_pagination_system()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 26 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
