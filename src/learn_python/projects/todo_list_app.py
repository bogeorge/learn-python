"""
To-Do List Application

A comprehensive to-do list application with file persistence and search functionality.
This project demonstrates functions, data structures, and file handling concepts from Week 2.
"""

import json
import os
import sys
from datetime import datetime


class TodoList:
    """Main to-do list application class."""

    def __init__(self, filename: str = "todo_data.json"):
        """Initialize the to-do list with optional file persistence."""
        self.filename = filename
        self.tasks: list[dict] = self.load_tasks()
        self.next_id = max([task["id"] for task in self.tasks], default=0) + 1

    def load_tasks(self) -> list[dict]:
        """Load tasks from JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    return json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")
        return []

    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=2)
        except OSError as e:
            print(f"Error saving tasks: {e}")

    def add_task(
        self,
        description: str,
        priority: str = "medium",
        category: str = "general",
        due_date: str | None = None,
    ):
        """Add a new task to the list."""
        task = {
            "id": self.next_id,
            "description": description,
            "priority": priority,
            "category": category,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None,
        }

        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task added (ID: {task['id']})")
        return task["id"]

    def remove_task(self, task_id: int):
        """Remove a task by ID."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                self.save_tasks()
                print(f"Task {task_id} removed: '{removed_task['description']}'")
                return True
        print(f"Task {task_id} not found")
        return False

    def mark_complete(self, task_id: int):
        """Mark a task as complete."""
        for task in self.tasks:
            if task["id"] == task_id:
                if not task["completed"]:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    self.save_tasks()
                    print(f"Task {task_id} marked as complete")
                else:
                    print(f"Task {task_id} is already complete")
                return True
        print(f"Task {task_id} not found")
        return False

    def mark_incomplete(self, task_id: int):
        """Mark a task as incomplete."""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    task["completed"] = False
                    task["completed_at"] = None
                    self.save_tasks()
                    print(f"Task {task_id} marked as incomplete")
                else:
                    print(f"Task {task_id} is already incomplete")
                return True
        print(f"Task {task_id} not found")
        return False

    def view_tasks(
        self,
        show_completed: bool = True,
        filter_by: str | None = None,
        filter_value: str | None = None,
    ):
        """View tasks with optional filtering."""
        filtered_tasks = self.tasks.copy()

        if not show_completed:
            filtered_tasks = [t for t in filtered_tasks if not t["completed"]]

        if filter_by and filter_value:
            if filter_by == "priority":
                filtered_tasks = [
                    t for t in filtered_tasks if t["priority"] == filter_value
                ]
            elif filter_by == "category":
                filtered_tasks = [
                    t for t in filtered_tasks if t["category"] == filter_value
                ]
            elif filter_by == "due_date":
                filtered_tasks = [
                    t for t in filtered_tasks if t["due_date"] == filter_value
                ]

        if not filtered_tasks:
            print("No tasks found.")
            return

        print(f"\n{'=' * 60}")
        print(f"TO-DO LIST ({len(filtered_tasks)} tasks)")
        print(f"{'=' * 60}")

        for task in filtered_tasks:
            status = "✓" if task["completed"] else " "
            priority_symbol = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(
                task["priority"], "⚪"
            )

            print(
                f"{priority_symbol} [{status}] {task['id']:3d}. {task['description']}"
            )
            print(
                f"     Category: {task['category']}, Due: {task['due_date'] or 'No due date'}"
            )

            if task["completed"] and task["completed_at"]:
                completed_date = datetime.fromisoformat(task["completed_at"]).strftime(
                    "%Y-%m-%d"
                )
                print(f"     Completed on: {completed_date}")
            print()

    def search_tasks(self, search_term: str, search_in: str = "all"):
        """Search for tasks containing the search term."""
        results = []
        search_term = search_term.lower()

        for task in self.tasks:
            matches = False

            if search_in in ["all", "description"] and search_term in task["description"].lower():
                    matches = True

            if search_in in ["all", "category"] and search_term in task["category"].lower():
                    matches = True

            if matches:
                results.append(task)

        if results:
            print(f"\nFound {len(results)} task(s) matching '{search_term}':")
            for task in results:
                status = "Complete" if task["completed"] else "Pending"
                print(f"  ID {task['id']}: {task['description']} [{status}]")
        else:
            print(f"No tasks found matching '{search_term}'")

        return results

    def get_statistics(self):
        """Get statistics about the to-do list."""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["completed"])
        pending = total - completed

        # Tasks by priority
        priorities = {}
        for task in self.tasks:
            priorities[task["priority"]] = priorities.get(task["priority"], 0) + 1

        # Tasks by category
        categories = {}
        for task in self.tasks:
            categories[task["category"]] = categories.get(task["category"], 0) + 1

        print(f"\n{'=' * 60}")
        print("TO-DO LIST STATISTICS")
        print(f"{'=' * 60}")
        print(f"Total tasks: {total}")
        print(f"Completed: {completed} ({completed / total * 100:.1f}%)")
        print(f"Pending: {pending} ({pending / total * 100:.1f}%)")

        print("\nBy priority:")
        for priority, count in priorities.items():
            print(f"  {priority}: {count}")

        print("\nBy category:")
        for category, count in categories.items():
            print(f"  {category}: {count}")

    def clear_completed(self):
        """Remove all completed tasks."""
        completed_count = sum(1 for task in self.tasks if task["completed"])

        if completed_count == 0:
            print("No completed tasks to clear.")
            return False

        confirm = input(f"Remove {completed_count} completed task(s)? (y/n): ")
        if confirm.lower() == "y":
            self.tasks = [task for task in self.tasks if not task["completed"]]
            self.save_tasks()
            print(f"Removed {completed_count} completed task(s)")
            return True

        print("Operation cancelled.")
        return False

    def edit_task(self, task_id: int, **updates):
        """Edit an existing task."""
        for task in self.tasks:
            if task["id"] == task_id:
                valid_fields = ["description", "priority", "category", "due_date"]
                for field, value in updates.items():
                    if field in valid_fields:
                        task[field] = value

                self.save_tasks()
                print(f"Task {task_id} updated")
                return True

        print(f"Task {task_id} not found")
        return False


