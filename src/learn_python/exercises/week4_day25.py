import sys
import time
import functools
import json

"""
Week 4, Day 25: Decorators

Exercises to practice using and creating decorators.
"""


def exercise_1_function_decorators():
    """
    Basic function decorators.

    1. Create simple decorators
    2. Apply decorators to functions
    3. Understand decorator syntax
    """
    print("Exercise 1: Function Decorators")
    print("-" * 40)

    # Simple decorator that prints function info
    def simple_decorator(func):
        def wrapper():
            print(f"Calling function: {func.__name__}")
            result = func()
            print(f"Function {func.__name__} finished")
            return result

        return wrapper

    @simple_decorator
    def say_hello():
        print("Hello, world!")

    @simple_decorator
    def say_goodbye():
        print("Goodbye, world!")

    print("Using simple decorator:")
    say_hello()
    print()
    say_goodbye()
    print()

    # Decorator with arguments
    def repeat(times):
        """Decorator that repeats function execution."""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                results = []
                for i in range(times):
                    print(f"Call {i + 1}/{times}")
                    result = func(*args, **kwargs)
                    results.append(result)
                return results

            return wrapper

        return decorator

    @repeat(3)
    def greet(name):
        print(f"Hello, {name}!")
        return f"Greeted {name}"

    print("\nUsing decorator with arguments:")
    results = greet("Alice")
    print(f"Results: {results}")
    print(f"Function name preserved: {greet.__name__}")


def exercise_2_decorators_with_args():
    """
    Decorators that accept arguments.

    1. Decorators with parameters
    2. Passing arguments to decorated functions
    3. Preserving function metadata
    """
    print("\n\nExercise 2: Decorators with Arguments")
    print("-" * 40)

    # Timing decorator
    def timer(description="Function"):
        """Decorator that times function execution."""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                duration = end_time - start_time
                print(f"{description} '{func.__name__}' took {duration:.6f} seconds")
                return result

            return wrapper

        return decorator

    @timer("Calculation")
    def slow_calculation(n):
        """Simulate a slow calculation."""
        total = 0
        for i in range(n):
            total += i**2
            time.sleep(0.001)  # Simulate work
        return total

    @timer("Database query")
    def database_query(query):
        """Simulate a database query."""
        time.sleep(0.1)
        return f"Results for: {query}"

    print("Using timer decorator:")
    result1 = slow_calculation(100)
    print(f"Result: {result1}\n")

    result2 = database_query("SELECT * FROM users")
    print(f"Result: {result2}\n")

    # Validation decorator
    def validate_input(min_val=None, max_val=None):
        """Decorator that validates function arguments."""

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Check positional arguments
                for i, arg in enumerate(args):
                    if isinstance(arg, (int, float)):
                        if min_val is not None and arg < min_val:
                            raise ValueError(f"Argument {i} must be >= {min_val}")
                        if max_val is not None and arg > max_val:
                            raise ValueError(f"Argument {i} must be <= {max_val}")

                # Check keyword arguments
                for key, value in kwargs.items():
                    if isinstance(value, (int, float)):
                        if min_val is not None and value < min_val:
                            raise ValueError(f"Argument '{key}' must be >= {min_val}")
                        if max_val is not None and value > max_val:
                            raise ValueError(f"Argument '{key}' must be <= {max_val}")

                return func(*args, **kwargs)

            return wrapper

        return decorator

    @validate_input(min_val=0, max_val=100)
    def calculate_percentage(value, total):
        """Calculate percentage."""
        return (value / total) * 100

    print("Using validation decorator:")
    try:
        percentage = calculate_percentage(75, 100)
        print(f"Percentage: {percentage}%")

        # This should raise an error
        percentage = calculate_percentage(-10, 100)
    except ValueError as e:
        print(f"Validation error: {e}")


