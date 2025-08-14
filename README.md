<div align="center">
  <picture>
    <img src="assets/img/logo.png" alt="Logo" width="80%">
  </picture>
</div>

<div align="center">
  <h1>To-Do List Project (Terminal & GUI)</h1>
</div>

This repository contains two Python-based to-do list applications, both with a user interface in **Portuguese** but code and commits in **English**, designed for learning and practical usage. This project uses `pytest` for unit testing.

---

## Screenshots

**Tkinter Version**
<img src="assets/img/screenshot-tkinter.png" alt="Tkinter Screenshot" width="250px">

**Terminal Version**
<img src="assets/img/screenshot-terminal.png" alt="Terminal Screenshot" width="250px">

---

## Project Structure

```
todo-list/
│
├── todo_list/
|   ├── todo_core.py              # Add and Remove Functions to import
│   ├── todo_terminal.py          # Terminal-based version (chat-style interface)
│   └── todo_tkinter.py           # GUI version using Tkinter
│
├── tests/
│   └── test_todo.py              # Pytest
│
├── img/
│    ├── logo.png                 # Logo for README
│    ├── screenshot-terminal.png  # Terminal screenshot for Readme
│    └── screenshot-tkinter.png   # Tkinter screenshot for Readme
├── .gitignore                    # Simple gitignore
├── CHANGELOG.md                  # All changes
├── README.md                     # Project documentation

```

---

## Features

### Terminal Version (`todo_terminal.py`)
- Add, list, and remove tasks via terminal
- Clear input validation and error messages
- Infinite menu loop until user exits

### GUI Version (`todo_tkinter.py`)
- Clean and minimal Tkinter interface
- Add task via text input
- Remove selected task from the list
- Auto-refreshes task list when modified

### Functions to import (`todo_core.py`)
- Add and Remove task on list (tasks)

---

## Requirements

- Python 3.x (recommended: 3.8+)
- No external libraries needed to run the project (only built-in modules)
- **pytest** (for running tests)

---

## How to Run

### Terminal version:
```bash
python todo_list/todo_terminal.py
```

### GUI version (Tkinter):
```bash
python todo_list/todo_tkinter.py
```

---

## How to Run Tests

**1. Install pytest** (if you don’t have it yet):
```bash
pip install pytest
```

**2. Run the tests**:
```bash
pytest
```

Pytest will automatically discover tests inside the `tests/` directory and run them.

---

## Notes

- The interface language is **Portuguese**, but all code, commits, and documentation are in **English**.
- You can expand this project by adding save/load features using JSON or text files.

![Versão](https://img.shields.io/badge/version-1.2.0-blue.svg)

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## Author

**Lucas Alcântara**  
GitHub: [@A1cantar4](https://github.com/A1cantar4)