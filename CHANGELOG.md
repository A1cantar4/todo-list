# 📜 CHANGELOG

All significant changes to this project will be documented here.  
The format follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standard.  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.0.0] - 2025-08-15
### Added
- Support for 11 languages (ar, bn, de, en, es, fr, hi, pt, ru, ur, zh).
- Persistent language configuration via `settings.json`.
- `tasks.json` now stores all tasks persistently.
- New `i18n.py` module for loading translation files.
- New `storage.py` module for managing tasks with IDs.
- Added `locales/` folder with JSON translation files.
- Task IDs for better management and deletion.
- Internationalization support integrated in `todo_core`.

### Changed
- Updated `README.md` with i18n information and database(json).

## [1.2.0] - 2025-08-13
### Added
- This CHANGELOG.md.
- .gitignore.
- Logo to README.md (in "assets/img/logo.png").
- Screenshots of two programs (terminal and tkinter version) -> assets/img/screenshot-"..." .
- CONTRIBUITING.md -> to explain all the ways to contribute to my project.
- File "todo_core.py" (Function "Add" and "Remove" to tkinter and terminal python files) in "todo-list/".
- Pytest with four tests in "tests/test_todo.py".
- File "__init__".py -> tests/ and todo_list/.
- requirements with pytest.

### Fixed
- "test_todo.py" -> fixed the import and name of function.
- "listas" to -> "listar" in menu of "todo_terminal.py."

### Changed
- Modified README.md, new instructions about tests, added version, new center title and logo; and fixed correct height of screenshots.
- In todo-list tkinter -> added version of program.
- In todo-list tkinter -> refactored "task adding" and "removing" logic to support testing.
- In todo-list terminal -> added version of program.
- In todo-list terminal -> refactored "task adding" and "removing" logic to support testing.
- Removed "-" to LICENSE.
- Roved the Python files to "todo-list" folder.
- Name of imports in all python files.
- Modified name of python files in Readme and Contribuiting.

## [1.1.2] - 2025-07-23
### Added
- Global README.md.
- LICENSE.

### Changed
- Added " - " to license.
- Translated the comments and code from portuguese to english.

## [1.1.1] - 2025-07-17
### Added
- New python file, the Tkinter version of main program todo-list.

## [1.1.0] - 2025-07-08
### Changed
- Added space between lines of code (Main file).

### Fixed
- Infinite Loop after add task.

## [1.0.0] - 2025-07-07 
### Added
- Main file "todo-list-terminal-chat-style.py".