def exercise_3_class_decorators():
    """
    Decorators for classes.

    1. Class decorators
    2. Modifying class behavior
    3. Adding methods or attributes
    """
    print("\n\nExercise 3: Class Decorators")
    print("-" * 40)

    # Singleton decorator
    def singleton(cls):
        """Decorator that makes a class a singleton."""
        instances = {}

        @functools.wraps(cls)
        def get_instance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

        return get_instance

    @singleton
    class DatabaseConnection:
        def __init__(self, connection_string):
            self.connection_string = connection_string
            print(f"Creating database connection to: {connection_string}")

        def query(self, sql):
            return f"Executing: {sql}"

    print("Singleton pattern with decorator:")
    db1 = DatabaseConnection("localhost:5432/mydb")
    db2 = DatabaseConnection("localhost:5432/otherdb")

    print(f"db1 is db2: {db1 is db2}")
    print(f"db1 connection: {db1.connection_string}")
    print(f"db2 connection: {db2.connection_string}")
    print()

    # Add logging to all methods
    def log_method_calls(cls):
        """Decorator that adds logging to all methods of a class."""
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                # Create a wrapper for the method
                def make_wrapper(method):
                    @functools.wraps(method)
                    def wrapper(self, *args, **kwargs):
                        print(
                            f"Calling {cls.__name__}.{method.__name__} with args={args}, kwargs={kwargs}"
                        )
                        result = method(self, *args, **kwargs)
                        print(f"{cls.__name__}.{method.__name__} returned: {result}")
                        return result

                    return wrapper

                # Replace the method with wrapped version
                setattr(cls, attr_name, make_wrapper(attr))

        return cls

    @log_method_calls
    class Calculator:
        def add(self, a, b):
            return a + b

        def multiply(self, a, b):
            return a * b

        def power(self, base, exponent):
            return base**exponent

    print("Class with logged methods:")
    calc = Calculator()
    result1 = calc.add(5, 3)
    result2 = calc.multiply(4, 6)
    result3 = calc.power(2, 8)

    print(f"\nFinal results: add={result1}, multiply={result2}, power={result3}")


