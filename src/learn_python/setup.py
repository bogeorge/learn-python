#!/usr/bin/env python3
"""
Python Learning Workspace Setup Script

This script helps set up your Python learning environment.
Run it with: python3 setup.py
"""

import os
import platform
import subprocess
import sys


def print_header():
    """Print a welcome header."""
    print("=" * 60)
    print("PYTHON LEARNING WORKSPACE SETUP")
    print("=" * 60)
    print()


def check_python_version():
    """Check if Python 3 is installed."""
    print("1. Checking Python version...")
    version = sys.version_info

    if version.major < 3:
        print("❌ ERROR: Python 3 is required. Please install Python 3.6 or higher.")
        print(f"   Current version: {sys.version}")
        return False
    elif version.minor < 6:
        print(f"⚠️  WARNING: Python 3.6+ recommended. Current: {sys.version}")
        print("   Some features may not work optimally.")
        return True
    else:
        print(f"✅ Python {sys.version} is installed.")
        return True


def check_virtualenv():
    """Check if virtual environment exists."""
    print("\n2. Checking virtual environment...")

    venv_path = os.path.join(os.path.dirname(__file__), "venv")

    if os.path.exists(venv_path):
        print("✅ Virtual environment already exists at 'venv/'")
        return True
    else:
        print("❌ Virtual environment not found.")
        print("   Run: python3 -m venv venv")
        return False


def create_virtualenv():
    """Create a virtual environment."""
    print("\nCreating virtual environment...")

    try:
        # Check if venv module is available
        subprocess.run(
            [sys.executable, "-m", "venv", "--help"], capture_output=True, check=True
        )

        # Create virtual environment
        result = subprocess.run(
            [sys.executable, "-m", "venv", "venv"], capture_output=True, text=True
        )

        if result.returncode == 0:
            print("✅ Virtual environment created successfully.")
            return True
        else:
            print(f"❌ Failed to create virtual environment: {result.stderr}")
            return False

    except subprocess.CalledProcessError:
        print("❌ venv module not available.")
        print("   On some systems, you might need to install python3-venv:")
        print("   Ubuntu/Debian: sudo apt install python3-venv")
        print("   macOS: python3 -m ensurepip")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def check_pip():
    """Check if pip is installed and working."""
    print("\n3. Checking pip...")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"], capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"✅ pip is installed: {result.stdout.split()[1]}")
            return True
        else:
            print("❌ pip is not working properly.")
            return False

    except Exception as e:
        print(f"❌ Error checking pip: {e}")
        return False


def upgrade_pip():
    """Upgrade pip to the latest version."""
    print("\nUpgrading pip...")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print("✅ pip upgraded successfully.")
            return True
        else:
            print(f"❌ Failed to upgrade pip: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ Error upgrading pip: {e}")
        return False


def install_basic_packages():
    """Install basic Python packages for learning."""
    print("\n4. Installing basic packages...")

    packages = [
        "ipython",  # Interactive Python shell
        "black",  # Code formatter
        "flake8",  # Linter
        "pytest",  # Testing framework
    ]

    try:
        for package in packages:
            print(f"   Installing {package}...")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:
                print(f"   ✅ {package} installed")
            else:
                print(f"   ❌ Failed to install {package}: {result.stderr}")

        print("\n✅ Basic packages installed.")
        return True

    except Exception as e:
        print(f"❌ Error installing packages: {e}")
        return False


def print_activation_instructions():
    """Print instructions for activating the virtual environment."""
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)

    print("\nTo activate your virtual environment:")

    system = platform.system().lower()

    if system == "windows":
        print("""
    In Command Prompt:
        venv\\Scripts\\activate
    
    In PowerShell:
        .\\venv\\Scripts\\Activate.ps1
        """)
    else:  # macOS, Linux
        print("""
    In terminal:
        source venv/bin/activate
    
    To deactivate:
        deactivate
        """)

    print("\nOnce activated, your prompt should show (venv).")
    print("All Python packages will be installed in this environment.")


def print_next_steps():
    """Print next steps for learning."""
    print("\n" + "=" * 60)
    print("NEXT STEPS")
    print("=" * 60)

    print("""
1. Read the learning plan:
   - cat PYTHON_LEARNING_PLAN.md
   - cat WEEKLY_SCHEDULE.md

2. Start with Day 1 exercises:
   - python exercises/week1_day1.py

3. Try the beginner projects:
   - python projects/beginner/01_simple_calculator.py

4. Explore resources:
   - cat resources/learning_resources.md

5. Track your progress in docs/progress.md
    """)


def create_progress_file():
    """Create a progress tracking file."""
    print("\n5. Creating progress tracking file...")

    progress_path = os.path.join(os.path.dirname(__file__), "docs", "progress.md")

    # Create docs directory if it doesn't exist
    os.makedirs(os.path.dirname(progress_path), exist_ok=True)

    if os.path.exists(progress_path):
        print("✅ Progress file already exists.")
        return True

    progress_content = """# Learning Progress Tracker

## Daily Log

### [Date]
- **Concepts Learned**: 
- **Exercises Completed**:
- **Challenges Faced**:
- **Questions to Research**:
- **Time Spent**: 

## Week [Week Number] Summary

### Concepts Mastered
- [ ] 
- [ ] 
- [ ] 

### Projects Completed
- [ ] 
- [ ] 
- [ ] 

### Key Takeaways
1. 
2. 
3. 

### Goals for Next Week
1. 
2. 
3. 

## Milestones

### Week 1 Goals
- [ ] Complete Python basics
- [ ] Build first project
- [ ] Understand variables and control flow

### Week 2 Goals  
- [ ] Master functions
- [ ] Work with data structures
- [ ] Complete intermediate project

### Week 3 Goals
- [ ] Understand OOP concepts
- [ ] Handle files and errors
- [ ] Build object-oriented project

### Week 4 Goals
- [ ] Work with external data
- [ ] Use advanced Python features
- [ ] Complete capstone project

## Resources to Revisit
- 
- 
- 

## Notes
Add any additional notes, insights, or reminders here.

---
*Last updated: [Date]*
"""

    try:
        with open(progress_path, "w") as f:
            f.write(progress_content)
        print("✅ Progress file created at docs/progress.md")
        return True
    except Exception as e:
        print(f"❌ Error creating progress file: {e}")
        return False


def main():
    """Main setup function."""
    print_header()

    # Check Python version
    if not check_python_version():
        return

    # Check/create virtual environment
    if not check_virtualenv():
        create = input("\nCreate virtual environment? (y/n): ").strip().lower()
        if create == "y":
            if not create_virtualenv():
                print("\n⚠️  Continuing without virtual environment...")
        else:
            print("\n⚠️  Continuing without virtual environment...")

    # Check pip
    if not check_pip():
        print("\n⚠️  pip issues detected. Some features may not work.")

    # Upgrade pip
    upgrade = input("\nUpgrade pip to latest version? (y/n): ").strip().lower()
    if upgrade == "y":
        upgrade_pip()

    # Install packages
    install = input("\nInstall basic Python packages? (y/n): ").strip().lower()
    if install == "y":
        install_basic_packages()

    # Create progress file
    create_progress = input("\nCreate progress tracking file? (y/n): ").strip().lower()
    if create_progress == "y":
        create_progress_file()

    # Print instructions
    print_activation_instructions()
    print_next_steps()

    print("\n" + "=" * 60)
    print("Happy learning! 🐍")
    print("=" * 60)


if __name__ == "__main__":
    main()
