"""
Library Management System

A complete library management system with:
- Book and Member classes
- Borrowing/returning system
- Search functionality
- Data persistence with JSON
- Overdue fines calculation
- Reports generation
"""

import json
import os
from datetime import datetime, timedelta, date
import uuid
from typing import List, Dict, Optional, Union

DATA_DIR = "library_data"
BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
MEMBERS_FILE = os.path.join(DATA_DIR, "members.json")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.json")


class Book:
    """Represents a book in the library."""
    
    def __init__(self, title: str, author: str, isbn: str, year: int, 
                 category: str = "Unknown", copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.category = category
        self.total_copies = copies
        self.available_copies = copies
        self.borrowed_by = []  # List of (member_id, due_date)
        self.date_added = date.today().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert book to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "category": self.category,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
            "borrowed_by": self.borrowed_by,
            "date_added": self.date_added
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Book':
        """Create book from dictionary."""
        book = cls(
            title=data["title"],
            author=data["author"],
            isbn=data["isbn"],
            year=data["year"],
            category=data.get("category", "Unknown"),
            copies=data.get("total_copies", 1)
        )
        book.available_copies = data["available_copies"]
        book.borrowed_by = data.get("borrowed_by", [])
        book.date_added = data.get("date_added", date.today().isoformat())
        return book
    
    def check_out(self, member_id: str, days: int = 14) -> bool:
        """Check out a copy of this book to a member."""
        if self.available_copies <= 0:
            return False
        
        due_date = (date.today() + timedelta(days=days)).isoformat()
        self.borrowed_by.append((member_id, due_date))
        self.available_copies -= 1
        return True
    
    def return_book(self, member_id: str) -> bool:
        """Return a borrowed copy of this book."""
        for i, (borrowed_member_id, due_date) in enumerate(self.borrowed_by):
            if borrowed_member_id == member_id:
                self.borrowed_by.pop(i)
                self.available_copies += 1
                return True
        return False
    
    def is_available(self) -> bool:
        """Check if any copies are available."""
        return self.available_copies > 0
    
    def get_overdue_borrowers(self) -> List[tuple]:
        """Get list of members with overdue copies."""
        today = date.today()
        overdue = []
        for member_id, due_date_str in self.borrowed_by:
            due_date = date.fromisoformat(due_date_str)
            if due_date < today:
                overdue.append((member_id, due_date_str))
        return overdue
    
    def __str__(self) -> str:
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} ({self.year}) - {status} ({self.available_copies}/{self.total_copies})"