def exercise_4_decorator_chaining():
    """
    Chaining multiple decorators.

    1. Multiple decorators on one function
    2. Order of execution
    3. Combining decorator functionality
    """
    print("\n\nExercise 4: Decorator Chaining")
    print("-" * 40)

    # Create several simple decorators
    def decorator1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1: Before function")
            result = func(*args, **kwargs)
            print("Decorator 1: After function")
            return result

        return wrapper

    def decorator2(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2: Before function")
            result = func(*args, **kwargs)
            print("Decorator 2: After function")
            return result

        return wrapper

    def decorator3(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 3: Before function")
            result = func(*args, **kwargs)
            print("Decorator 3: After function")
            return result

        return wrapper

    # Apply multiple decorators
    @decorator1
    @decorator2
    @decorator3
    def say_something(message):
        print(f"Function says: {message}")
        return f"Processed: {message}"

    print("Chained decorators (applied bottom to top):")
    print("Note: Decorators are applied from the innermost outward")
    print()
    result = say_something("Hello, decorators!")
    print(f"\nFinal result: {result}")
    print()

    # Practical example: combining decorators
    def log_call(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Calling {func.__name__} with args={args}, kwargs={kwargs}")
            return func(*args, **kwargs)

        return wrapper

    def handle_errors(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"[ERROR] in {func.__name__}: {e}")
                return None

        return wrapper

    def cache_results(max_size=128):
        """Decorator that caches function results."""
        cache = {}

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Create cache key
                key = (args, tuple(sorted(kwargs.items())))

                if key in cache:
                    print(f"[CACHE HIT] {func.__name__}{args}")
                    return cache[key]

                print(f"[CACHE MISS] {func.__name__}{args}")
                result = func(*args, **kwargs)

                # Manage cache size
                if len(cache) >= max_size:
                    # Remove oldest item (simple FIFO)
                    oldest_key = next(iter(cache))
                    del cache[oldest_key]

                cache[key] = result
                return result

            return wrapper

        return decorator

    @log_call
    @handle_errors
    @cache_results(max_size=2)
    def expensive_operation(x, y):
        """Simulate an expensive operation."""
        print(f"Performing expensive operation with {x}, {y}")
        time.sleep(0.5)  # Simulate work
        return x * y + x + y

    print("\nPractical decorator combination:")
    print("log_call -> handle_errors -> cache_results -> expensive_operation")
    print()

    # First calls (cache misses)
    result1 = expensive_operation(2, 3)
    print(f"Result 1: {result1}\n")

    result2 = expensive_operation(4, 5)
    print(f"Result 2: {result2}\n")

    # Repeat calls (cache hits)
    result1_again = expensive_operation(2, 3)
    print(f"Result 1 again: {result1_again}\n")

    result3 = expensive_operation(6, 7)  # This will evict oldest cache entry
    print(f"Result 3: {result3}\n")

    # Test error handling
    @handle_errors
    def risky_division(a, b):
        return a / b

    print("Error handling test:")
    result = risky_division(10, 2)
    print(f"10 / 2 = {result}")

    result = risky_division(10, 0)
    print(f"10 / 0 = {result}")


def exercise_5_builtin_decorators():
    """
    Python's built-in decorators.

    1. @property, @setter, @deleter
    2. @classmethod, @staticmethod
    3. @functools.wraps, @functools.lru_cache
    """
    print("\n\nExercise 5: Built-in Decorators")
    print("-" * 40)

    # Property decorators
    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            """Get the radius."""
            return self._radius

        @radius.setter
        def radius(self, value):
            """Set the radius with validation."""
            if value <= 0:
                raise ValueError("Radius must be positive")
            self._radius = value

        @radius.deleter
        def radius(self):
            """Delete the radius."""
            print("Deleting radius")
            del self._radius

        @property
        def diameter(self):
            """Calculate diameter (read-only property)."""
            return self._radius * 2

        @property
        def area(self):
            """Calculate area (read-only property)."""
            return 3.14159 * self._radius**2

    print("Property decorators:")
    circle = Circle(5)
    print(f"Radius: {circle.radius}")
    print(f"Diameter: {circle.diameter}")
    print(f"Area: {circle.area:.2f}")

    circle.radius = 10
    print(f"\nNew radius: {circle.radius}")
    print(f"New diameter: {circle.diameter}")
    print(f"New area: {circle.area:.2f}")

    try:
        circle.radius = -5
    except ValueError as e:
        print(f"\nError setting radius: {e}")

    print()

    # Classmethod and staticmethod
    class TemperatureConverter:
        @staticmethod
        def celsius_to_fahrenheit(celsius):
            """Convert Celsius to Fahrenheit."""
            return (celsius * 9 / 5) + 32

        @staticmethod
        def fahrenheit_to_celsius(fahrenheit):
            """Convert Fahrenheit to Celsius."""
            return (fahrenheit - 32) * 5 / 9

        @classmethod
        def from_string(cls, temp_str):
            """Create converter from string like '25C' or '77F'."""
            value = float(temp_str[:-1])
            unit = temp_str[-1].upper()

            if unit == "C":
                return cls(value, "C")
            elif unit == "F":
                return cls(value, "F")
            else:
                raise ValueError(f"Unknown unit: {unit}")

        def __init__(self, value, unit="C"):
            self.value = value
            self.unit = unit

        def convert(self, target_unit):
            """Convert to target unit."""
            if self.unit == target_unit:
                return self.value

            if self.unit == "C" and target_unit == "F":
                return self.celsius_to_fahrenheit(self.value)
            elif self.unit == "F" and target_unit == "C":
                return self.fahrenheit_to_celsius(self.value)
            else:
                raise ValueError(f"Cannot convert from {self.unit} to {target_unit}")

    print("Classmethod and staticmethod:")

    # Using static methods
    print(f"25°C = {TemperatureConverter.celsius_to_fahrenheit(25):.1f}°F")
    print(f"77°F = {TemperatureConverter.fahrenheit_to_celsius(77):.1f}°C")

    # Using class method
    temp1 = TemperatureConverter.from_string("25C")
    print(f"\nFrom '25C': {temp1.value}°{temp1.unit}")
    print(f"Converted to Fahrenheit: {temp1.convert('F'):.1f}°F")

    temp2 = TemperatureConverter.from_string("98.6F")
    print(f"\nFrom '98.6F': {temp2.value}°{temp2.unit}")
    print(f"Converted to Celsius: {temp2.convert('C'):.1f}°C")

    print()

    # functools.lru_cache
    import math

    @functools.lru_cache(maxsize=32)
    def fibonacci(n):
        """Calculate Fibonacci number with caching."""
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("functools.lru_cache for Fibonacci:")
    print("Calculating Fibonacci numbers...")

    start = time.time()
    for i in range(35):
        fib = fibonacci(i)
        if i % 10 == 0:
            print(f"  fib({i}) = {fib}")
    end = time.time()

    print(f"Time taken: {end - start:.3f} seconds")
    print(f"Cache info: {fibonacci.cache_info()}")


def mini_project_api_endpoint_decorators():
    """
    API Endpoint Decorators

    A simulated web framework with decorators for:
    1. Route registration (@app.route)
    2. Authentication (@authenticated)
    3. Rate limiting (@rate_limit)
    4. Input validation (@validate_json)
    5. Response formatting (@json_response)
    """
    print("\n" + "=" * 60)
    print("MINI PROJECT: API ENDPOINT DECORATORS")
    print("=" * 60)

    # Simulated web application
    class WebApp:
        def __init__(self):
            self.routes = {}
            self.middleware = []

        def route(self, path, methods=None):
            """Decorator to register a route."""
            if methods is None:
                methods = ["GET"]

            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    return func(*args, **kwargs)

                # Store the route
                self.routes[path] = {
                    "handler": wrapper,
                    "methods": methods,
                    "original_func": func,
                }
                return wrapper

            return decorator

        def authenticated(self, func):
            """Decorator to require authentication."""

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Simulated authentication check
                request = args[0] if args else {}
                token = request.get("headers", {}).get("Authorization")

                if token == "Bearer valid-token-123":
                    print(f"[AUTH] User authenticated for {func.__name__}")
                    return func(*args, **kwargs)
                else:
                    return {"error": "Authentication required", "status": 401}

            return wrapper

        def rate_limit(self, requests_per_minute=60):
            """Decorator to implement rate limiting."""
            import time

            request_timestamps = {}

            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    # Get client IP (simulated)
                    request = args[0] if args else {}
                    client_ip = request.get("client_ip", "unknown")

                    now = time.time()

                    # Clean old timestamps (older than 1 minute)
                    if client_ip in request_timestamps:
                        request_timestamps[client_ip] = [
                            t for t in request_timestamps[client_ip] if now - t < 60
                        ]
                    else:
                        request_timestamps[client_ip] = []

                    # Check rate limit
                    if len(request_timestamps[client_ip]) >= requests_per_minute:
                        return {
                            "error": "Rate limit exceeded",
                            "status": 429,
                            "retry_after": 60,
                        }

                    # Add current timestamp
                    request_timestamps[client_ip].append(now)

                    print(
                        f"[RATE LIMIT] {client_ip}: {len(request_timestamps[client_ip])}/{requests_per_minute} requests"
                    )
                    return func(*args, **kwargs)

                return wrapper

            return decorator

        def validate_json(self, schema):
            """Decorator to validate JSON request body."""

            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    request = args[0] if args else {}
                    body = request.get("body", {})

                    # Simple schema validation
                    for field, expected_type in schema.items():
                        if field not in body:
                            return {"error": f"Missing field: {field}", "status": 400}

                        if not isinstance(body[field], expected_type):
                            return {
                                "error": f"Field '{field}' must be of type {expected_type.__name__}",
                                "status": 400,
                            }

                    print(f"[VALIDATION] Request validated for {func.__name__}")
                    return func(*args, **kwargs)

                return wrapper

            return decorator

        def json_response(self, func):
            """Decorator to format response as JSON."""

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)

                # If result is already a dict with status, return as is
                if isinstance(result, dict) and "status" in result:
                    return result

                # Otherwise, wrap in JSON response
                return {"data": result, "status": 200, "timestamp": time.time()}

            return wrapper

        def handle_request(self, path, method, request):
            """Handle an incoming request."""
            if path not in self.routes:
                return {"error": "Not found", "status": 404}

            route_info = self.routes[path]
            if method not in route_info["methods"]:
                return {"error": "Method not allowed", "status": 405}

            handler = route_info["handler"]
            return handler(request)

    # Create app instance
    app = WebApp()

    # Define routes with decorators
    @app.route("/")
    @app.json_response
    def home(request):
        return {"message": "Welcome to the API"}

    @app.route("/api/users", methods=["GET"])
    @app.authenticated
    @app.rate_limit(requests_per_minute=30)
    @app.json_response
    def get_users(request):
        # Simulated database query
        users = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        ]
        return {"users": users}

    @app.route("/api/users", methods=["POST"])
    @app.authenticated
    @app.validate_json({"name": str, "email": str, "age": int})
    @app.json_response
    def create_user(request):
        body = request.get("body", {})

        # Simulate creating user
        new_user = {
            "id": 100,
            "name": body["name"],
            "email": body["email"],
            "age": body["age"],
        }

        return {"message": "User created", "user": new_user}

    @app.route("/api/stats", methods=["GET"])
    @app.rate_limit(requests_per_minute=10)
    @app.json_response
    def get_stats(request):
        # Simulated statistics
        import random

        return {
            "active_users": random.randint(100, 1000),
            "requests_today": random.randint(1000, 10000),
            "average_response_time": random.uniform(0.1, 0.5),
        }

    # Test the API
    print("Testing API endpoints:\n")

    # Test home endpoint
    print("1. Testing / endpoint:")
    request = {"client_ip": "192.168.1.100"}
    response = app.handle_request("/", "GET", request)
    print(f"   Response: {json.dumps(response, indent=2)}\n")

    # Test authenticated endpoint without auth
    print("2. Testing /api/users without authentication:")
    request = {"client_ip": "192.168.1.100", "headers": {}}
    response = app.handle_request("/api/users", "GET", request)
    print(f"   Response: {json.dumps(response, indent=2)}\n")

    # Test authenticated endpoint with auth
    print("3. Testing /api/users with authentication:")
    request = {
        "client_ip": "192.168.1.100",
        "headers": {"Authorization": "Bearer valid-token-123"},
    }
    response = app.handle_request("/api/users", "GET", request)
    print(f"   Response: {json.dumps(response, indent=2)}\n")

    # Test rate limiting
    print("4. Testing rate limiting on /api/stats:")
    for i in range(12):  # Limit is 10 requests per minute
        request = {"client_ip": "192.168.1.101"}
        response = app.handle_request("/api/stats", "GET", request)
        if i == 10:
            print(f"   Request {i + 1}: {json.dumps(response, indent=2)}")
            break

    # Test validation
    print("\n5. Testing validation on /api/users POST:")
    print("   a) Valid request:")
    valid_request = {
        "client_ip": "192.168.1.100",
        "headers": {"Authorization": "Bearer valid-token-123"},
        "body": {"name": "Diana", "email": "diana@example.com", "age": 28},
    }
    response = app.handle_request("/api/users", "POST", valid_request)
    print(f"   Response: {json.dumps(response, indent=2)}\n")

    print("   b) Invalid request (missing age):")
    invalid_request = {
        "client_ip": "192.168.1.100",
        "headers": {"Authorization": "Bearer valid-token-123"},
        "body": {"name": "Eve", "email": "eve@example.com"},
    }
    response = app.handle_request("/api/users", "POST", invalid_request)
    print(f"   Response: {json.dumps(response, indent=2)}\n")

    print("   c) Invalid request (wrong type):")
    invalid_request = {
        "client_ip": "192.168.1.100",
        "headers": {"Authorization": "Bearer valid-token-123"},
        "body": {"name": "Frank", "email": "frank@example.com", "age": "thirty"},
    }
    response = app.handle_request("/api/users", "POST", invalid_request)
    print(f"   Response: {json.dumps(response, indent=2)}")

    print("\n" + "-" * 60)
    print("Decorators used in this project:")
    print("  1. @app.route() - Registers URL routes")
    print("  2. @authenticated - Requires authentication")
    print("  3. @rate_limit() - Implements rate limiting")
    print("  4. @validate_json() - Validates request body")
    print("  5. @json_response - Formats responses as JSON")
    print("-" * 60)


def run_all_exercises():
    """Run all Day 25 exercises."""
    print("=" * 60)
    print("Week 4, Day 25: Decorators")
    print("=" * 60)

    print("\nThis day covers function and class decorators,")
    print("decorator chaining, and practical applications.")
    print("\nRunning exercises...")

    exercise_1_function_decorators()
    exercise_2_decorators_with_args()
    exercise_3_class_decorators()
    exercise_4_decorator_chaining()
    exercise_5_builtin_decorators()

    print("\n" + "=" * 60)
    print("Mini Project: API Endpoint Decorators")
    print("=" * 60)
    mini_project_api_endpoint_decorators()

    print("\n" + "=" * 60)
    print("Great work! You've completed Day 25 exercises.")
    print("=" * 60)


if __name__ == "__main__":
    func_name = sys.argv[1] if len(sys.argv) > 1 else None

    if func_name:
        print(f"Running {func_name}")
        globals()[func_name]()
    else:
        run_all_exercises()
