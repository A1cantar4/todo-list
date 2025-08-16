<div align="center">
  <picture>
    <img src="assets/img/logo.png" alt="Logo" width="80%">
  </picture>
</div>

<div align="center">
  <h1>To-Do List Project (Terminal & GUI)</h1>
</div>

This repository contains two Python-based to-do list applications, both with a user interface available in **multiple languages** (Portuguese, English, Spanish, French, German, Russian, Arabic, Hindi, Bengali, Urdu, Chinese), while the code and commits remain in **English**, designed for learning and practical usage.  
This project uses `pytest` for unit testing.

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
├── assets/
│   └── img/
│       ├── logo.png                  # Logo for README
│       ├── screenshot-terminal.png   # Terminal screenshot for Readme
│       └── screenshot-tkinter.png    # Tkinter screenshot for Readme
│
├── settings/
│   ├── settings.py                   # Save/load configs
│   ├── settings.json                 # Languages
│   ├── tasks.json
│   └── locales/
│       ├── en.json                   # English
│       ├── zh.json                   # 中文 (Mandarim)
│       ├── hi.json                   # हिंदी (Hindi)
│       ├── de.json                   # Deutsch
│       ├── es.json                   # Español
│       ├── fr.json                   # Français
│       ├── ar.json                   # العربية
│       ├── bn.json                   # বাংলা (Bengali)
│       ├── ru.json                   # Русский
│       ├── pt.json                   # Português
│       └── ur.json                   # اُردُو
│
├── tests/
│   └── test_todo.py                  # Pytest
│
├── todo_list/
|   ├── i18n.py                       # Translate msg
|   ├── storage.py                    # Save/load
|   ├── todo_core.py                  # Add and Remove Functions to import
│   ├── todo_terminal.py              # Terminal-based version (chat-style interface)
│   └── todo_tkinter.py               # GUI version using Tkinter
│
├── .gitignore                        # Simple gitignore
├── CHANGELOG.md                      # All changes
├── CONTRIBUITING.md                  # Instructions to contribuiting
├── README.md                         # Project documentation
├── LICENSE                           # MIT License
└── requirements.txt              
```

---

## Features

### Terminal Version (`todo_terminal.py`)
- Automatic language selection on first run.
- Change language anytime directly from the program (menu option or button).
- Clear input validation and error messages.
- Infinite menu loop until user exits.
- Each task is stored with a unique ID, ensuring correct deletion without affecting other tasks.

### GUI Version (`todo_tkinter.py`)
- Clean and minimal Tkinter interface.
- Automatic language selection on first run.
- Change language anytime directly from the program (menu option or button).
- Add task via text input.
- Remove selected task from the list.
- Auto-refreshes task list when modified.

### Functions to import (`todo_core.py`)
- Add and Remove task on list (tasks).

---

## Internationalization (i18n)

- The project supports **11 languages** out of the box:
  - 🇧🇷 Portuguese (`pt`)
  - 🇺🇸 English (`en`)
  - 🇪🇸 Spanish (`es`)
  - 🇫🇷 French (`fr`)
  - 🇩🇪 German (`de`)
  - 🇷🇺 Russian (`ru`)
  - 🇸🇦 Arabic (`ar`)
  - 🇮🇳 Hindi (`hi`)
  - 🇧🇩 Bengali (`bn`)
  - 🇵🇰 Urdu (`ur`)
  - 🇨🇳 Chinese (`zh`)

- Automatic language selection on the first run.  
- Change the language anytime directly from the menu (Terminal) or button (Tkinter).  
- Easy to extend: just add a new `.json` file under `settings/locales/` with translations.

---

## Requirements

- Python 3.x (recommended: 3.8+)
- No external libraries needed to run the project (only built-in modules).
- **pytest** (for running tests).

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

![Versão](https://img.shields.io/badge/version-2.0.0-blue.svg)
![i18n](https://img.shields.io/badge/i18n-11_languages-green.svg)

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## Author

**Lucas Alcântara**  
GitHub: [@A1cantar4](https://github.com/A1cantar4)