class Member:
    """Represents a library member."""
    
    def __init__(self, name: str, email: str, phone: str = ""):
        self.member_id = str(uuid.uuid4())[:8]  # Generate unique ID
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []  # List of (isbn, due_date)
        self.fines = 0.0
        self.membership_date = date.today().isoformat()
        self.max_books = 5  # Maximum books a member can borrow
        self.is_active = True
    
    def to_dict(self) -> Dict:
        """Convert member to dictionary for JSON serialization."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "borrowed_books": self.borrowed_books,
            "fines": self.fines,
            "membership_date": self.membership_date,
            "max_books": self.max_books,
            "is_active": self.is_active
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Member':
        """Create member from dictionary."""
        member = cls(
            name=data["name"],
            email=data["email"],
            phone=data.get("phone", "")
        )
        member.member_id = data["member_id"]
        member.borrowed_books = data.get("borrowed_books", [])
        member.fines = data.get("fines", 0.0)
        member.membership_date = data.get("membership_date", date.today().isoformat())
        member.max_books = data.get("max_books", 5)
        member.is_active = data.get("is_active", True)
        return member
    
    def can_borrow(self) -> bool:
        """Check if member can borrow more books."""
        return len(self.borrowed_books) < self.max_books and self.is_active and self.fines == 0
    
    def borrow_book(self, isbn: str, days: int = 14) -> bool:
        """Record a book borrowing."""
        if not self.can_borrow():
            return False
        
        due_date = (date.today() + timedelta(days=days)).isoformat()
        self.borrowed_books.append((isbn, due_date))
        return True
    
    def return_book(self, isbn: str) -> bool:
        """Record a book return."""
        for i, (borrowed_isbn, due_date) in enumerate(self.borrowed_books):
            if borrowed_isbn == isbn:
                self.borrowed_books.pop(i)
                
                # Check if overdue
                due_date_obj = date.fromisoformat(due_date)
                if due_date_obj < date.today():
                    days_overdue = (date.today() - due_date_obj).days
                    self.fines += days_overdue * 0.25  # $0.25 per day
                
                return True
        return False
    
    def get_overdue_books(self) -> List[tuple]:
        """Get list of overdue books."""
        today = date.today()
        overdue = []
        for isbn, due_date_str in self.borrowed_books:
            due_date = date.fromisoformat(due_date_str)
            if due_date < today:
                overdue.append((isbn, due_date_str))
        return overdue
    
    def pay_fine(self, amount: float) -> float:
        """Pay fine and return change."""
        if amount <= 0:
            return amount
        
        if amount >= self.fines:
            change = amount - self.fines
            self.fines = 0
            return change
        else:
            self.fines -= amount
            return 0
    
    def __str__(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} ({self.member_id}) - {status}, Books: {len(self.borrowed_books)}/{self.max_books}, Fines: ${self.fines:.2f}"


class Library:
    """Main library system."""
    
    def __init__(self):
        self.books: Dict[str, Book] = {}  # ISBN -> Book
        self.members: Dict[str, Member] = {}  # member_id -> Member
        self.transactions: List[Dict] = []
        self._load_data()
    
    def _ensure_data_dir(self):
        """Ensure data directory exists."""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
    
    def _load_data(self):
        """Load data from JSON files."""
        self._ensure_data_dir()
        
        # Load books
        if os.path.exists(BOOKS_FILE):
            try:
                with open(BOOKS_FILE, 'r') as f:
                    books_data = json.load(f)
                    for book_data in books_data:
                        book = Book.from_dict(book_data)
                        self.books[book.isbn] = book
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading books: {e}")
        
        # Load members
        if os.path.exists(MEMBERS_FILE):
            try:
                with open(MEMBERS_FILE, 'r') as f:
                    members_data = json.load(f)
                    for member_data in members_data:
                        member = Member.from_dict(member_data)
                        self.members[member.member_id] = member
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading members: {e}")
        
        # Load transactions
        if os.path.exists(TRANSACTIONS_FILE):
            try:
                with open(TRANSACTIONS_FILE, 'r') as f:
                    self.transactions = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading transactions: {e}")
    
    def _save_data(self):
        """Save data to JSON files."""
        self._ensure_data_dir()
        
        # Save books
        books_data = [book.to_dict() for book in self.books.values()]
        try:
            with open(BOOKS_FILE, 'w') as f:
                json.dump(books_data, f, indent=2)
        except IOError as e:
            print(f"Error saving books: {e}")
        
        # Save members
        members_data = [member.to_dict() for member in self.members.values()]
        try:
            with open(MEMBERS_FILE, 'w') as f:
                json.dump(members_data, f, indent=2)
        except IOError as e:
            print(f"Error saving members: {e}")
        
        # Save transactions
        try:
            with open(TRANSACTIONS_FILE, 'w') as f:
                json.dump(self.transactions, f, indent=2)
        except IOError as e:
            print(f"Error saving transactions: {e}")
    
    def _record_transaction(self, action: str, details: Dict):
        """Record a transaction."""
        transaction = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "details": details
        }
        self.transactions.append(transaction)
        # Keep only last 1000 transactions
        if len(self.transactions) > 1000:
            self.transactions = self.transactions[-1000:]
    
    # Book Management
    
    def add_book(self, title: str, author: str, isbn: str, year: int, 
                 category: str = "Unknown", copies: int = 1) -> bool:
        """Add a new book to the library."""
        if isbn in self.books:
            return False
        
        book = Book(title, author, isbn, year, category, copies)
        self.books[isbn] = book
        
        self._record_transaction("ADD_BOOK", {
            "isbn": isbn,
            "title": title,
            "author": author,
            "copies": copies
        })
        
        self._save_data()
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """Remove a book from the library."""
        if isbn not in self.books:
            return False
        
        book = self.books[isbn]
        if book.available_copies != book.total_copies:
            return False  # Can't remove if copies are borrowed
        
        del self.books[isbn]
        
        self._record_transaction("REMOVE_BOOK", {
            "isbn": isbn,
            "title": book.title
        })
        
        self._save_data()
        return True
    
    def update_book_copies(self, isbn: str, new_total: int) -> bool:
        """Update the number of copies of a book."""
        if isbn not in self.books:
            return False
        
        book = self.books[isbn]
        if new_total < book.total_copies - book.available_copies:
            return False  # Can't reduce below borrowed copies
        
        book.total_copies = new_total
        book.available_copies = new_total - (book.total_copies - book.available_copies)
        
        self._record_transaction("UPDATE_BOOK_COPIES", {
            "isbn": isbn,
            "old_total": book.total_copies,
            "new_total": new_total
        })
        
        self._save_data()
        return True
    
    # Member Management
    
    def register_member(self, name: str, email: str, phone: str = "") -> Optional[str]:
        """Register a new member and return member ID."""
        # Check if email already exists
        for member in self.members.values():
            if member.email == email:
                return None
        
        member = Member(name, email, phone)
        self.members[member.member_id] = member
        
        self._record_transaction("REGISTER_MEMBER", {
            "member_id": member.member_id,
            "name": name,
            "email": email
        })
        
        self._save_data()
        return member.member_id
    
    def update_member(self, member_id: str, **kwargs) -> bool:
        """Update member information."""
        if member_id not in self.members:
            return False
        
        member = self.members[member_id]
        allowed_fields = ["name", "email", "phone", "max_books", "is_active"]
        
        for field, value in kwargs.items():
            if field in allowed_fields and hasattr(member, field):
                setattr(member, field, value)
        
        self._record_transaction("UPDATE_MEMBER", {
            "member_id": member_id,
            "updates": kwargs
        })
        
        self._save_data()
        return True
    
    def deactivate_member(self, member_id: str) -> bool:
        """Deactivate a member."""
        return self.update_member(member_id, is_active=False)
    
    # Borrowing System
    
    def borrow_book(self, member_id: str, isbn: str, days: int = 14) -> bool:
        """Borrow a book for a member."""
        if member_id not in self.members:
            return False
        
        if isbn not in self.books:
            return False
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        # Check conditions
        if not member.can_borrow():
            return False
        
        if not book.is_available():
            return False
        
        # Perform borrowing
        if member.borrow_book(isbn, days) and book.check_out(member_id, days):
            self._record_transaction("BORROW_BOOK", {
                "member_id": member_id,
                "isbn": isbn,
                "due_date": (date.today() + timedelta(days=days)).isoformat()
            })
            
            self._save_data()
            return True
        
        return False
    
    def return_book(self, member_id: str, isbn: str) -> bool:
        """Return a borrowed book."""
        if member_id not in self.members:
            return False
        
        if isbn not in self.books:
            return False
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        # Perform return
        if member.return_book(isbn) and book.return_book(member_id):
            self._record_transaction("RETURN_BOOK", {
                "member_id": member_id,
                "isbn": isbn,
                "return_date": date.today().isoformat()
            })
            
            self._save_data()
            return True
        
        return False
    
    def pay_fine(self, member_id: str, amount: float) -> float:
        """Pay fine for a member and return change."""
        if member_id not in self.members:
            return amount
        
        member = self.members[member_id]
        change = member.pay_fine(amount)
        
        if amount > 0:
            self._record_transaction("PAY_FINE", {
                "member_id": member_id,
                "amount": amount,
                "remaining_fine": member.fines
            })
            
            self._save_data()
        
        return change
    
    # Search Functionality
    
    def search_books(self, **kwargs) -> List[Book]:
        """Search books by various criteria."""
        results = []
        
        for book in self.books.values():
            match = True
            
            if "title" in kwargs and kwargs["title"].lower() not in book.title.lower():
                match = False
            
            if "author" in kwargs and kwargs["author"].lower() not in book.author.lower():
                match = False
            
            if "isbn" in kwargs and kwargs["isbn"] != book.isbn:
                match = False
            
            if "category" in kwargs and kwargs["category"].lower() != book.category.lower():
                match = False
            
            if "year" in kwargs and kwargs["year"] != book.year:
                match = False
            
            if "available_only" in kwargs and kwargs["available_only"] and not book.is_available():
                match = False
            
            if match:
                results.append(book)
        
        return results
    
    def search_members(self, **kwargs) -> List[Member]:
        """Search members by various criteria."""
        results = []
        
        for member in self.members.values():
            match = True
            
            if "name" in kwargs and kwargs["name"].lower() not in member.name.lower():
                match = False
            
            if "email" in kwargs and kwargs["email"].lower() not in member.email.lower():
                match = False
            
            if "member_id" in kwargs and kwargs["member_id"] != member.member_id:
                match = False
            
            if "active_only" in kwargs and kwargs["active_only"] and not member.is_active:
                match = False
            
            if match:
                results.append(member)
        
        return results
    
    # Reports
    
    def get_overdue_books_report(self) -> Dict:
        """Generate report of overdue books."""
        report = {
            "generated": datetime.now().isoformat(),
            "overdue_books": [],
            "total_overdue": 0,
            "total_fines": 0.0
        }
        
        for book in self.books.values():
            overdue_borrowers = book.get_overdue_borrowers()
            if overdue_borrowers:
                for member_id, due_date in overdue_borrowers:
                    member = self.members.get(member_id)
                    if member:
                        days_overdue = (date.today() - date.fromisoformat(due_date)).days
                        fine = days_overdue * 0.25
                        
                        report["overdue_books"].append({
                            "title": book.title,
                            "author": book.author,
                            "isbn": book.isbn,
                            "member_id": member_id,
                            "member_name": member.name,
                            "due_date": due_date,
                            "days_overdue": days_overdue,
                            "fine": fine
                        })
        
        report["total_overdue"] = len(report["overdue_books"])
        report["total_fines"] = sum(item["fine"] for item in report["overdue_books"])
        
        return report
    
    def get_popular_books_report(self, limit: int = 10) -> List[Dict]:
        """Get report of most popular books."""
        books_with_borrow_count = []
        
        for book in self.books.values():
            borrowed_count = book.total_copies - book.available_copies
            books_with_borrow_count.append({
                "book": book,
                "borrowed_count": borrowed_count,
                "borrow_percentage": (borrowed_count / book.total_copies * 100) if book.total_copies > 0 else 0
            })
        
        # Sort by borrowed count (descending)
        books_with_borrow_count.sort(key=lambda x: x["borrowed_count"], reverse=True)
        
        return [
            {
                "title": item["book"].title,
                "author": item["book"].author,
                "isbn": item["book"].isbn,
                "total_copies": item["book"].total_copies,
                "available_copies": item["book"].available_copies,
                "borrowed_count": item["borrowed_count"],
                "borrow_percentage": item["borrow_percentage"]
            }
            for item in books_with_borrow_count[:limit]
        ]
    
    def get_member_activity_report(self) -> Dict:
        """Generate member activity report."""
        active_members = [m for m in self.members.values() if m.is_active]
        inactive_members = [m for m in self.members.values() if not m.is_active]
        
        total_borrowed = sum(len(m.borrowed_books) for m in self.members.values())
        total_fines = sum(m.fines for m in self.members.values())
        
        return {
            "generated": datetime.now().isoformat(),
            "total_members": len(self.members),
            "active_members": len(active_members),
            "inactive_members": len(inactive_members),
            "total_books_borrowed": total_borrowed,
            "members_with_fines": len([m for m in self.members.values() if m.fines > 0]),
            "total_fines": total_fines,
            "avg_books_per_member": total_borrowed / len(self.members) if self.members else 0
        }
    
    def get_library_statistics(self) -> Dict:
        """Get overall library statistics."""
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books
        
        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "unique_titles": len(self.books),
            "total_members": len(self.members),
            "active_members": len([m for m in self.members.values() if m.is_active]),
            "total_transactions": len(self.transactions)
        }
    
    # Utility Methods
    
    def get_book(self, isbn: str) -> Optional[Book]:
        """Get book by ISBN."""
        return self.books.get(isbn)
    
    def get_member(self, member_id: str) -> Optional[Member]:
        """Get member by ID."""
        return self.members.get(member_id)
    
    def get_member_by_email(self, email: str) -> Optional[Member]:
        """Get member by email."""
        for member in self.members.values():
            if member.email == email:
                return member
        return None
    
    def get_books_borrowed_by_member(self, member_id: str) -> List[Book]:
        """Get list of books borrowed by a member."""
        if member_id not in self.members:
            return []
        
        member = self.members[member_id]
        books = []
        for isbn, _ in member.borrowed_books:
            book = self.books.get(isbn)
            if book:
                books.append(book)
        return books


def main():
    """Main function to run the library management system."""
    library = Library()
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)
    
    # Add some sample data if library is empty
    if not library.books:
        print("\nAdding sample books...")
        sample_books = [
            ("Python Programming", "John Doe", "978-0134444321", 2020, "Programming", 5),
            ("Data Science Handbook", "Jane Smith", "978-1119092940", 2019, "Data Science", 3),
            ("Clean Code", "Robert Martin", "978-0132350884", 2008, "Software Engineering", 4),
            ("The Pragmatic Programmer", "Andrew Hunt", "978-0201616224", 1999, "Software Engineering", 2),
            ("Design Patterns", "Erich Gamma", "978-0201633610", 1994, "Software Engineering", 3),
        ]
        
        for title, author, isbn, year, category, copies in sample_books:
            library.add_book(title, author, isbn, year, category, copies)
    
    if not library.members:
        print("Adding sample members...")
        sample_members = [
            ("Alice Johnson", "alice@example.com", "555-0101"),
            ("Bob Smith", "bob@example.com", "555-0102"),
            ("Charlie Brown", "charlie@example.com", "555-0103"),
        ]
        
        for name, email, phone in sample_members:
            library.register_member(name, email, phone)
    
    # Demo some functionality
    print("\nLibrary Statistics:")
    stats = library.get_library_statistics()
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    print("\nSearching for programming books:")
    programming_books = library.search_books(category="Programming")
    for book in programming_books:
        print(f"  - {book}")
    
    print("\nDemo borrowing system:")
    # Get first member and book
    member_id = list(library.members.keys())[0]
    book_isbn = list(library.books.keys())[0]
    
    member = library.get_member(member_id)
    book = library.get_book(book_isbn)
    
    print(f"  Member: {member.name}")
    print(f"  Book: {book.title}")
    
    if library.borrow_book(member_id, book_isbn):
        print(f"  ✓ Successfully borrowed '{book.title}'")
    else:
        print(f"  ✗ Could not borrow '{book.title}'")
    
    # Show updated status
    print(f"\n  Updated book status: {book}")
    print(f"  Member borrowed books: {len(member.borrowed_books)}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)
    print("\nThe library management system is ready to use!")
    print(f"Data is saved in the '{DATA_DIR}' directory.")
    print("\nAvailable functionality:")
    print("  - Book management (add, remove, update)")
    print("  - Member management (register, update, deactivate)")
    print("  - Borrowing and returning system")
    print("  - Search functionality")
    print("  - Overdue fines calculation")
    print("  - Reports generation")
    print("  - Data persistence with JSON")


if __name__ == "__main__":
    main()
