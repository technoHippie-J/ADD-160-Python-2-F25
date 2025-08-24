# INTERMEDIATE PYTHON - ADD-160-001L (Fall 2025)

*(This README.md file created with help from ChatGPT 5 Thinking)*

This repository contains my coursework for **Intermediate Python (ADD-160-001L)**. It follows the class modules on OOP best practices, GUI development, RESTful APIs, and file processing.

> If you’re grading: everything here is my own work unless otherwise credited.

---

## Table of Contents

- [INTERMEDIATE PYTHON - ADD-160-001L (Fall 2025)](#intermediate-python---add-160-001l-fall-2025)
  - [Table of Contents](#table-of-contents)
  - [Course at a Glance](#course-at-a-glance)
  - [Repo Structure](#repo-structure)
  - [Environment \& Setup](#environment--setup)
  - [Run Instructions](#run-instructions)
  - [Code Style \& Quality](#code-style--quality)
  - [Weekly Modules \& Deliverables](#weekly-modules--deliverables)
  - [Unit 1: Advanced OOP + Best Practices](#unit-1-advanced-oop--best-practices)
  - [Unit 2: GUI Programming](#unit-2-gui-programming)
  - [Unit 3: RESTful APIs](#unit-3-restful-apis)
  - [Unit 4: File Processing](#unit-4-file-processing)
  - [Resources](#resources)
  - [License](#license)

---

## Course at a Glance

- **Term:** Fall 2025  
- **Modality/Tools:** Canvas, LinkedIn Learning, Python Institute, VS Code, GitHub  
- **Focus Areas:**  
  1) Advanced OOP (classes, inheritance, decorators, abstract classes, composition, metaprogramming)  
  2) Best Practices (PEP 8, PEP 257, packaging, exceptions, copying/serialization)  
  3) GUI Programming (widgets, events, canvas, state)  
  4) RESTful APIs (JSON, requests, CRUD)  
  5) File Processing (SQLite intro, XML, CSV, logging, configparser)

---

## Repo Structure

> This is the intended layout; some folders will be added as we go.

```text
/
├─ unit1_oop/
│ ├─ wk01/
│ ├─ wk02/
│ ├─ wk03/
│ ├─ wk04/
│ ├─ wk05/
│ └─ wk06/
├─ unit2_gui/
│ ├─ wk07/
│ ├─ wk08/
│ ├─ wk09/
│ └─ wk10/
├─ unit3_api/
│ ├─ wk11/
│ └─ wk12/
├─ unit4_files/
│ ├─ wk13/
│ ├─ wk14/
│ ├─ wk15/
│ └─ wk16/
├─ tests/ # pytest tests (where applicable)
├─ notes/ # lecture notes / scratch
├─ data/ # sample datasets
├─ requirements.txt
└─ README.md

```

---

## Environment & Setup

- **Python:** 3.11+ recommended  
- **Editor:** Visual Studio Code (Python extension, Pylance, Black/autopep8, isort)  
- **Virtual env (Windows):**
  
  ```powershell
  py -3 -m venv .venv
  .\.venv\Scripts\activate
  pip install -U pip
  pip install -r requirements.txt
  ```

- If a sub-folder has its own requirements.txt, install that too from the same activated venv.

---

## Run Instructions

Most exercises are simple scripts or small packages.

Run a script:

python path\to\script.py

Run tests (if present):

pytest -q

---

## Code Style & Quality

PEP 8 for styling and PEP 257 for docstrings.

Prefer type hints and docstrings:

def area(radius: float) -> float:
    """Return the area of a circle."""
    ...

Handle errors explicitly (no silent excepts).

Keep modules focused; prefer composition over inheritance when it clarifies design.

Use logging (not print) for diagnostic output in larger tasks.

---

## Weekly Modules & Deliverables

## Unit 1: Advanced OOP + Best Practices

**Week 1** - due Aug 24

 OOP 1.1 - Review of OOP (5 pts)

 OOP 1.2 - Class and Instance Data (5 pts)

**Week 2** - due Sep 7

 OOP 2.1 - Core Syntax (5 pts)

 OOP 2.2 - Inheritance and Polymorphism (5 pts)

 OOP 2.3 - Extended Function Argument Syntax (5 pts)

 Best Practices 1.1 - What is PEP? & 1.2 - The Zen of Python (5 pts)

**Week 3** - due Sep 14

 OOP 2.4 - Decorators (5 pts)

 OOP 2.5 - Different Faces of Python Methods (5 pts)

 OOP 2.6 - Abstract Classes (5 pts)

 Best Practice 1.3 - PEP 8 Introduction (page)

**Week 4** - due Sep 21

 OOP 2.7 - Encapsulation (5 pts)

 OOP 2.8 - Composition vs Inheritance (5 pts)

 OOP 2.9 - Inheriting from Built-in Classes (5 pts)

 Best Practices 4.1 - PEP 257 Docstring Conventions (5 pts)

**Week 5** - due Sep 28

 OOP 3.1 - Advanced Exceptions (5 pts)

 OOP 4.1 - Shallow vs Deep Copy (5 pts)

 OOP 4.2 - Serialization with pickle (5 pts)

**Week 6** - due Oct 5

 OOP 4.3 - Serialization with shelve (5 pts)

 OOP 5.1 - Metaprogramming (5 pts)

 Test 1: OOP (30 pts)

 Test 2: Best Practices (10 pts)

## Unit 2: GUI Programming

**Week 7** - due Oct 12

 GUI 1.1 & 1.2 - Intro to GUI Programming (5 pts)

 GUI 1.3 - Settling Widgets in the Window (5 pts)

 GUI 1.4 - Coloring Widgets (5 pts)

 GUI 1.5 - A Simple GUI Application (5 pts)

**Week 8** - due Oct 19

 GUI 1.6 - Events & Handlers (5 pts)

 GUI 1.7 - Visiting Widget Properties (5 pts)

 GUI 1.8 - Interacting with Widget Methods (5 pts)

 GUI 1.9 - Looking at Variables (5 pts)

**Week 9** - due Oct 26

 GUI 2.1 - Lexicon of Widgets, Part 1 (5 pts)

 GUI 2.2 - Lexicon of Widgets, Part 2 (5 pts)

 GUI 2.3 - Lexicon of Widgets, Part 3 (5 pts)

**Week 10** - due Nov 2

 GUI 2.4 - Shaping the Main Window & Dialogs (5 pts)

 GUI 2.5 - Working with the Canvas (5 pts)

 GUI 3.1 - Intro to GUI Programming in Python (5 pts)

 Test 3: GUI (10 pts)

## Unit 3: RESTful APIs

**Week 11** - due Nov 9

 API 1.1 - Networks, Layers, Internet (5 pts)

 API 1.2 - Using Sockets in Python (5 pts)

 API 1.3 - JSON Basics (5 pts)

 API 1.4 - Working with JSON in Python (5 pts)

**Week 12** - due Nov 16

 API 1.5 - Why JSON over XML (5 pts)

 API 1.6 - requests Module (5 pts)

 API 1.7 - CRUD (5 pts)

 Test 3: RESTful APIs (10 pts)

## Unit 4: File Processing

**Week 13** - due Nov 23

 Files 1.1 & 1.2 - SQLite / What is a Database (5 pts)

 Files 1.3 - Data (5 pts)

 Files 1.4 - Practice (5 pts)

 Files 2.1 - XML Files (5 pts)

**Week 14** - due Nov 30

 Files 2.2 - XML Practice 1 (5 pts)

 Files 2.4 - XML Practice 2 (5 pts)

 Files 3.1 - The csv Module (5 pts)

 Files 3.4 - CSV (5 pts)

**Week 15** - due Dec 7

 Files 4.1 - Logging in Python (5 pts)

 Files 4.2 - Logging (5 pts)

 Files 5.1 - configparser (5 pts)

 Files 5.2 - Interpolating Values (5 pts)

**Week 16** - due Dec 11

 Test 3: Files (10 pts)

---

## Resources

Python Institute - certification & learning materials

LinkedIn Learning - supplemental video courses

PEP 8 / PEP 257 - style & docstring conventions

MCC Library - research support

Canvas - assignments, grades, office hours, announcements

---

## License

This repository is for educational use. Unless otherwise noted, code is © 2025 by me and not licensed for commercial reuse.
