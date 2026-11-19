# Bo's AWS Lambda & Python Learning Workspace

A specialized learning environment focused on Python for AWS Lambda development with AWS Bedrock integration. Customized for Bo's career goals in serverless Python development.

## Structure

```
.
├── AWS_LAMBDA_ROADMAP.md      # 12-week AWS Lambda & Bedrock roadmap
├── PYTHON_LEARNING_PLAN.md    # General Python learning plan
├── WEEKLY_SCHEDULE.md         # Updated for AWS focus
├── README.md                  # This file
├── QUICK_START.md             # Get started in 5 minutes
├── WHAT_I_BUILT.md            # Workspace overview
├── setup.py                   # Interactive setup script
├── exercises/                 # AWS Lambda-focused exercises
│   ├── lambda_day1.py        # Day 1: Lambda patterns
│   ├── week1_day1.py         # General Python basics
│   └── week1_day2.py         # General Python data types
├── projects/                  # Practical projects
│   └── beginner/
│       ├── 01_simple_calculator.py
│       └── 02_number_guessing_game.py
├── docs/                      # Documentation & progress
│   └── progress.md           # Progress tracking
├── resources/                 # Learning materials
│   └── learning_resources.md
└── venv/                      # Python virtual environment
```

## Getting Started

### 1. Set Up Python Environment
```bash
# Check if Python is installed
python3 --version

# Set up virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 2. Install Basic Tools
```bash
# Upgrade pip
pip install --upgrade pip

# Install useful packages
pip install ipython  # Interactive Python shell
pip install black    # Code formatter
pip install flake8   # Linter
```

### 3. Start Learning
Begin with Week 1 in `WEEKLY_SCHEDULE.md` and follow the daily plan.

## Daily Workflow

1. **Morning Review** (10 min): Review previous day's concepts
2. **Learning Session** (30-60 min): Study new topic with examples
3. **Coding Practice** (30 min): Complete exercises in `exercises/` directory
4. **Project Work** (Optional): Work on current project
5. **Evening Review** (10 min): Reflect on what was learned

## Learning Resources

### Quick Start Guides
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
- [Learn Python in 10 Minutes](https://www.stavros.io/tutorials/python/)

### Practice Platforms
- [Exercism Python Track](https://exercism.org/tracks/python)
- [Python Practice Problems](https://www.practicepython.org/)
- [PyNative Exercises](https://pynative.com/python-exercises-with-solutions/)

### Reference Materials
- [Python Standard Library](https://docs.python.org/3/library/)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Common Python Gotchas](https://docs.python-guide.org/writing/gotchas/)

## Progress Tracking

Create a `progress.md` file in the `docs/` directory to track:
- ✅ Concepts mastered
- 🏗️ Projects completed  
- ❓ Questions to research
- 📈 Skill level progression

## Tips for Success

1. **Code Every Day**: Consistency beats intensity
2. **Build Real Projects**: Apply concepts immediately
3. **Read Others' Code**: Learn from open-source projects
4. **Debug Systematically**: Use print statements and debugger
5. **Ask for Help**: Use Stack Overflow, Reddit (r/learnpython)
6. **Teach What You Learn**: Explain concepts to reinforce understanding

## Project Ideas

### Beginner Level (Complete within 1-2 weeks)
- [ ] Calculator
- [ ] Number Guessing Game  
- [ ] To-Do List
- [ ] Simple Blog

### Intermediate Level (Complete within 3-4 weeks)
- [ ] Expense Tracker
- [ ] Weather App
- [ ] Password Manager
- [ ] Markdown to HTML Converter

### Advanced Level (Complete within 5-8 weeks)
- [ ] Web Scraper
- [ ] REST API
- [ ] Data Visualization Dashboard
- [ ] Machine Learning Model

## Next Steps

1. Read `PYTHON_LEARNING_PLAN.md` for the complete roadmap
2. Follow `WEEKLY_SCHEDULE.md` for daily guidance
3. Start with Day 1 exercises
4. Begin your first project in `projects/beginner/`

---

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*

Happy coding! 🐍