def display_menu():
    """Display the main menu."""
    print(f"\n{'=' * 60}")
    print("TO-DO LIST APPLICATION")
    print(f"{'=' * 60}")
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Mark task complete/incomplete")
    print("4. Remove task")
    print("5. Search tasks")
    print("6. View statistics")
    print("7. Clear completed tasks")
    print("8. Edit task")
    print("9. Filter tasks")
    print("0. Exit")
    print(f"{'=' * 60}")


def get_priority_input():
    """Get valid priority input from user."""
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            return priority
        print("Please enter 'high', 'medium', or 'low'")


def get_date_input():
    """Get valid date input from user."""
    while True:
        date_str = input("Due date (YYYY-MM-DD) or leave blank: ").strip()
        if not date_str:
            return None

        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Please use YYYY-MM-DD format or leave blank")


def main():
    """Main application loop."""
    todo_list = TodoList()

    print("Welcome to the To-Do List Application!")
    print(f"Loaded {len(todo_list.tasks)} task(s) from storage.")

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (0-9): ")

            if choice == "0":
                print("Goodbye!")
                break

            elif choice == "1":
                show_completed = input("Show completed tasks? (y/n): ").lower() == "y"
                todo_list.view_tasks(show_completed=show_completed)

            elif choice == "2":
                print("\nAdd New Task:")
                description = input("Task description: ").strip()
                if not description:
                    print("Description cannot be empty.")
                    continue

                priority = get_priority_input()
                category = input("Category: ").strip() or "general"
                due_date = get_date_input()

                todo_list.add_task(description, priority, category, due_date)

            elif choice == "3":
                try:
                    task_id = int(input("Enter task ID: "))
                    action = input("Mark (c)omplete or (i)ncomplete? ").lower()

                    if action == "c":
                        todo_list.mark_complete(task_id)
                    elif action == "i":
                        todo_list.mark_incomplete(task_id)
                    else:
                        print(
                            "Invalid action. Use 'c' for complete or 'i' for incomplete."
                        )
                except ValueError:
                    print("Please enter a valid task ID (number).")

            elif choice == "4":
                try:
                    task_id = int(input("Enter task ID to remove: "))
                    todo_list.remove_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID (number).")

            elif choice == "5":
                print("\nSearch Options:")
                print("1. Search in description")
                print("2. Search in category")
                print("3. Search everywhere")

                search_choice = input("Enter search option (1-3): ")

                if search_choice == "1":
                    search_in = "description"
                elif search_choice == "2":
                    search_in = "category"
                elif search_choice == "3":
                    search_in = "all"
                else:
                    print("Invalid choice. Defaulting to search everywhere.")
                    search_in = "all"

                search_term = input("Enter search term: ")
                todo_list.search_tasks(search_term, search_in)

            elif choice == "6":
                todo_list.get_statistics()

            elif choice == "7":
                todo_list.clear_completed()

            elif choice == "8":
                try:
                    task_id = int(input("Enter task ID to edit: "))

                    print("\nLeave blank to keep current value.")
                    description = input("New description: ").strip()
                    priority = (
                        input("New priority (high/medium/low): ").strip().lower()
                    )
                    category = input("New category: ").strip()
                    due_date = input("New due date (YYYY-MM-DD): ").strip()

                    updates = {}
                    if description:
                        updates["description"] = description
                    if priority in ["high", "medium", "low"]:
                        updates["priority"] = priority
                    if category:
                        updates["category"] = category
                    if due_date:
                        try:
                            datetime.strptime(due_date, "%Y-%m-%d")
                            updates["due_date"] = due_date
                        except ValueError:
                            print("Invalid date format. Date not updated.")

                    if updates:
                        todo_list.edit_task(task_id, **updates)
                    else:
                        print("No changes made.")

                except ValueError:
                    print("Please enter a valid task ID (number).")

            elif choice == "9":
                print("\nFilter Options:")
                print("1. Filter by priority")
                print("2. Filter by category")
                print("3. Filter by completion status")

                filter_choice = input("Enter filter option (1-3): ")

                if filter_choice == "1":
                    priority = get_priority_input()
                    todo_list.view_tasks(filter_by="priority", filter_value=priority)
                elif filter_choice == "2":
                    category = input("Enter category: ").strip()
                    todo_list.view_tasks(filter_by="category", filter_value=category)
                elif filter_choice == "3":
                    show_completed = input(
                        "Show (c)ompleted or (p)ending tasks? "
                    ).lower()
                    todo_list.view_tasks(show_completed=(show_completed == "c"))
                else:
                    print("Invalid choice.")

            else:
                print("Invalid choice. Please enter 0-9.")

        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Allow running specific functions from command line
    if len(sys.argv) > 1:
        todo_list = TodoList()

        if sys.argv[1] == "view":
            todo_list.view_tasks()
        elif sys.argv[1] == "add":
            if len(sys.argv) >= 3:
                todo_list.add_task(sys.argv[2])
                print(f"Task added: {sys.argv[2]}")
            else:
                print("Usage: python todo_list_app.py add 'Task description'")
        elif sys.argv[1] == "complete":
            if len(sys.argv) >= 3:
                try:
                    task_id = int(sys.argv[2])
                    todo_list.mark_complete(task_id)
                except ValueError:
                    print("Please provide a valid task ID")
        elif sys.argv[1] == "stats":
            todo_list.get_statistics()
        else:
            print(f"Unknown command: {sys.argv[1]}")
    else:
        main()
