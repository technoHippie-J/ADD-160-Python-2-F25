# Address Book Application

**Author:** Anthony Janus
**Class:** Intermediate Python - Week 2 Assignment

## Description

This is a command-line application for managing a simple address book. It allows users to create new contacts and view pre-loaded contact information as required by the assignment.

### File Structure

1. __main__.py - Program logic; includes user menu(new user, new contact, run assignment reqs, quit)
2. address_book.py - Class(_sort_key(), magic methods (__eq__, __lt__, __str__), properties:getters/setters(with validation)/deleters) for address book entires
3. addrbk_user_input.py - User input module

## Prerequisites

- Python 3.6 or newer.
- No external libraries are needed. The application only uses Python's standard library.

## How to Run the Application

1.  Unzip the file `tjanus_addrbk.zip`.

### Through the CLI/On Mac/Linux
2.  Open a terminal (on Mac/Linux) or Command Prompt/PowerShell (on Windows).
3.  Navigate into the unzipped project folder using the `cd` command. For example:

    `cd path/to/YourName_AddressBookProject`

4.  Run the following command to start the application:

    ```bash
    python __main__.py
    ```
    *(Note: On some systems, you may need to use `python3` instead of `python`)*

### On Windows
2. Navigate into the unzipped project folder using the `cd` command. For example:

    `cd path/to/tjanus_addrbk/dist/`

3. Run the .exe file in the dist folder called:

    `__main__.exe`

---