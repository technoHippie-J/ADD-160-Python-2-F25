# Methods for user input
"""The methods used for entering user input. Input constraints implemented where applicable"""


def user_entry_first_name(contact):
    complete = False
    while not complete:
        print("Please enter the contact's first name: \n")
        new_first_name = input("Enter: ").strip()
        try:
            contact.first_name = new_first_name
            complete = True
            print(f"First name set to: {contact.first_name}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_last_name(contact):
    complete = False
    while not complete:
        print("Please enter the contact's last name: \n")
        new_last_name = input("Enter: ").strip()
        try:
            contact.last_name = new_last_name
            complete = True
            print(f"Last name set to: {contact.last_name}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_birthday(contact):
    complete = False
    while not complete:
        print(
            "Please enter the contact's birthday in the following format:\n\n"
            "YYYY/MM/DD\n\n"
        )
        new_birthday = input("Enter: ").strip()
        try:
            contact.birthday = new_birthday
            complete = True
            print(f"Birthday set to: {contact.birthday}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_email(contact):
    complete = False
    while not complete:
        print("Please enter the contact's email: \n")
        new_email = input("Enter: ").strip()
        try:
            contact.email = new_email
            complete = True
            print(f"Email set to: {contact.email}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_street_address(contact):
    complete = False
    while not complete:
        print("Please enter the contact's street address: \n")
        new_street_address = input("Enter: ").strip()
        try:
            contact.street_address = new_street_address
            complete = True
            print(f"Street address set to: {contact.street_address}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_city(contact):
    complete = False
    while not complete:
        print("Please enter the contact's city: \n")
        new_city = input("Enter: ").strip()
        try:
            contact.city = new_city
            complete = True
            print(f"City set to: {contact.city}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_state(contact):
    complete = False
    while not complete:
        print("Please enter the contact's state: \n")
        new_state = input("Enter: ").strip()
        try:
            contact.state = new_state
            complete = True
            print(f"State set to: {contact.state}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_country(contact):
    complete = False
    while not complete:
        print("Please enter the contact's three-letter country code: \n")
        new_country = input("Enter: ").strip()
        try:
            contact.country = new_country
            complete = True
            print(f"Country set to: {contact.country}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_zip_code(contact):
    complete = False
    while not complete:
        print("Please enter the contact's zip code: \n")
        new_zip_code = input("Enter: ").strip()
        try:
            contact.zip_code = new_zip_code
            complete = True
            print(f"Zip code set to: {contact.zip_code}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")


def user_entry_phone(contact):
    complete = False
    while not complete:
        print(
            "Please enter the contact's phone number in the following format, including dashes:\n\n"
            "xxx-xxx-xxxx\n\n"
        )
        new_phone = input("Enter: ").strip()
        try:
            contact.phone = new_phone
            complete = True
            print(f"Phone number set to: {contact.phone}")
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")
